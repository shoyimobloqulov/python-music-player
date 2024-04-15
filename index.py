from tkinter import *
import pygame
from functions import resizeImage
root = Tk()
root.title('JALOLOVA')
root.iconbitmap('icons/music.ico')
root.geometry("500x400")

#Initialze Pygame Mixers
pygame.mixer.init()

#Create PlayList Box
song_box = Listbox(root,bg="black",fg="green",width=80)
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
play_button = Button(controls_frame,image=play_btn,borderwidth=1)
pause_button = Button(controls_frame,image=pause_btn,borderwidth=1)
stop_button = Button(controls_frame,image=stop_btn,borderwidth=1)

# Buttons Grid Frame
back_button.grid(row=0,column=0,padx=10)
forward_button.grid(row=0,column=1,padx=10)
play_button.grid(row=0,column=2,padx=10)
pause_button.grid(row=0,column=3,padx=10)
stop_button.grid(row=0,column=4,padx=10)



root.mainloop()

