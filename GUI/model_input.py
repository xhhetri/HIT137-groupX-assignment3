import tkinter as tk

class ModelInput:
    def __init__(self, parent):
        # Use a frame with border to hold the section
        self.title_label = tk.Label(parent, text="Model Input Section", font=("Arial", 14))
        self.frame = tk.Frame(parent, border=2, relief=tk.GROOVE, padx=10, pady=10)
        self.frame.pack(pady=10, padx=10)

        

        # Inner frame for label + dropdown + button on the same row
        input_row = tk.Frame(self.frame)
        input_row.pack(fill="x")

        # Model selection label
        tk.Label(input_row, text="Model Selection:", font=("Arial", 12)).pack(side="left", padx=(0,10))

        # Variable to store selected option
        self.selected_model = tk.StringVar(value="Text-to-image")

        # Dropdown menu
        options = ["Text-to-image", "Image Classification"]
        tk.OptionMenu(input_row, self.selected_model, *options).pack(side="left", padx=(0,10), fill="x", expand=True)

        # Run button
        tk.Button(input_row, text="Load Model", width=12, command=self.run_model).pack(side="left", fill="x")

    def run_model(self):
        print(f"Loading {self.selected_model.get()}...")
