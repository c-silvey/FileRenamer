from tkinter import *
from tkinter import filedialog
import os

# ---------
# define button commands
# ---------

# select source folder


def select_folder():
    global sourcePath
    sourcePath = filedialog.askdirectory(initialdir="S://")
    inputPath.insert(0, sourcePath)

# Run program


def renamer():
    global sourcePath
    old_str = oldEntry.get()
    new_str = newEntry.get()
    for f in os.listdir(sourcePath):
        if old_str.lower() in f.lower():
            os.rename(
                os.path.join(
                    sourcePath, f), os.path.join(
                    sourcePath, f.lower().replace(
                        old_str.lower(), new_str)))

    root.destroy()

# ---------
# GUI Stuff
# ---------


# initialize root
root = Tk()

# create folder path label
inputLabel = Label(root, text='Select photo folder:')
inputLabel.grid(row=0, column=0, padx=10, sticky=W)

# create text entry box for photo folder path
inputPath = Entry(root, width=105)
inputPath.grid(row=1, column=0, padx=10, pady=20, columnspan=2, sticky=W)

# create button to select source path
selectButton_1 = Button(root, text="Select", width=10, command=select_folder)
selectButton_1.grid(row=1, column=2, padx=10)

# create old string label
oldLabel = Label(root, text='Old String:')
oldLabel.grid(row=3, column=0, padx=10, sticky=W)

# create old string entry box
oldEntry = Entry(root, width=50)
oldEntry.grid(row=4, column=0, padx=10, pady=20, columnspan=1, sticky=W)

# create new string label
newLabel = Label(root, text='New String:')
newLabel.grid(row=3, column=1, padx=10, sticky=W)

# create new string entry box
newEntry = Entry(root, width=50)
newEntry.grid(row=4, column=1, padx=10, pady=20, columnspan=1, sticky=W)

# create button to rename files
saveButton = Button(root, text="Rename", width=10, command=renamer)
saveButton.grid(row=4, column=2, padx=10, pady=10)

# run mainloop
root.mainloop()
