#!/usr/bin/python
import tkinter as tk
from widgets import Selector
from tkinter import filedialog
from style import ACCENT, FG, BG, fnt
import sys

# Filename from commandline
ARGFILENAME = sys.argv[1] if 1 < len(sys.argv) else ""
# Sample directories
SAMPLE_DIRS = ("Classes", "Packages", "Samples")

class TexInit(tk.Tk):
    def __init__(self):
        super().__init__()

        self.config(bg=BG)
        
        title = tk.Label(self, text=' TexInit by JeJ ', font=fnt(20), bg=ACCENT, fg=FG)
        title.pack(anchor=tk.W, pady=(0, 10))
        
        # Create and display a selector for each specified directory
        self.selectors = {cls: Selector(self, cls) for cls in SAMPLE_DIRS}
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

        classes = self.selectors["Classes"].make()
        packages = self.selectors["Packages"].make()
        samples = self.selectors["Samples"].make()
        
        document = ''.join([classes, '\n', packages, '\n\\begin{document}\n',
                            samples, '\n\\end{document}\n'])

        with open(output, 'w') as f:
            f.write(document)

        self.destroy()

if __name__ == '__main__':
    TexInit().mainloop()
