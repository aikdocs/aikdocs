import requests
from bs4 import BeautifulSoup
import yaml
from atlassian import Confluence
import json
import urllib.request

base_url = "https://fastgpt.daocloud.io/"
f = open('secret.yaml', 'r', encoding='utf-8')
login_details = yaml.load(f.read(), Loader=yaml.FullLoader)

confluence = Confluence(url=base_url, username=login_details["username"], password=login_details["password"])

sesn = requests.session()

login_data = {  # Your login details here
    "username": login_details["username"],
    "password": login_details["password"]
}

resp = sesn.post(base_url+"login", login_data)

url = "https://fastgpt.daocloud.io/kb?kbId=64869c48f25dba3b7c7d45a0"

