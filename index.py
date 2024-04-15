from tkinter import *
import pygame
root = Tk()
root.title('JALOLOVA')
root.iconbitmap('music.ico')
root.geometry("500x400")
pygame.mixer.init()

def play():
    pygame.mixer.music.load("audio/bass.mp3")
    pygame.mixer.music.play(loops=0)
def stop():
    pygame.mixer.music.stop()

my_button = Button(root,text="Eshitish",font=("Helvetica",14),command=play)
my_button.pack(pady=20)

stop_button = Button(root,text="To'xtatish",font=("Helvetica",14),command=stop)
stop_button.pack()

root.mainloop()

