from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("YOYOYo")
def frwd(num):
    global lb
    global bt3
    global bt2
    lb.grid_forget()
    bt3 = Button(root, text="Right", command=lambda :frwd(num+1))
    bt1 = Button(root, text="Left", command=lambda :back(num-1))
    lb = Label(image=l[num], height=200, width=300)
    if num==5:
        bt3 = Button(root, text="Right", state=DISABLED)
    bt1.grid(row=1, column=0)
    bt3.grid(row=1, column=2)
    lb.grid(row=0, column=0, columnspan=3)
def back(num):
    global lb
    global bt3
    global bt2
    lb.grid_forget()
    if num==0:
        bt1 = Button(root, text="Left", state=DISABLED)
    else:bt1 = Button(root, text="Left", command=lambda: back(num - 1))
    bt3 = Button(root, text="Right", command=lambda:frwd(num + 1))
    lb = Label(image=l[num], height=200, width=300)

    bt1.grid(row=1, column=0)
    bt3.grid(row=1, column=2)
    lb.grid(row=0, column=0, columnspan=3)
img1=ImageTk.PhotoImage(Image.open("polpop/2.jpg"))
img2=ImageTk.PhotoImage(Image.open("polpop/3.jpg"))
img3=ImageTk.PhotoImage(Image.open("polpop/4.jpg"))
img4=ImageTk.PhotoImage(Image.open("polpop/5.jpg"))
img5=ImageTk.PhotoImage(Image.open("polpop/6.jpg"))
img6=ImageTk.PhotoImage(Image.open("polpop/7.jpg"))
l=[img1,img2,img3,img4,img5,img6]
lb=Label(image=img1,height=200,width=300)
lb.grid(row=0,column=0,columnspan=3)
bt1=Button(root,text="Left",command=back,state=DISABLED)
bt2=Button(root,text="Exit",command=root.destroy)
bt3=Button(root,text="Right",command=lambda:frwd(2))
bt1.grid(row=1,column=0)
bt2.grid(row=1,column=1)
bt3.grid(row=1,column=2)

mainloop()