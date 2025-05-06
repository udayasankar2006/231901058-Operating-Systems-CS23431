# main.py
import tkinter as tk
from tkinter import ttk
from process_monitor import get_processes
from process_graph import ProcessGraph
from styles import set_dark_theme

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Task Manager")
        self.root.geometry("1000x600")
        set_dark_theme(self.root)

        self.tree = ttk.Treeview(root, columns=("PID", "Name", "RAM (MB)", "RAM %"), show="headings")
        self.tree.heading("PID", text="PID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("RAM (MB)", text="RAM (MB)")
        self.tree.heading("RAM %", text="RAM %")
        self.tree.column("Name", width=250)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)
        self.tree.bind("<Double-1>", self.show_graph)

        self.graph_window = None
        self.update_process_list()

    def update_process_list(self):
        self.tree.delete(*self.tree.get_children())
        for proc in get_processes():
            self.tree.insert("", "end", values=proc)
        self.root.after(1000, self.update_process_list)

    def show_graph(self, event):
        selected = self.tree.focus()
        if not selected:
            return
        pid = int(self.tree.item(selected)["values"][0])
        name = self.tree.item(selected)["values"][1]
        if self.graph_window:
            self.graph_window.destroy()
        self.graph_window = tk.Toplevel(self.root)
        self.graph_window.title(f"RAM Usage - {name} (PID {pid})")
        ProcessGraph(self.graph_window, pid, name)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
