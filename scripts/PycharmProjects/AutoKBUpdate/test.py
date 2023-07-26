import requests
import yaml
import os

sesn = requests.session()
login_url = "https://fastgpt.daocloud.io/login"
f = open('secret.yaml', 'r', encoding='utf-8')
secret = yaml.load(f.read(), Loader=yaml.FullLoader)  # Load the config file
base = secret["dir"]  # The directory of folder DaoCloud-docs
wd = "DaoCloud-docs\\docs\\zh\\docs"  # The directory of files to be uploaded
splitQuota = 2500  # The number of tokens per group of data

login_data = {  # Post the login details on the login website
    "username": secret["username"],
    "password": secret["password"]
}

resp = sesn.post(login_url, login_data)  # Login first.


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

upload("123123", 'a'*100)