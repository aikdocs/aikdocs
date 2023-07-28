import requests
import yaml
import os

sesn = requests.session()
login_url = "https://fastgpt.daocloud.io/login"
f = open('secret.yaml', 'r', encoding='utf-8')
secret = yaml.load(f.read(), Loader=yaml.FullLoader)  # Load the config file
base = "D:\\kubernetes-website-main\\website-main\\"  # The directory of folder DaoCloud-docs
wd = "content\\en"  # The directory of files to be uploaded
splitQuota = 600  # The number of tokens per group of data

login_data = {  # Post the login details on the login website
    "username": secret["username"],
    "password": secret["password"]
}

resp = sesn.post(login_url, login_data)  # Login first.


def shorten(wdir):
    cnt = 0
    for i in range(len(wdir)-1, -1, -1):
        if wdir[i] == '\\':
            cnt += 1
        if cnt == 2:
            return wdir[i:]


def segment(text):  # Divide the text into sub-texts of {splitQuota} tokens.
    global base

    parts = []
    cnt = 1

    prev_index = 0
    index = -1
    flag = True

    while flag:  # Split the file into sub-files of the previously mentioned size.
        try:
            prev_index = index + 1
            for i in range(cnt * splitQuota, cnt * splitQuota + 200):
                if text[i] == '。':
                    index = i
                    break
        except:
            index = len(text) - 1
            flag = False

        parts.append(text[prev_index:index + 1])

        cnt += 1

    return parts


def getsuffix(filename):  # Get the file suffix.
    for i in range(len(filename) - 1, -1, -1):
        if filename[i] == ".":
            return filename[i + 1:]


def upload(text, dir):  # Upload the text to the website.
    url = "https://fastgpt.daocloud.io/api/openapi/kb/pushData"

    payload = {
        "kbId": secret["kbId"],
        "mode": "index",
        "prompt": "",
        "data": [
            {
                "q": text,
                "source": dir
            }
        ]
    }

    print(payload["data"][0]["source"])
    headers = {
        "apikey": secret["apikey"],
        "Content-Type": "application/json"
    }

    response = sesn.post(url, headers=headers, json=payload)

    print(response.text)


if __name__ == "__main__":
    for root, dirs, files in os.walk(base + wd):  # Loop through all the files in the directory.
        for file in files:
            if getsuffix(file) == "md":  # We only care about .md files
                cwd = root + '\\' + file

                lines = []
                with open(cwd, 'rb') as f:
                    bintext = f.readlines()

                for i in bintext:
                    try:  # Ignore the characters that cannot be decoded
                        lines.append(i.decode('utf-8'))
                    except:
                        pass

                text = "".join(lines)
                parts = segment(text)

                for part in parts:
                    cwd = cwd.replace(base, "")
                    upload(part, cwd)