from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pygame

pygame.init()
root=Tk()
root.geometry("500x500")

#CREATING PLAYLISTS.....DROPDOWN BOX
playlist=Listbox(root,fg="green",bg="black",width=60)
playlist.grid(row=0,column=0,columnspan=5,padx=40,pady=30)

#CREATING EVERY TYPE OF COMMANDS

#adding songs in list
def adsong():
    names=filedialog.askopenfilenames()
    for music in names:
        playlist.insert(0,music[58:])
#removing songs from list
def resong():
    for i in playlist.curselection():
        playlist.delete(i, i)
#loading songs
global paused
paused=False
def wait(is_paused):
    global paused
    paused=is_paused

    if paused==False:
        pygame.mixer.music.pause()
        pause.config(image=cont)
        paused=True
    else:
        pygame.mixer.music.unpause()
        pause.config(image=paus)
        paused=False
def play():
    s=playlist.get(ACTIVE)
    pause.config(image=paus)
    pygame.mixer.music.load("C:/Users/LUCKY/PycharmProjects/pythonProject/music folder/"+s)
    print("music folder/"+s)
    pygame.mixer.music.play()
def stop():
    pause.config(image=paus)
    playlist.select_clear(0,END)
    pygame.mixer.music.stop()
def frwd():
    l=playlist.get(0, playlist.size())
    i=int(playlist.curselection()[0])
    playlist.select_clear(0, END)
    if i==playlist.size()-1:
        sw=l[0]
        playlist.activate(0)
        playlist.select_set(0,last=None)
    else:
        sw=l[i+1]
        playlist.select_set(i+1,last=None)

        playlist.activate(i+1)
    pause.config(image=paus)
    pygame.mixer.music.load("music folder/" + sw)
    pygame.mixer.music.play()
def bckw():
    l = playlist.get(0, playlist.size())
    i = int(playlist.curselection()[0])
    playlist.select_clear(0, END)
    if i == 0:
        sw = l[-1]
        playlist.select_set(-1,last=None)
        playlist.activate(-1)
    else:
        sw = l[i - 1]
        playlist.select_set(first=i-1,last=i-1)
        playlist.activate(i-1)
    pause.config(image=paus)
    pygame.mixer.music.load("music folder/" + sw)
    pygame.mixer.music.play()
#OPENING IMAGES
cont=PhotoImage(file="polpop/circle.png").subsample(10,10)
fow=PhotoImage(file="polpop/forward.png").subsample(10,10)
bac=PhotoImage(file="polpop/backward.png").subsample(10,10)
stop1=PhotoImage(file="polpop/stop.png").subsample(10,10)
paus=PhotoImage(file="polpop/pause.png").subsample(10,10)
play1=PhotoImage(file="polpop/media_player_button_2-512.png").subsample(10,10)

#CREATING PLAY BUTTONS......IMAGE+BUTTON
forw=Button(root,image=fow,borderwidth=0,command=frwd)
forw.grid(row=1,column=0,padx=10)

halt=Button(root,image=stop1,borderwidth=0,command=stop)
halt.grid(row=1,column=1,padx=10)

back=Button(root,image=bac,borderwidth=0,command=bckw)
back.grid(row=1,column=2,padx=10)

pause=Button(root,image=paus,borderwidth=0,command=lambda: wait(paused))
pause.grid(row=1,column=3,padx=10)

playbutt=Button(root,image=play1,borderwidth=0,command=play)
playbutt.grid(row=1,column=4,padx=10)


#CREATING MENU BARS.....ADDING AND REMOVING SONGS
mymenu=Menu(root,cursor="heart")
root.config(menu=mymenu)

add_songs=Menu(mymenu)
remove_song=Menu(mymenu)
mymenu.add_cascade(label="add song",menu=add_songs)
mymenu.add_cascade(label="remove songs",menu=remove_song)
add_songs.add_command(label="add one song",command=adsong)
remove_song.add_command(label="remove songs",command=resong)


mainloop()