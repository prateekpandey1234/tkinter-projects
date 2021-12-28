from tkinter import *
from tkinter import messagebox
root=Tk()
root.config(bg="grey")
#defining variable
global game
global l
global x
l=[]
game="X"
x=1
#creating functions
def NEW_game():
    global l
    global x
    for j in l:
        j.config(text="", bg="grey")
    l=[]
    x=1
def checker():
    if (butt4["text"]=="X" and butt1["text"]=="X" and butt7["text"]=="X") or (butt4["text"]=="O" and butt1["text"]=="O" and butt7["text"]=="O"):
        butt1.config(bg="red")
        butt4.config(bg="red")
        butt7.config(bg="red")
        messagebox.showinfo(title="Game Over",message="Player 1 Won!!" if butt1["text"]=="X" else "Player 2 won")
        NEW_game()
    elif (butt1["text"]=="X" and butt5["text"]=="X" and butt9["text"]=="X") or (butt1["text"]=="O" and butt5["text"]=="O" and butt9["text"]=="O"):
        butt1.config(bg="red")
        butt5.config(bg="red")
        butt9.config(bg="red")
        messagebox.showinfo(title="Game Over",message="Player 1 Won!!" if butt1["text"]=="X" else "Player 2 won")
        NEW_game()
    elif (butt3["text"]=="X" and butt1["text"]=="X" and butt2["text"]=="X") or (butt3["text"]=="O" and butt1["text"]=="O" and butt2["text"]=="O"):
        butt1.config(bg="red")
        butt3.config(bg="red")
        butt2.config(bg="red")
        messagebox.showinfo(title="Game Over",message="Player 1 Won!!" if butt1["text"]=="X" else "Player 2 won")
        NEW_game()
    elif (butt2["text"]=="X" and butt5["text"]=="X" and butt8["text"]=="X") or (butt2["text"]=="O" and butt5["text"]=="O" and butt8["text"]=="O"):
        butt2.config(bg="red")
        butt5.config(bg="red")
        butt8.config(bg="red")
        messagebox.showinfo(title="Game Over",message="Player 1 Won!!" if butt2["text"]=="X" else "Player 2 won")
        NEW_game()
    elif (butt3["text"]=="X" and butt6["text"]=="X" and butt9["text"]=="X") or (butt3["text"]=="O" and butt6["text"]=="O" and butt9["text"]=="O"):
        butt3.config(bg="red")
        butt6.config(bg="red")
        butt9.config(bg="red")
        messagebox.showinfo(title="Game Over",message="Player 1 Won!!" if butt3["text"]=="X" else "Player 2 won")
        NEW_game()
    elif (butt4["text"]=="X" and butt5["text"]=="X" and butt6["text"]=="X") or (butt4["text"]=="O" and butt5["text"]=="O" and butt6["text"]=="O"):
        butt4.config(bg="red")
        butt5.config(bg="red")
        butt6.config(bg="red")
        messagebox.showinfo(title="Game Over",message="Player 1 Won!!" if butt4["text"]=="X" else "Player 2 won")
        NEW_game()
    elif (butt7["text"]=="X" and butt8["text"]=="X" and butt9["text"]=="X") or (butt7["text"]=="O" and butt8["text"]=="O" and butt9["text"]=="O"):
        butt7.config(bg="red")
        butt8.config(bg="red")
        butt9.config(bg="red")
        messagebox.showinfo(title="Game Over",message="Player 1 Won!!"if butt7["text"]=="X" else "Player 2 won")
        NEW_game()
    elif (butt3["text"]=="X" and butt5["text"]=="X" and butt7["text"]=="X") or (butt3["text"]=="O" and butt5["text"]=="O" and butt7["text"]=="O"):
        butt3.config(bg="red")
        butt5.config(bg="red")
        butt7.config(bg="red")
        messagebox.showinfo(title="Game Over",message="Player 1 Won!!"if butt7["text"]=="X" else "Player 2 won")
        NEW_game()
def clickthebutton(button_pressed):
    global l
    global game
    global x

    if x%2!=0 and button_pressed not in l:
        x+=1
        button_pressed.config(text="X")
        l.append(button_pressed)
        checker()
    elif x%2==0 and button_pressed not in l:
        button_pressed.config(text="O")
        l.append(button_pressed)
        x+=1
        checker()
    return


#creating buttons and menu
butt1=Button(root,text="",height=4,width=9,bg="grey",fg="light blue",font=("Helvetica",20))
butt1.grid(row=0,column=0)
butt2=Button(root,text="",height=4,width=9,bg="grey",fg="light blue",font=("Helvetica",20))
butt2.grid(row=0,column=1)
butt3=Button(root,text="",height=4,width=9,bg="grey",fg="light blue",font=("Helvetica",20))
butt3.grid(row=0,column=2)
butt4=Button(root,text="",height=4,width=9,bg="grey",fg="light blue",font=("Helvetica",20))
butt4.grid(row=1,column=0)
butt5=Button(root,text="",height=4,width=9,bg="grey",fg="light blue",font=("Helvetica",20))
butt5.grid(row=1,column=1)
butt6=Button(root,text="",height=4,width=9,bg="grey",fg="light blue",font=("Helvetica",20))
butt6.grid(row=1,column=2)
butt7=Button(root,text="",height=4,width=9,bg="grey",fg="light blue",font=("Helvetica",20))
butt7.grid(row=2,column=0)
butt8=Button(root,text="",height=4,width=9,bg="grey",fg="light blue",font=("Helvetica",20))
butt8.grid(row=2,column=1)
butt9=Button(root,text="",height=4,width=9,bg="grey",fg="light blue",font=("Helvetica",20))
butt9.grid(row=2,column=2)

butt1.config(command=lambda button=butt1:clickthebutton(button))
butt2.config(command=lambda button=butt2:clickthebutton(button))
butt3.config(command=lambda button=butt3:clickthebutton(button))
butt4.config(command=lambda button=butt4:clickthebutton(button))
butt5.config(command=lambda button=butt5:clickthebutton(button))
butt6.config(command=lambda button=butt6:clickthebutton(button))
butt7.config(command=lambda button=butt7:clickthebutton(button))
butt8.config(command=lambda button=butt8:clickthebutton(button))
butt9.config(command=lambda button=butt9:clickthebutton(button))



menu1=Menu(root)
root.config(menu=menu1)
new=Menu(menu1,tearoff=False)
menu1.add_cascade(label="New",menu=new)
new.add_command(label="New game",command=NEW_game)
new.add_separator()
new.add_command(label="Quit",command=root.destroy)




mainloop()