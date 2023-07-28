import requests
import yaml
import os

sesn = requests.session()
login_url = "https://fastgpt.daocloud.io/login"
f = open('secret.yaml', 'r', encoding='utf-8')
secret = yaml.load(f.read(), Loader=yaml.FullLoader)  # Load the config file
base = "D:\\DaoCloud\\AllDocs\\DCE 4.0\\"  # The directory of folder DaoCloud-docs

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
            for i in range(cnt * splitQuota, cnt * splitQuota + 1000):
                if text[i] == '。' or i == cnt * splitQuota + 199:
                    index = i
                    break
        except:
            index = len(text) - 1
            flag = False

        parts.append(text[prev_index:index + 1])

        cnt += 1

    return parts


def upload(text):  # Upload the text to the website.
    url = "https://fastgpt.daocloud.io/api/openapi/kb/pushData"

    payload = {
        "kbId": secret["kbId"],
        "mode": "index",
        "prompt": "",
        "data": [
            {
                "q": text,
            }
        ]
    }

    headers = {
        "apikey": secret["apikey"],
        "Content-Type": "application/json"
    }

    response = sesn.post(url, headers=headers, json=payload)

    print(response.text)


if __name__ == "__main__":
    cwd = base + "DCE 4.0 产品文档-v2-20230726_140141.txt"

    lines = []
    with open(cwd, 'rb') as f:
        bintext = f.readlines()

    for i in bintext:
        try:  # Ignore the characters that cannot be decoded
            lines.append(i.decode('gb2312'))
        except:
            pass

    text = "".join(lines)
    parts = segment(text)
    print(len(parts))
    for part in parts:
        upload(part)