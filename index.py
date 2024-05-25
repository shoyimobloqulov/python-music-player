from tkinter import *
from tkinter import ttk
import pygame
from tkinter import filedialog
from mutagen.mp3 import MP3
import os
import time
from tkinter import messagebox 


root = Tk()
root.title('JALOLOVA')
root.iconbitmap('icons/music.ico')
root.geometry("500x400")

# Initialize Pygame Mixers
pygame.mixer.init()

def play_time():
    current_time = pygame.mixer.music.get_pos() / 1000
    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

    song = song_box.get(ACTIVE)
    song = f"audio/{song}.mp3"
    song_mut = MP3(song)
    song_length = song_mut.info.length
    converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))

    status_bar.config(text=f'{converted_current_time} / {converted_song_length}')

    # Update progress bar
    progress_bar['value'] = (current_time / song_length) * 100
    if int(progress_bar['value']) < 100:
        status_bar.after(1000, play_time)

def add_song():
    file_path = filedialog.askopenfilename(initialdir='audio/', title="Qo'shiq tanlang", filetypes=(("mp3 Files", "*.mp3"),))

    song = os.path.basename(file_path)
    song = song.replace(".mp3", "")

    song_box.insert(END, song)

def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='audio/', title="Qo'shiq tanlang", filetypes=(("mp3 Files", "*.mp3"),))
    for song in songs:
        song = os.path.basename(song)
        song = song.replace(".mp3", "")

        song_box.insert(END, song)

def play():
    try:
        song = song_box.get(ACTIVE)
        song = f'audio/{song}.mp3'
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        play_time()
    except Exception as e:
        messagebox.showerror("Xatolik", "Xatolik aniqlandi. Qo'shishlarni qo'shishingiz kerak." + f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}") 

def stop():
    pygame.mixer.music.stop()
    song_box.select_clear(ACTIVE)
    status_bar.config(text='')
    progress_bar['value'] = 0

global paused
paused = False

def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

def next_song():
    next_one = song_box.curselection()
    if next_one:
        next_one = next_one[0] + 1
        if next_one < song_box.size():
            song = song_box.get(next_one)
            
            song = f'audio/{song}.mp3'
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops=0)

            song_box.selection_clear(0, END)
            song_box.activate(next_one)
            song_box.selection_set(next_one, last=None)

def previous_song():
    try:
        next_one = song_box.curselection()
        next_one = next_one[0] - 1
        song = song_box.get(next_one)

        song = f'audio/{song}.mp3'
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        song_box.selection_clear(0, END)
        song_box.activate(next_one)
        song_box.selection_set(next_one, last=None)
    except Exception as e:
        messagebox.showerror("Xatolik", "Xatolik aniqlandi. " + f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
def delete_song():
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()

def delete_all_song():
    song_box.delete(0, END)
    pygame.mixer.music.stop()

song_box = Listbox(root, bg="black", fg="white", width=85, selectforeground="white")
song_box.pack(pady=20)

back_btn = PhotoImage(file='icons/play-back.png').subsample(5,5)
forward_btn = PhotoImage(file='icons/play-forward.png').subsample(5,5)
play_btn = PhotoImage(file='icons/play.png').subsample(5,5)
pause_btn = PhotoImage(file='icons/pause.png').subsample(5,5)
stop_btn = PhotoImage(file='icons/stop.png').subsample(5,5)

controls_frame = Frame(root)
controls_frame.pack()

back_button = Button(controls_frame, image=back_btn, borderwidth=1, command=previous_song)
forward_button = Button(controls_frame, image=forward_btn, borderwidth=1, command=next_song)
play_button = Button(controls_frame, image=play_btn, borderwidth=1, command=play)
pause_button = Button(controls_frame, image=pause_btn, borderwidth=1, command=lambda: pause(paused))
stop_button = Button(controls_frame, image=stop_btn, borderwidth=1, command=stop)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

# Set button and listbox background and foreground colors
back_button.configure(fg='silver',borderwidth=0)
forward_button.configure(fg='silver',borderwidth=0)
play_button.configure(fg='silver',borderwidth=0)
pause_button.configure(fg='silver',borderwidth=0)
stop_button.configure(fg='silver',borderwidth=0)
song_box.configure(bg='white', fg='black',borderwidth=0)

my_menu = Menu(root)
root.config(menu=my_menu)

add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Qo'shiq qo'shish", menu=add_song_menu)
add_song_menu.add_command(label="Qo'shiq", command=add_song)
add_song_menu.add_command(label="Qo'shiqlar", command=add_many_songs)

remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Qo'shiq o'chirish", menu=remove_song_menu)
remove_song_menu.add_command(label="Qo'shiqni o'chirish", command=delete_song)
remove_song_menu.add_command(label="Qo'shiqlarni o'chirish", command=delete_all_song)

status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

# Create Progress Bar
progress_bar = ttk.Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate')
progress_bar.pack(pady=10)

root.mainloop()
