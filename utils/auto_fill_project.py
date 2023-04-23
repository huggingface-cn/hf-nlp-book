import pandas as pd
import keyboard
import time
keyboard.press_and_release("down")
time.sleep(5)
data=pd.read_csv('translate_course\summery.csv')
# for passage in data['words_num']:#title words_num
#     keyboard.write(str(passage))
#     time.sleep(0.2)
#     keyboard.press_and_release("enter")
#     time.sleep(0.5)
# average=sum(data['words_num'])/len(data['words_num'])
# for passage in data['words_num']:
#     keyboard.press_and_release("enter")
#     num=int(passage/(average*2)*5)
#     if num>4:
#         num=4
#     num=4-num
#     for i in range(num):
#         keyboard.press_and_release("down")
#         time.sleep(0.2)
#     keyboard.press_and_release("enter")
#     time.sleep(0.5)
for passage in data['title']:#title words_num
    keyboard.write(str(passage).split(" ")[0].split('/')[0])
    time.sleep(0.2)
    keyboard.press_and_release("enter")
    time.sleep(0.5)







