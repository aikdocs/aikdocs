import os
import yaml

f = open('config.yaml', 'r', encoding='utf-8')
secrets = yaml.load(f.read(), Loader=yaml.FullLoader)
base_dir = secrets["ChangeEncoding"]["basedir"]

files = os.listdir(base_dir + "txt_final")

for file in files:
    text = []
    with open(base_dir + "txt_final\\" + file, 'rb') as f:
        text = f.readlines()
    with open(base_dir + "txt_final_utf_8\\" + file, 'w', encoding='utf-8') as f:
        for i in text:
            try:
                line = i.decode('gb2312')
                f.write(line)
            except:
                pass
