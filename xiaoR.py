# -*- coding: utf-8 -*-
import sys

sys.path.append('./snowboy')

import snowboydecoder
import signal
from main import main

interrupted = False


def signal_handler():
    global interrupted
    if (interrupted == True):
        interrupted = False
    else:
        interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted


def wake_up():
    model = "snowboy/小R.pmdl"

    # capture SIGINT signal, e.g., Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
    print('Listening... Press Ctrl+C to exit')

    # main loop
    detector.start(detected_callback=signal_handler,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)

    detector.terminate()


while True:
    print("----------------------------xiaoR机器人-----------------------------------")
    print("----------------------------－－－－－-----------------------------------")
    print("----------------------------－－－－－-----------------------------------")
    print("----------------------------－－－－－-----------------------------------")
    print("----------------------------－－－－－-----------------------------------")
    wake_up()
    snowboydecoder.play_audio_file()
    main()
    signal_handler()




