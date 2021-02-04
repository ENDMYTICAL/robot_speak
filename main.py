# -*- coding: utf-8 -*-
from communicate import recognition
from communicate import tuling
from communicate import compound
from communicate import speak
from communicate import chat
from osArduino import ReadArduio
import aiml
import os

myRobot = aiml.Kernel()

if os.path.isfile("./AIML/robot.brn"):
    myRobot.bootstrap(brainFile="./AIML/robot.brn")
else:
    myRobot.bootstrap(learnFiles="./AIML/robot.xml", commands="LOAD AIML B")
    myRobot.saveBrain("./AIML/robot.brn")

ChatRobot = aiml.Kernel()

if os.path.isfile("./AIML/chat.brn"):
    ChatRobot.bootstrap(brainFile="./AIML/chat.brn")
else:
    ChatRobot.bootstrap(learnFiles="./AIML/chat.xml", commands="LOAD AIML B")
    ChatRobot.saveBrain("./AIML/chat.brn")


def main():
    # 调用录音函数
    os.system('python3 vcad.py')

    # 调用语音识别函数
    message = recognition()
    print(message)
    # 检查自己的机器人是否有该指令
    robot_message = myRobot.respond(message)
    chat_message = ChatRobot.respond(message)
    if robot_message != '':
        print(robot_message)
        robot_message = robot_message.split('+')
        print(robot_message)
        robot_mes = robot_message[0]
        robot_order = robot_message[1]
        print(robot_order)
        compound(robot_mes)
        speak()
        if (robot_order == '000'):
            ReadArduio()
        if (robot_order == '111'):
            chat(message)
        if (robot_order == '222'):
            exit()
    elif chat_message != '':
        print(chat_message)
        compound(chat_message)
        speak()
    else:
        # 调用图灵机器人
        answer_message = tuling(message)

        # 调用语音合成
        compound(answer_message)

        # 调用播放器
        speak()



