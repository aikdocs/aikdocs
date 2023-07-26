from atlassian import Confluence
import requests
from bs4 import BeautifulSoup
import os

base_url = "https://dwiki.daocloud.io"

f = open('config.yaml', 'r', encoding='utf-8')
secrets = yaml.load(f.read(), Loader=yaml.FullLoader)
username = secrets["GetVideos"]["username"]
password = secrets["GetVideos"]["password"]

confluence = Confluence(url=base_url, username=username, password=password)  # Create a confluence session.

page_id = "55332751"  # The ID of "道客公开课"
login_data = {  # Your login details here
    "os_username": username,
    "os_password": password
}

ids = confluence.get_child_id_list(page_id)  # Get all the IDs of the available file pages.

sesn = requests.session()  # Create a session so that we don't need to login every time when downloading files.
# A crawler requires login at the beginning. Original cookies of login wouldn't be recognized.
resp = sesn.post(base_url, login_data)


def BreakFileName(string):  # Return format: file_name, file_suffix.
    for i in range(len(string)-1, -1, -1):
        if string[i] == '.':
            return string[:i], string[i:]

for id in ids:
    vids = confluence.get_child_id_list(id)  # Get all the IDs of the available files in the file page.

    for vid in vids:
        url = base_url + "/pages/viewpage.action?pageId=" + vid  # Create the url for the file.
        resp = sesn.get(url)
        soup = BeautifulSoup(resp.content, "html.parser")
        ls = soup.find_all('a', class_='confluence-embedded-file')  # Locate the download link in the soup.
        meta_tag = soup.find('meta', attrs={'name': 'ajs-page-title'})
        name = meta_tag['content']

        cnt = 1
        for l in ls:  # Get the file name
            src = l['data-file-src']  # Get the download link of file.

            video_url = base_url + src  # Concatenate the link with the base url.
            download = sesn.get(video_url)  # Download session of the file.

            base_dir = "D:/DaoCloud_vids/"  # Prepare a folder to store all the files.

            if os.access(base_dir + name, os.F_OK):  # Prevents overlap of file names.
                filename, suffix = BreakFileName(name)
                # For example, if "zoom_0.mp4" already exists, a new file "zoom_0_1.mp4" is created instead.
                filename += '_' + str(cnt)
                name = filename + suffix
                cnt += 1

            dir = base_dir + name

            try:
                with open(dir, 'wb') as f:
                    f.write(download.content)  # Write the file locally.
                print(name + " downloaded successfully")
            except:
                print(name + " download failed, id: " + vid)