import tkinter as tk

class UserInputSection:
    def __init__(self, parent):
        # Frame to hold the section
        self.frame = tk.Frame(parent, border=2, relief=tk.GROOVE, padx=10, pady=10)

        # Section title
        self.title_label = tk.Label(self.frame, text="User Input Section", font=("Arial", 14))
        self.title_label.pack(anchor="w", pady=(0,10))

        # Inner frame for radio buttons + browse button
        input_row = tk.Frame(self.frame)
        input_row.pack(fill="x")

        # Radio buttons on the same row
        tk.Radiobutton(input_row, text="Text",  value="Text").pack(side="left", padx=(0,10))
        tk.Radiobutton(input_row, text="Image",  value="Image").pack(side="left", padx=(0,10))

        # Browse button next to radio buttons
        tk.Button(input_row, text="Browse", width=12, command=self.browse_file).pack(side="left", padx=(10,0))

    def browse_file(self):
        print(f"Selected: {self.selection.get()}")
