import requests
import yaml

sesn = requests.session()
login_url = "https://fastgpt.daocloud.io/login"
f = open('secret.yaml', 'r', encoding='utf-8')
secret = yaml.load(f.read(), Loader=yaml.FullLoader)  # Load the config file
base = "D:\\DaoCloud\\AllDocs\\"  # The directory of folder DaoCloud-docs
wd = "Product Release\\"  # The directory of files to be uploaded
splitQuota = 600  # The number of tokens per group of data

login_data = {  # Post the login details on the login website
    "username": secret["username"],
    "password": secret["password"]
}

resp = sesn.post(login_url, login_data)  # Login first.


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
    file = "01.产品发布交付物-v20-20230726_163117.txt"
    cwd = base + wd + file

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

    for part in parts:
        cwd = cwd.replace(base, "")
        upload(part)