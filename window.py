from tkinter import *
from wordsnap import main

grab_text = False

root = Tk()
root.title("Word Snap")
root.geometry("300x180+500+250")

def stop():
    grab_text = False

def start():
    grab_text = True
    while grab_text:
        grab_text = main()

Button(root, text='Stop', width =5,command=root.destroy).place(x=20,y=130)
Button(root, text='Start',width=5, command=start).place(x=230,y=130)

mainloop()
