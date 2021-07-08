from pathlib import Path
import tkinter
from tkinter import ttk

def CreateJSONDisplay(JSON_file):
    """Creates a dialog box with a JSON that can be copied and a button for continuing on to the next part of the instructions."""
    root = tkinter.Tk()
    JSON_file_path = Path('.', 'JSONs', JSON_file)

    JSON_text = tkinter.Text(root)
    JSON_text.pack()
    with open(JSON_file_path) as JSON_IO:
        JSON_text.insert("1.0", JSON_IO.read())

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

    project_name = tkinter.Entry(root)
    project_name.pack()

    continue_button = ttk.Button(
        root,
        text="After entering the name, click here to continue.",
        command=GetNameAndContinue,
    )
    continue_button.pack()
    
    root.mainloop()
    return name