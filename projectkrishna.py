import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        root.title("Simple To-Do List")

        # Listbox to show tasks
        self.listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)

        # Entry to type new tasks
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=5)
        self.entry.bind('<Return>', lambda event: self.add_task())

        # Buttons frame
        frame = tk.Frame(root)
        frame.pack(pady=5)

        self.add_btn = tk.Button(frame, text="Add Task", width=15, command=self.add_task)
        self.add_btn.grid(row=0, column=0, padx=5)

        self.delete_btn = tk.Button(frame, text="Delete Task", width=15, command=self.delete_task)
        self.delete_btn.grid(row=0, column=1, padx=5)

        self.complete_btn = tk.Button(frame, text="Toggle Complete", width=15, command=self.toggle_complete)
        self.complete_btn.grid(row=0, column=2, padx=5)

        self.edit_btn = tk.Button(frame, text="Edit Task", width=15, command=self.edit_task)
        self.edit_btn.grid(row=0, column=3, padx=5)

    def add_task(self):
        task = self.entry.get().strip()
        if task == "":
            messagebox.showwarning("Warning", "Please enter a task")
            return
        self.listbox.insert(tk.END, task)
        self.entry.delete(0, tk.END)

    def delete_task(self):
        try:
            selected_idx = self.listbox.curselection()[0]
            self.listbox.delete(selected_idx)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete")

    def toggle_complete(self):
        try:
            selected_idx = self.listbox.curselection()[0]
            task = self.listbox.get(selected_idx)
            if task.startswith("✔️ "):
                # Unmark complete
                task = task[2:]
            else:
                # Mark complete
                task = "✔️ " + task
            self.listbox.delete(selected_idx)
            self.listbox.insert(selected_idx, task)
            self.listbox.select_set(selected_idx)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to toggle")

    def edit_task(self):
        try:
            selected_idx = self.listbox.curselection()[0]
            old_task = self.listbox.get(selected_idx)
            # Remove checkmark before editing if present
            if old_task.startswith("✔️ "):
                old_task = old_task[2:]
            new_task = simpledialog.askstring("Edit Task", "Modify task:", initialvalue=old_task)
            if new_task and new_task.strip():
                self.listbox.delete(selected_idx)
                self.listbox.insert(selected_idx, new_task.strip())
                self.listbox.select_set(selected_idx)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to edit")


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
