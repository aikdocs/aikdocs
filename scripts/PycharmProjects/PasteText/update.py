import requests
import yaml
from bs4 import BeautifulSoup

f = open('secret.yaml', 'r', encoding='utf-8')
secrets = yaml.load(f.read(), Loader=yaml.FullLoader)
view_id = secrets["viewId"]
field_key = "name"
apikey = secrets["apikey"]
datasheet = secrets["datasheet"]
sesn = requests.session()


def getWebpage():
    global view_id
    global field_key
    global apikey
    global datasheet

    url = f"https://apitable.daocloud.io/fusion/v1/datasheets/{datasheet}/records"

    get_headers = {
        "Authorization": f"Bearer {apikey}"
    }

    response = sesn.get(url, headers=get_headers, params={"viewId": view_id, "fieldKey": field_key})
    response = response.json()
    records = response["data"]["records"]
    return records


def getLink(link):
    text = ""
    response = sesn.get(link)
    soup = BeautifulSoup(response.content, "html.parser")
    span_elements = soup.find_all("span")

    for span_element in span_elements:
        part_text = span_element.get_text(strip=True)
        text += part_text

    return text


def updateRecord(record):
    global view_id
    global field_key
    global apikey
    global datasheet

    try:
        url = f"https://apitable.daocloud.io/fusion/v1/datasheets/{datasheet}/records?viewId={view_id}&fieldKey={field_key}"
        recordId = record["recordId"]
        passage_link = record["fields"]["内容url"]
        text = getLink(passage_link)
        record["fields"]["内容"] = text

        headers = {
            "Authorization": f"Bearer {apikey}",
            "Content-Type": "application/json"
        }

        data = {
            "records": [
                {
                    "recordId": recordId,
                    "fields": record["fields"]
                }
            ],
            "fieldKey": field_key
        }

        response = sesn.patch(url, headers=headers, json=data)
        print(response.json())
    except:
        pass


if __name__ == "__main__":
    records = getWebpage()
    for record in records:
        Id = record["recordId"]
        try:
            text = record["fields"]["内容"]
            print(f"Content of {Id} already present!")
        except:
            try:
                url = record["fields"]["内容url"]
                updateRecord(record)
            except:
                print(f"No url to update for {Id}!")