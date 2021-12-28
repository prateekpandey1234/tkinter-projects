from tkinter import *
from PIL import ImageTk,Image
from random import randint
root=Tk()
root.geometry("500x500")
states_frame=Frame(root,height=100,width=100)
capitals_frame=Frame(root,height=100,width=100)

def answer():
    s=""
    if e.get().lower()==l[rand]:
        s+="Right answer"
    else:
        s+="Wrong answer\n Right answer is "+l[rand]
    ans_lab.config(text=s)
def states():
    forget_frames()
    for widget in states_frame.winfo_children():
        widget.destroy()
    for widget in capitals_frame.winfo_children():
        widget.destroy()
    states_frame.pack()

    labe=Label(states_frame,text="states").pack()
    global l
    l=["sikkim","jharkhand","uttrakhand","japan","germany"]
    global rand
    rand=randint(0,len(l)-1)

    global img
    img=ImageTk.PhotoImage(Image.open("states/"+l[rand]+".png"))
    lne=Label(states_frame,image=img,padx=10,pady=10)
    lne.pack(pady=10)

    global e
    e=Entry(states_frame,relief="raised")
    e.pack(fill="x",pady=10)


    ans=Button(states_frame,text="Answer",command=answer)
    ans.pack(pady=10)

    pas=Button(states_frame,text="Pass",command=states)
    pas.pack(pady=10)

    global ans_lab
    ans_lab=Label(states_frame,text="")
    ans_lab.pack(pady=10)

def capitals():
    forget_frames()
    for widget in states_frame.winfo_children():
        widget.destroy()
    for widget in capitals_frame.winfo_children():
        widget.destroy()

    capitals_frame.pack(fill="both",expand=True)
    labe = Label(capitals_frame, text="capitals").pack()

def forget_frames():
    states_frame.pack_forget()
    capitals_frame.pack_forget()

men=Menu(root,cursor="cross")
root.config(menu=men)
men0=Menu(men)
men.add_cascade(label="Geography",menu=men0)
men0.add_command(label="States",command=states)
men0.add_command(label="Capitals",command=capitals)
men0.add_separator()
men0.add_command(label="Exit",command=root.quit)

mainloop()