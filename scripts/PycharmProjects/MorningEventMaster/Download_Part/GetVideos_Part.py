from atlassian import Confluence
import requests
from bs4 import BeautifulSoup
import yaml

base_url = "https://dwiki.daocloud.io"

f = open('config.yaml', 'r', encoding='utf-8')
secrets = yaml.load(f.read(), Loader=yaml.FullLoader)
username = secrets["GetVideos"]["username"]
password = secrets["GetVideos"]["password"]

# Create a confluence session.
confluence = Confluence(url=base_url, username=username, password=password)

page_id = "55332751"  # The ID of "道客公开课"
login_data = {  # Your login details here
    "os_username": username,
    "os_password": password
}

ids = confluence.get_child_id_list(page_id)  # Get all the IDs of the available file pages.

sesn = requests.session()  # Create a session so that we don't need to login every time when downloading files.
# A crawler requires login at the beginning. Original cookies of login wouldn't be recognized.
resp = sesn.post(base_url, login_data)

base_dir = secrets["GetVideos"]["basedir"]  # The directory which contains the csv file of download.

full_dir = base_dir + "\\urls.csv"
f = open(full_dir, 'r')
files = f.readlines()
f.close()

for a_url in files:
    url = a_url.strip()
    try:
        reqs = sesn.get(url)
        soup = BeautifulSoup(reqs.content, "html.parser")
        ls = soup.find_all('a', class_='confluence-embedded-file')  # Locate the download link in the soup.
        meta_tag = soup.find('meta', attrs={'name': 'ajs-page-title'})
        name = meta_tag['content']

        for l in ls:
            serverside_name = l['aria-label']
            src = l['data-file-src']  # Get the download link of file.
            video_url = base_url + src  # Concatenate the link with the base url.

            if ".mp4" in serverside_name:
                download = sesn.get(video_url)  # Download session of the file.

                with open(base_dir + name + ".mp4", "wb") as f:
                    f.write(download.content)

                print(f"{name}.mp4 downloaded successfully.")
    except:
        print("Invalid url.")