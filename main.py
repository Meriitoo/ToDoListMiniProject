import tkinter as tk
from tkinter import ttk

todo_list = []


def add_task():
    task = task_entry.get()
    if task:
        todo_list.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)


def remove_task():
    selected_task = task_listbox.get(tk.ACTIVE)
    if selected_task:
        todo_list.remove(selected_task)
        update_task_list()


def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in todo_list:
        task_listbox.insert(tk.END, task)


root = tk.Tk()
root.title("To-Do List App")

style = ttk.Style()
style.configure("TButton", padding=10, relief="flat", foreground="black")

style.configure("AddTask.TButton", background="green", font=("Times New Roman", 12, "bold"))
style.configure("RemoveTask.TButton", background="red", font=("Times New Roman", 12, "bold"))

task_label = ttk.Label(root, text="Task:", font=("Times New Roman", 20,))
task_label.pack(pady=5)

task_entry = ttk.Entry(root, width=40)
task_entry.pack(pady=5)

add_button = ttk.Button(root, text="Add Task", style="AddTask.TButton", command=add_task)
add_button.pack(pady=5)

remove_button = ttk.Button(root, text="Remove Task", style="RemoveTask.TButton", command=remove_task)
remove_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=40, height=10, font=("Helvetica", 12))
task_listbox.pack(pady=10)

root.mainloop()
