import tkinter as tk
import os
from style import fnt, ACTIVE_BG, BG, FG, ACCENT

class Option(tk.Checkbutton):
    def __init__(self, parent, filename):
        # Pull option content from file
        with open(filename, 'r') as f:
            self.content = f.readlines()
        
        # Grab description of option from first line in file
        title = self.content[0].replace('%', '').strip()
        
        self.state = tk.IntVar()
        super().__init__(parent, fg=FG, font=fnt(10), highlightbackground=BG,
                activebackground=ACTIVE_BG, activeforeground=FG,
                bg=BG, selectcolor=ACTIVE_BG, text=title, variable=self.state)

    def make(self):
        # If the option is selected, return content
        if self.state.get():
            return ''.join(self.content)

        return ''


class Selector(tk.Frame):
    def __init__(self, parent, folder):
        super().__init__(parent, bg=BG)

        title = tk.Label(self, font=fnt(10), text=f' Select {folder} ', fg=FG, bg=ACCENT)
        title.pack(anchor=tk.W)
        
        # Frame to hold Options
        option_frame = tk.Frame(self, bg=BG, borderwidth=2, relief=tk.RIDGE)
        option_frame.pack(fill=tk.X)
        
        # Get path to the folder this module resides in
        folder_path = os.path.join(os.path.dirname(__file__), folder)

        # Create all option checkbuttons, providing an absolute path to each file
        self.options = [Option(option_frame, os.path.join(folder_path, filename))
                for filename in os.listdir(folder_path)]       

        # Place all checkbuttons
        [option.pack(anchor=tk.W) for option in self.options]

    def make(self):
        # Get the result of this selector as a string
        return ''.join([option.make() for option in self.options])
            

