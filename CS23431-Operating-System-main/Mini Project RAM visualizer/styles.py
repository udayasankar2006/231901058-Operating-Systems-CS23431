# styles.py
from tkinter import ttk

def set_dark_theme(root):
    style = ttk.Style(root)
    style.theme_use("default")

    # General background
    root.configure(bg="#1e1e1e")

    # Treeview styling
    style.configure("Treeview",
                    background="#2e2e2e",
                    foreground="white",
                    fieldbackground="#2e2e2e",
                    rowheight=25,
                    bordercolor="#444444",
                    borderwidth=0)

    style.configure("Treeview.Heading",
                    background="#1e1e1e",
                    foreground="white",
                    font=("Segoe UI", 10, "bold"))

    style.map("Treeview",
              background=[("selected", "#3a3a3a")],
              foreground=[("selected", "white")])

    # Scrollbar styling (optional)
    style.configure("Vertical.TScrollbar",
                    gripcount=0,
                    background="#444444",
                    darkcolor="#3a3a3a",
                    lightcolor="#3a3a3a",
                    troughcolor="#2e2e2e",
                    bordercolor="#2e2e2e",
                    arrowcolor="white")

    style.configure("Horizontal.TScrollbar",
                    gripcount=0,
                    background="#444444",
                    darkcolor="#3a3a3a",
                    lightcolor="#3a3a3a",
                    troughcolor="#2e2e2e",
                    bordercolor="#2e2e2e",
                    arrowcolor="white")
