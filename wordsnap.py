from tkinter import *
from convert import convert

grab_text = False

root = Tk()
root.title("Word Snap")
root.geometry("300x180+500+250")

warning = Label(root, text="",
                  font=("time new roman",10), fg='red')
warning.pack()
warning.place(x=30,y=105)

def start():
    #warning.config(state=DISABLED)
    worked = convert()
    if worked == False:
        warning.configure(text="*Ensure a new image has been added to\n the clipboard.")
    else:
        warning.configure(text="")
        

Button(root, text='Convert', width=10,command=start).place(x=110,y=145)

Label(root,
      text="Add an image to the\n clipboard, then click convert to\n have the image\
 on the clipboard\n replaced with the text on the image.",
      font=("time new roman",10),
      fg='black').place(x=40,y=25)

mainloop()
