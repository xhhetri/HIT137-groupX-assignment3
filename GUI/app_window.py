import tkinter as tk
from menubar import MenuBar
from model_input import ModelInput
from user_input_section import UserInputSection

class AppWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tkinter AI GUI")
        self.root.geometry("500x150")  # slightly taller to fit content

        # Attach the menu bar
        self.menu = MenuBar(self.root)

        # Add the ModelInput section
        self.model_input = ModelInput(self.root)
        self.model_input.frame.grid(row=1)
        
        #Add the UserInputSection
        self.user_input = UserInputSection(self.root)
        self.user_input.frame.grid(row=2)
        
        
    def main_loop(self):
        self.root.mainloop()



if __name__ == "__main__":
    app = AppWindow()
    app.main_loop()