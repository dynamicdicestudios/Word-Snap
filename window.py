from tkinter import *
from wordsnap import main

grab_text = False

root = Tk()
root.title("Word Snap")
root.geometry("300x180+500+250")

#warning.config(state=DISABLED)

def start():
    #warning.config(state=DISABLED)
    worked = main()
    if worked == False:
        warning = Label(root, text="*Ensure an image has been added to\n the clipboard",
                  font=("time new roman",10), fg='red').place(x=40,y=105)
        

Button(root, text='Convert', width=10,command=start).place(x=110,y=145)

Label(root,
      text="Add an image to the\n clipboard, then click start to\n have the image\
 on the clipboard\n replaced with the text on the image.",
      font=("time new roman",10),
      fg='black').place(x=30,y=25)




mainloop()
