import tkinter as tk

class MenuBar:
    def __init__(self, root):
        self.menubar = tk.Menu(root)

        # File menu
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.file_menu)

        # Models menu
        self.models_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Models", menu=self.models_menu)

        # Help menu
        self.help_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=self.help_menu)

        # Attach menubar to root window
        root.config(menu=self.menubar)
