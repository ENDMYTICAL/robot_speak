# -*- coding: utf-8 -*-

import aiml
import os

myRobot = aiml.Kernel()

if os.path.isfile("robot.brn"):
    myRobot.bootstrap(brainFile="robot.brn")
else:
    myRobot.bootstrap(learnFiles = "robot.xml", commands="LOAD AIML B")
    myRobot.saveBrain("robot.brn")
'''	
ChatRobot = aiml.Kernel()

if os.path.isfile("chat.brn"):
    ChatRobot.bootstrap(brainFile="chat.brn")
else:
    ChatRobot.bootstrap(learnFiles = "chat.xml", commands="LOAD AIML B")
    ChatRobot.saveBrain("chat.brn")
'''
# kernel()已经等待使用了
while True:
	print(myRobot.respond(input("Enter your message >> ")))
   # print(ChatRobot.respond(input("Enter your message >> ")))
