#!/usr/bin/python
import tkinter as tk
from widgets import Selector
from tkinter import filedialog
from style import ACCENT, FG, BG, fnt
import os
import sys 

# Filename from commandline
ARGFILENAME = sys.argv[1] if 1 < len(sys.argv) else ""
# Snippet directories
SNIPPET_DIRS = ("Classes", "Packages", "Options", "Samples")
# Template file
TEMPLATE = os.path.join(os.path.dirname(__file__), "template.tex")

class TexInit(tk.Tk):
    def __init__(self):
        super().__init__()

        self.config(bg=BG)
        
        title = tk.Label(self, text=' TexInit by JeJ ', font=fnt(20), bg=ACCENT, fg=FG)
        title.pack(anchor=tk.W, pady=(0, 10))
        
        # Create and display a selector for each specified directory
        self.selectors = {cls: Selector(self, cls) for cls in SNIPPET_DIRS}
        [selector.pack(fill=tk.X, pady=(0, 10)) for selector in self.selectors.values()]
        
        tk.Button(self, text=f"Create {ARGFILENAME}",
                activeforeground=FG, fg=FG,
                activebackground=ACCENT, bg=ACCENT,
                font=fnt(10), command=self.make).pack(anchor=tk.W)

    def make(self):
        # Grab filename from command line arguments
        output = ARGFILENAME
         
        if not output:
            # Grab filename from dialog
            output = filedialog.asksaveasfilename(title="Output File",
                    filetypes=(("LaTeX File", "*.tex"),))

        # Cancel if we can't get either
        if not output:
            return
    
        template = ""
        # Pull template from file
        with open(TEMPLATE, "r") as f:
            template = f.read()
            
        # Substitute in snippets
        for directory in SNIPPET_DIRS:
            template = template.replace("{{"+directory+"}}",
                    self.selectors[directory].make())

        # Write to document
        with open(output, 'w') as f:
            f.write(template)

        self.destroy()

if __name__ == '__main__':
    TexInit().mainloop()
