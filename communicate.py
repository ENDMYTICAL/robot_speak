# -*- coding: utf-8 -*-
from aip import AipSpeech
import requests
import os
import time
import random
#百度API
APP_ID = '#'
API_KEY = '#'
SECRET_KEY = '#'
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# 图灵API
TULING_KEY = '#'

filename = "output.mp3"

# 读取本地文件
def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()

#语音识别
def recognition():

    res = aipSpeech.asr(get_file_content('input.wav'), 'wav', 16000, {'dev_pid': 1537}, )
    #百度API返回的数据
    print(res)
    # 转化成string,如果没有则返回error
    text = res['result'][0][:-1]
    return text

#图灵机器人的回答
def tuling(message):
    url = 'http://www.tuling123.com/openapi/api?key=' + TULING_KEY + '&infomation=' + message
    '''
    res = requests.get(url)
    res.encoding = 'utf-8'
    answer_message = json.loads(res.text)
    '''
    text = requests.post(url).json()
    return text['text']
def chat(message):
    compound("开始唠嗑把!")
    speak()
    message={1:'你好,主人?',2:'有啥子问题哦,主银?',3:'啊,你怎么又来打扰我了.'}
    a=random.randint(1,3)
    compound(message[a])
    speak()
    while True:
        os.system('python3 vcad.py')
        message = recognition()
        answer_message = tuling(message)
        compound(answer_message)
        speak()
        if message=='不聊了':
            break;
        if message=='再见':
            break;
        if message=='再见,':
            break;
#语音合成
def compound(text):

        result = aipSpeech.synthesis(text, 'zh', 1, {
            'vol': 5,
            'per': 4
        })

        if not isinstance(result, dict):
            with open(filename, 'wb') as f:
                f.write(result)
        print("---------------------------")
        time.sleep(1)

#语音播放器
def speak():
    os.system('mpg321 output.mp3')


#删除语音文件
def dell():
    os.remove(filename)
