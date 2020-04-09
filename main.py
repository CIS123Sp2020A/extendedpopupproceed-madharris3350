#Madison Harris
#this is my extended pop up code
from tkinter import *
import tkinter.messagebox as box

#The first step after imports is create a window
window = Tk()
#This shows up at the top of the frame
window.title("Message Box Example")



def dialog():
    var = box.askyesno("Message Box", "Proceed?")
    if var == 1:
        box.showinfo("Yes Box", "Proceeding...")
    else:
        box.showwarning("No Box", "Cancelling...")

#creating a button
btn = Button(window, text="Click", command=dialog)
# I have to pack the button

btn.pack(padx=150, pady=50)
#start the action and keep it going
window.mainloop()
