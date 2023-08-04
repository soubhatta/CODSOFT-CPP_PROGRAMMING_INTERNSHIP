# CodSoft Internship
# Domain Name - Python Programming
# Task - 2(To Do List)
# Intern Name - Soumalya Bhattacharyya

import tkinter as tk
from tkinter import messagebox


# importing Tk library for creating GUI
def add_task():
    """ Adding Task in the list box"""
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


def delete_task():
    """ Deleting Task From the list box"""
    try:
        selected_index = listbox.curselection()
        listbox.delete(selected_index)

    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")


def clear_tasks():
    """ Clearing All Task From the list box"""
    listbox.delete(0, tk.END)


# Creating the main window
window = tk.Tk()
window.title("To-Do List")

# Creating the listbox
listbox = tk.Listbox(window, width=50)
listbox.pack(pady=10)

# Creating the entry field
entry = tk.Entry(window, font=("Helvetica", 14))
entry.pack(pady=5)

# Creating the buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# Add Button to perform Adding task
add_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=0)

# Delete button to perform Delete
delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=1)

# Clear Button to clear all
clear_button = tk.Button(button_frame, text="Clear Task", command=clear_tasks)
clear_button.grid(row=0, column=2)

# Starting the GUI
window.mainloop()

# Code by Soumalya Bhattacharyya
