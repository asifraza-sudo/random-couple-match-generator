import tkinter as tk
from tkinter import messagebox
import random


def myGenerateCouples():
    myNames = myEntry.get("1.0", tk.END).strip().split('\n')
    random.shuffle(myNames)
    myCouples = [f"{myNames[i]} & {myNames[i + 1]}" for i in range(0, len(myNames) - 1, 2)]
    if len(myNames) % 2 != 0:
        myCouples.append(f"{myNames[-1]} is alone")
    myCouplesText.set("\n".join(myCouples))


myRoot = tk.Tk()
myRoot.title("Random Couple Match Generator")


myEntryLabel = tk.Label(myRoot, text="Enter names (one per line):")
myEntryLabel.pack()

myEntry = tk.Text(myRoot, height=10, width=30)
myEntry.pack()


myButton = tk.Button(myRoot, text="Generate Couples", command=myGenerateCouples)
myButton.pack()


myCouplesText = tk.StringVar()
myCouplesLabel = tk.Label(myRoot, textvariable=myCouplesText, height=10, width=30, relief="solid", wraplength=200)
myCouplesLabel.pack()


myRoot.mainloop()
