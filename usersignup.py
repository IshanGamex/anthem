import random
from pynput.mouse import Button as MouseButton, Controller
m = Controller()

from pynput.keyboard import Key, Controller as KeyboardController
k = KeyboardController()

import time as t

import pandas as pd
'''
pip install pynput
pip install pandas
pip install time
pip install random
'''


print("After the code starts, any movement of you mouse will stop the code as this is an infinite loop.")

df = pd.read_csv('your_file.csv')

t.sleep(5)
row_index = 1  


def tab():
    k.press(Key.tab)
    t.sleep(0.01)
    k.release(Key.tab)
    t.sleep(0.01)

for i in range():

    FName = df.loc[row_index, "A"]
    LName = df.loc[row_index, "B"]
    email = df.loc[row_index, "C"]
    title = df.loc[row_index, "E"]
    sso = df.loc[row_index, "F"]
    row_index+=1
    for i in range(8):
        tab()
        t.sleep(0.05)
    k.press(Key.enter)
    k.release(Key.enter)
    for i in range(3):
        tab()
        t.sleep(0.05)
    k.type(FName)
    tab()
    k.type(LName)
    tab()
    k.type(email)
    tab()
    k.type(title)
    tab()
    k.type(sso)
    for i in range(3):
        tab()
    k.press(Key.enter)
    k.release(Key.enter)
    t.sleep(2)
