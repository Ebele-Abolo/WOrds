# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 08:47:28 2021

@author: joyab
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 07:53:14 2021

@author: joyab
"""

from tkinter import *
import random
root=Tk()

root.title("Wacky Word Wheel")
root.geometry("500x500")

list1 = ["Water","Wyoming","Wheel","Winter","Wendsday","Whoop","Why","What","When","Who","We","Witch","Which","Whim","Want","Wanna","we're","we'd"]
print(list1)

def random_number():
    random_no = random.randint(0,17)
    print(random_no)
    random_lucky_friend = list1[random_no]
    print("Your Wacky Word is: " + random_lucky_friend)

btn1 = Button(root)
btn1 = Button(root, text = "What's your wacky word? ", command = random_number )
btn1.place(relx= 0.5, rely= 0.5, anchor = CENTER)

root.mainloop()

    