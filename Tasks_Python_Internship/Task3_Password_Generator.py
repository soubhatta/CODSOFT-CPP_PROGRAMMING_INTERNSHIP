# CodSoft Internship
# Domain Name - Python Programming
# TASK - 3(Password Generator)
# Intern Name - Soumalya Bhattacharyya

import tkinter as tk
from tkinter import *
from random import randint

def new_rand():
    pass_entry.delete(0, END)
    pass_len = int(entry2.get())
    password = ''
    for x in range(pass_len):
        password += chr(randint(33, 126))
    pass_entry.insert(0, password)
    pass_entry.config(fg="green")  


def reset_password():
    pass_entry.delete(0, END)
    pass_entry.config(fg="black") 

title_font = ("Helvetica", 20)
title_color = "black"

root = Tk()
root.title("Password Generator")
root.geometry("500x400")


title_label = Label(root, text="Password Generator", font=title_font, fg=title_color)
title_label.pack(pady=20)

frame1 = Frame(root, width=50)
entry1 = Entry(frame1, width=30)
entry1.pack(side=RIGHT, pady=10, padx=20)
label = Label(frame1, text="Enter User Name:")
label.pack(side=RIGHT)
frame1.pack()

frame2 = Frame(root, width=50)
entry2 = Entry(frame2, width=30)
entry2.pack(side=RIGHT, pady=10, padx=20)
label = Label(frame2, text="Enter Password Length:")
label.pack(side=RIGHT)
frame2.pack()

frame3 = Frame(root, width=50)
pass_entry = Entry(frame3, width=30)
pass_entry.pack(side=RIGHT, pady=10, padx=20)
label = Label(frame3, text="Generated Password:")
label.pack(side=RIGHT)
frame3.pack()

button_generate = Button(root, text="Generate Password", command=new_rand, bg="white", fg="black")
button_generate.pack(pady=10)

frame_buttons = Frame(root)
frame_buttons.pack(pady=10)

button_accept = Button(frame_buttons, text="Accept", fg="black", bg="white", relief=RAISED, bd=3)
button_accept.pack(side=LEFT, padx=10)

button_reset = Button(frame_buttons, text="Reset", command=reset_password, fg="black", bg="white", relief=RAISED, bd=3)
button_reset.pack(side=LEFT, padx=10)

root.mainloop()

# Code by Soumalya Bhattacharyya
