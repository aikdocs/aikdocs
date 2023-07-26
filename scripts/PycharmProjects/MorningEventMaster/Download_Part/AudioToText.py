# -*- coding: UTF-8 -*-
import http.client
import json
import os
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import yaml

def getAccessToken(AccessId, AccessSecret):  # Generate the Access Token according to the Access ID and Access Secret.
    # 创建AcsClient实例
    client = AcsClient(
        AccessId,  # Your Access ID
        AccessSecret,  # Your Access Secret
        "cn-shanghai"
    );

    # 创建request，并设置参数。
    request = CommonRequest()
    request.set_method('POST')
    request.set_domain('nls-meta.cn-shanghai.aliyuncs.com')
    request.set_version('2019-02-28')
    request.set_action_name('CreateToken')

    try:
        response = client.do_action_with_exception(request)

        jss = json.loads(response)
        if 'Token' in jss and 'Id' in jss['Token']:
            token = jss['Token']['Id']
            return token

    except Exception as e:
        print(e)


def generateText(body):  # Concatenate the sentences recognized to form the whole text.
    sentences = body['flash_result']['sentences']
    text = ""
    for sentence in sentences:
        text += sentence['text']
    return text


def getFileName(string):  # Return format: file_name, file_suffix.
    for i in range(len(string)-1, -1, -1):
        if string[i] == '.':
            return string[:i]


def process(request, audioFile):  # Convert the file from audio to text.
    # 读取音频文件
    with open(audioFile, mode='rb') as f:
        audioContent = f.read()
    host = 'nls-gateway.cn-shanghai.aliyuncs.com'
    # 设置HTTP请求头部
    httpHeaders = {
        'Content-Length': len(audioContent)
    }
    # Python 2.x使用httplib
    # conn = httplib.HTTPConnection(host)

    # Python 3.x使用http.client
    conn = http.client.HTTPConnection(host)

    conn.request(method='POST', url=request, body=audioContent, headers=httpHeaders)
    response = conn.getresponse()
    # print('Response status and response reason:')
    # print(response.status, response.reason)
    body = response.read()
    try:
        # print('Recognize response is:')
        body = json.loads(body)
        # print(body)
        result = generateText(body)
        status = body['status']
        print(f"processing {audioFile}:", end=' ')
        if status == 20000000:
            print('Recognizer success!')
            return result
        else:
            print('Recognizer failed!')
    except ValueError:
        print('The response is not json format string')
    conn.close()


if __name__ == "__main__":
    f = open('config.yaml', 'r', encoding='utf-8')
    secrets = yaml.load(f.read(), Loader=yaml.FullLoader)

    appKey = secrets["AudioToText"]["appKey"]  # Your app key.
    AccessId = secrets["AudioToText"]["accessId"]  # Your access ID.
    AccessSecret = secrets["AudioToText"]["accessSecret"]  # Your access secret
    # 服务请求地址
    url = 'https://nls-gateway.cn-shanghai.aliyuncs.com/stream/v1/FlashRecognizer'

    base_path = secrets["AudioToText"]["basepath"]

    # 设置RESTful请求参数
    format = 'mp3'  # The file format.
    sampleRate = 16000  # The sample rate of the file.
    enablePunctuationPrediction = True
    enableInverseTextNormalization = True
    enableVoiceDetection = False

    files = os.listdir(base_path+"mp3\\")  # Load all the mp3 files.

    for file in files:
        audio_dir = base_path + "mp3\\" + file
        token = getAccessToken(AccessId, AccessSecret)
        print(token)
        request = url + '?appkey=' + appKey
        request = request + '&token=' + token
        request = request + '&format=' + format
        request = request + '&sample_rate=' + str(sampleRate)
        print('Request: ' + request)  # Form the request URL.

        try:
            ans = process(request, audio_dir)
            text_dir = base_path + "txt\\" + getFileName(file) + ".txt"
            with open(text_dir, 'w') as f:  # Store the recognized result.
                f.write(ans)
        except:
            print(f"{file} unsuccessful.")