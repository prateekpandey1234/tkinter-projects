from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
from tkinter import colorchooser
root=Tk()
root.geometry("1000x600")
root.title("Text editor biatch")


#setting variable for file name
global fuoname
fuoname = False
#defining functions

def open_file():
    box.delete("1.0", END)
    file1=filedialog.askopenfilename()
    if file1:
        global fuoname
        fuoname = file1
    file_opened=open(file1,"r")
    stuff=file_opened.read()
    box.insert(1.0,stuff)
    file_opened.close()
    fuk=str(file1)
    name_file=fuk[len(fuk)-1-fuk[::-1].index("/")+1:]
    root.title(name_file)
def save_as_file():
    file1 = filedialog.asksaveasfilename(initialdir="C:/Users/LUCKY/PycharmProjects/pythonProject/polpop",filetypes=(("txt files","*.txt"),("all","*.*")))
    file_opened = open(file1, "w")
    file_opened.write(box.get(1.0,END))
    file_opened.close()
def new_file():
    box.delete("1.0",END)
    root.title("New file")
    global fuoname
    fuoname = False
def save_file():
    global fuoname
    if fuoname:
        file_opened = open(fuoname, "w")
        file_opened.write(box.get(1.0, END))
        file_opened.close()
        messagebox.showinfo(title="Saved",message="Your file is saved")
    else:
        save_as_file()
def cut():
    global selected
    if box.selection_get():
        selected=box.selection_get()
        box.delete("sel.first","sel.last")
def copy():
    global selected
    if box.selection_get():
        selected=box.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)
def paste():
    global selected
    pos=box.index(INSERT)
    box.insert(pos,selected)
def tagfunc():
    bold=font.Font(box,box.cget("font"))
    bold.config(weight="bold")
    box.tag_config("bold",font=bold)
    tag=box.tag_names("sel.first")
    if "bold" in tag:
        box.tag_remove("bold","sel.first","sel.last")
    else:
        box.tag_add("bold","sel.first","sel.last")
def tagfunc3():
    bold=font.Font(box,box.cget("font"))
    bold.config(slant="italic")
    box.tag_config("italic",font=bold)
    tag=box.tag_names("sel.first")
    if "italic" in tag:
        box.tag_remove("italic","sel.first","sel.last")
    else:
        box.tag_add("italic","sel.first","sel.last")
def clolorbutton():
    color=colorchooser.askcolor()
    if color:
        bcolod= font.Font(box, box.cget("font"))
        box.tag_config("colored",font=bcolod,foreground=color[1])
        tag = box.tag_names("sel.first")
        if "colored" in tag:
            box.tag_remove("colored", "sel.first", "sel.last")
        else:
            box.tag_add("colored", "sel.first", "sel.last")
        box.selection_clear()
    box.selection_clear()

#frame and scrollbar and text box and menu
frm = Frame(root)
frm.pack()

scroll=Scrollbar(frm)
scroll.pack(side=RIGHT,fill=Y)

scroll2=Scrollbar(frm,orient=HORIZONTAL)
scroll2.pack(side=BOTTOM,fill=X)

box=Text(frm,width=70,height=30,font=("Helvetica",20),relief=SUNKEN,undo=True,selectforeground="black",selectbackground="red",wrap="none",yscrollcommand=scroll.set,xscrollcommand=scroll2.set)
box.pack()

scroll.config(command=box.yview)
scroll2.config(command=box.xview)

frame=Frame(root)
frame.pack(pady=20)

menu1=Menu(root,tearoff=False)
root.config(menu=menu1)

file=Menu(menu1,tearoff=False)
menu1.add_cascade(label="file",menu=file)
file.add_command(label="New",command=new_file)
file.add_command(label="open",command=open_file)
file.add_command(label="save",command=save_file)
file.add_command(label="save as",command=save_as_file)
file.add_separator()
file.add_command(label="Exit",command=root.quit)

edit=Menu(menu1,tearoff=False)
menu1.add_cascade(label="Edit",menu=edit)
edit.add_command(label="cut",command=cut)
edit.add_command(label="copy",command=copy)
edit.add_command(label="paste",command=paste)
font3=Menu(edit,tearoff=False)
edit.add_separator()
edit.add_cascade(label="Font",menu=font3)
font3.add_command(label="Bold",command=tagfunc)
font3.add_command(label="Italics",command=tagfunc3)
edit.add_command(label="change colour",command=clolorbutton)


mainloop()