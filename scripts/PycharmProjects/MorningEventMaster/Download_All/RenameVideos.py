from atlassian import Confluence
import requests
from bs4 import BeautifulSoup
import os

base_url = "https://dwiki.daocloud.io"

confluence = Confluence(url=base_url, username="leqian.wu", password="IxahD+ier7booSi")  # Create a confluence session.

page_id = "55332751"  # The ID of "道客公开课"
login_data = {  # Your login details here
    "os_username": "leqian.wu",
    "os_password": "IxahD+ier7booSi"
}

ids = confluence.get_child_id_list(page_id)  # Get all the IDs of the available file pages.

sesn = requests.session()  # Create a session so that we don't need to login every time when downloading files.
# A crawler requires login at the beginning. Original cookies of login wouldn't be recognized.
resp = sesn.post(base_url, login_data)


def BreakFileName(string):  # Return format: file_name, file_suffix.
    for i in range(len(string) - 1, -1, -1):
        if string[i] == '.':
            return string[:i], string[i:]


cnt = 1  # Explained later.

base_path = "D:\\DaoCloud_vids\\"

files = os.listdir(base_path + "mp4\\")

tmp = open(base_path + "test.mp4", "rb")
binContent = tmp.read()
tmp.close()

for id in ids:
    vids = confluence.get_child_id_list(id)  # Get all the IDs of the available files in the file page.

    for vid in vids:
        url = base_url + "/pages/viewpage.action?pageId=" + vid  # Create the url for the file.
        resp = sesn.get(url)
        soup = BeautifulSoup(resp.content, "html.parser")
        ls = soup.find_all('a', class_='confluence-embedded-file')  # Locate the download link in the soup.
        meta_tag = soup.find('meta', attrs={'name': 'ajs-page-title'})
        real_name = meta_tag['content']

        for l in ls:
            name = l['aria-label']  # Get the file name
            src = l['data-file-src']  # Get the download link of file.

            video_url = base_url + src  # Concatenate the link with the base url.

            base_dir = "D:/DaoCloud_vids/"  # Prepare a folder to store all the files.

            filename, suffix = BreakFileName(name)
            if os.access(base_dir + name, os.F_OK):  # Prevents overlap of file names.
                filename += '_' + str(cnt)
                name = filename + suffix
                cnt += 1

            if name[-4:] == ".mp4":
                with open(base_dir + name, "wb") as f:
                    f.write(binContent)

            try:
                with open(base_path + "txt\\" + filename + ".txt", 'r') as f:
                     text = f.readline()

                with open(base_path + "txt_renamed\\" + real_name + ".txt", 'w') as g:
                     g.write(text)

                print(f"{filename}.txt renamed to {real_name}.txt")
            except:
                print(f"{filename}.txt not found")