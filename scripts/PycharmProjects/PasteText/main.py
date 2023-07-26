import yaml
from apitable import Apitable

f = open('secret.yaml', 'r', encoding='utf-8')
secrets = yaml.load(f.read(), Loader=yaml.FullLoader)

apitable = Apitable(secrets["apikey"])
datasheet = apitable.datasheet(secrets["datasheet"], field_key="name")

all_records = datasheet.records.all()

for record in all_records:
    print(record.json())