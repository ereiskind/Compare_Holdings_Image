from pathlib import Path
import tkinter
from tkinter import ttk

# The functions below are hanging at root.destroy() functions, closing the windows created by the code but not the initial (root?) window; closing the latter window with the red 'x' prompts the program to move on
# The functions work when there's only print statements before and after, but not messageboxes; adding print statements between doesn't help
#ToDo: Figure out what's going on

def CreateJSONDisplay(JSON_text):
    """Creates a dialog box containing text that can be copied and a button for continuing on to the next part of the instructions."""
    root = tkinter.Tk()

    JSON_textbox = tkinter.Text(root)
    JSON_textbox.pack()
    JSON_textbox.insert("1.0", JSON_text)

    continue_button = ttk.Button(
        root,
        text="After copying the above and applying it to OpenRefine, click here to continue.",
        command=lambda: root.destroy(),
    )
    continue_button.pack()

    root.mainloop()


def RequestProjectNames(source):
    """Creates a dialog box to capture the name of the requested OpenRefine project."""
    def GetNameAndContinue():
        """Save the project name entered into the dialog box to a variable, close the dialog box, and continue on to the next part of the instructions."""
        global name
        name = project_name.get()
        root.destroy()
    
    root = tkinter.Tk()

    ttk.Label(
        root,
        text=f"What is the name of the {source} project?"
    ).pack()

    project_name = ttk.Entry(root)
    project_name.pack()

    continue_button = ttk.Button(
        root,
        text="After entering the name, click here to continue.",
        command=GetNameAndContinue,
    )
    continue_button.pack()
    
    root.mainloop()
    return name