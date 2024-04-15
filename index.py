from tkinter import *
import pygame
from functions import resizeImage
from tkinter import filedialog
import os
root = Tk()
root.title('JALOLOVA')
root.iconbitmap('icons/music.ico')
root.geometry("500x400")

#Initialze Pygame Mixers
pygame.mixer.init()

# Add song Function
def add_song():
    file_path = filedialog.askopenfilename(initialdir='audio/',title="Qo'shiq tanlang",filetypes=(("mp3 Files","*.mp3"),))
    
    #strip out the directory info and .mp3 extension from the song replace
    song = os.path.basename(file_path)
    song = song.replace(".mp3", "")

    #add song to ListBox
    song_box.insert(END,song)

#Play selected song
def play():
    song = song_box.get(ACTIVE)
    song = f'audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

#Stop playing button
def stop():
    pygame.mixer.music.stop()
    song_box.select_clear(ACTIVE)

# Create Global Pause Varable
global paused
paused = False


#Pause button function
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        #Unpause
        pygame.mixer.music.unpause()
        paused = False
    else:
        #Pause
        pygame.mixer.music.pause()
        paused = True

#Create PlayList Box
song_box = Listbox(root,bg="black",fg="green",width=80,selectbackground="gray",selectforeground="black")
song_box.pack(pady=20)

#Define Player Control Button Images
back_btn = PhotoImage(file='icons/play-back.png').subsample(4,4)
forward_btn = PhotoImage(file='icons/play-forward.png').subsample(4,4)
play_btn = PhotoImage(file='icons/play.png').subsample(4,4)
pause_btn = PhotoImage(file='icons/pause.png').subsample(4,4)
stop_btn = PhotoImage(file='icons/stop.png').subsample(4,4)

#Create Player Control Frame
controls_frame = Frame(root)
controls_frame.pack()


#Create Player Control Buttons
back_button = Button(controls_frame,image=back_btn,borderwidth=1)
forward_button = Button(controls_frame,image=forward_btn,borderwidth=1)
play_button = Button(controls_frame,image=play_btn,borderwidth=1,command=play)
pause_button = Button(controls_frame,image=pause_btn,borderwidth=1,command=lambda : pause(paused))
stop_button = Button(controls_frame,image=stop_btn,borderwidth=1,command=stop)

# Buttons Grid Frame
back_button.grid(row=0,column=0,padx=10)
forward_button.grid(row=0,column=1,padx=10)
play_button.grid(row=0,column=2,padx=10)
pause_button.grid(row=0,column=3,padx=10)
stop_button.grid(row=0,column=4,padx=10)


#Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Qo'shiq qo'shish",menu=add_song_menu)
add_song_menu.add_command(label="Playlist",command=add_song)

root.mainloop()

