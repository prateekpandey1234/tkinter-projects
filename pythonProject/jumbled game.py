from tkinter import *
from random import choice
from random import shuffle
from tkinter import messagebox
root=Tk()
root.geometry("300x300")

lab=Label(root,text="",font=("Helvetica",30))
lab.grid(row=0,column=0,columnspan=3)



lis=[ "Nagaland", "Orissa", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Tripura",
           "Uttaranchal", "Uttar Pradesh", "Haryana"," Himachal Pradesh", "Chhattisgarh"]

word=choice(lis)
l=list(word)
shuffle(l)
s="".join(l)
print(s)
lab.config(text=s)

emtry=Entry(root,relief=SUNKEN)
emtry.grid(row=1,column=0,columnspan=3,ipadx=50)

def shul():
    hit.config(text="")


    lis=[ "Nagaland", "Orissa", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Tripura",
           "Uttaranchal", "Uttar Pradesh", "Haryana"," Himachal Pradesh", "Chhattisgarh"]
    global word
    word=choice(lis)
    l=list(word)
    shuffle(l)

    s="".join(l)
    print(s)

    lab.config(text=s)

    emtry.delete(0,END)

    butt3["state"]=ACTIVE

    lab1.grid_forget()





def answer():
    global lab1
    lab1 = Label(root, text="")
    lab1.grid(row=3, column=0, columnspan=3)
    if emtry.get()==word:
        lab1.config(text="Correct")
    else:
        lab1.config(text="Wrong")


hit=Label(root,text="")
i=0
hit.grid(row=3,column=0)
sp=""
def hint():
    global sp
    global i
    sp+=word[i]
    hit.config(text=sp)
    i+=1

    if i==len(word)-3:
        resp=messagebox.showerror(title="NO MORE",message="no more hints will be given")
        butt3["state"]=DISABLED
        i=0
        sp=""


butt1=Button(root,text="answer",command=answer)
butt1.grid(row=2,column=0,padx=20)

butt3=Button(root,text="Hint",command=hint)
butt3.grid(row=2,column=1,padx=20)

butt=Button(root,text="click",command=shul)
butt.grid(row=2,column=2,padx=20)

mainloop()