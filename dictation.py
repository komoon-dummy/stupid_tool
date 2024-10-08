import time

import pyttsx3

CNT = 5

if __name__ == '__main__':
    # 初始化TTS引擎
    engine = pyttsx3.init()

    # 设置要报听写的文本
    with open('dictation.txt', 'r', encoding='utf-8') as f:
        texts = f.readlines()

    # 设置语速，可选，可以根据需要调整
    # 值越小语速越慢，值越大语速越快
    engine.setProperty('rate', 100)

    # 将文本添加到TTS引擎
    for text in texts:
        for i in range(CNT):
            engine.say(text)
            engine.runAndWait()
            time.sleep(2)
