def add_task():
    task = task_entry.get().strip()
    if task == "":
        return
    task_entry.delete(0, tk.END)
    task_number = task_list.size() + 1
    task_list.insert( tk.END, f"{task_number}. {task}")
    task_entry.delete(0, tk.END)

import tkinter as tk

window = tk.Tk()
window.configure(bg="peach puff")

window.title("To-Do List")
window.geometry("400x600")

label = tk.Label(window, text="My To-Do List", bg="#FFDAB9")

label.pack()

title = tk.Label(window,
                 text="Welcome to To-Do List program", bg="#FFB07C",
                 font=("Arial",18))
title.pack(pady=10)

task_entry = tk.Entry(window, width=30, font=("Arial", 14))
task_entry.pack(pady=5)

button = tk.Button(window, text="Add Task", command=add_task, bg="#F08080")
button.pack(pady=10)

task_list = tk.Listbox(window, width=40, height=25)
task_list.pack(pady=5)

def delete_task():
    selected = task_list.curselection()
    if selected:
        task_list.delete(selected)
        tasks=task_list.get(0, tk.END)
        task_list.delete(0, tk.END)

        for i, task in enumerate(tasks, start=1):
            task_list.insert(tk.END, f"{i}. {task.split('. ',1)[1]}")

button2 = tk.Button(window, text="Delete", command=delete_task, bg="#F08080")
button2.pack()

window.mainloop()
