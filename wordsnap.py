from tkinter import *
from convert import convert
from multiprocessing.pool import ThreadPool

root = Tk()
root.title("Word Snap")
root.geometry("300x180+500+250")

warning = Label(root, text="",
                  font=("time new roman",10), fg='red')
warning.pack()
warning.place(x=30,y=105)

success = Label(root, text="",
                  font=("time new roman",10), fg='green')
success.pack()
success.place(x=30,y=120)

def start():
    success.configure(text="")
    pool = ThreadPool(processes=1)
    
    async_result = pool.apply_async(convert)
    worked = async_result.get()
    
    if worked == False:
        warning.configure(text="*Ensure a new image has been added to\n the clipboard.")
    #elif worked == None:
        #warning.configure(text="*No text could be found on the image.")
    else:
        warning.configure(text="")
        success.configure(text="Finished converting! Check your clipboard.")
        

Button(root, text='Convert', width=10,command=start).place(x=110,y=145)

Label(root,
      text="Add an image to the\n clipboard, then click convert to\n have the image\
 on the clipboard\n replaced with the text on the image.\n\nNote: The image cannot be a file.",
      font=("time new roman",10),
      fg='black').place(x=40,y=5)

mainloop()
