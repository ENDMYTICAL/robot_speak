from communicate import compound
from communicate import speak
import os

def ReadArduio():
    input = open('./infomation/data.txt', 'r')
    astring = input.read()
    print(astring)
    input.close()
    # 播报环境情况
    compound(astring)
    speak()

