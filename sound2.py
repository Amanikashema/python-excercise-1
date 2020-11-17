from tkinter import*
import os
import pygame

root = Tk()
root.title("Music Player")
root.geometry('700x550')

status = StringVar()
track = StringVar

label_play = LabelFrame(root,text="Song Track")
label_play.place(x=0,y=0,width=340,height=100)

result = Label(label_play, textvariable=track).pack()
track_status = Label(label_play, textvariable=status).pack()

# control panel label
label_play2 = LabelFrame(root, text="Control Panel")
label_play2.place(x=0,y=100)

# function to play music
def play_music():
    file = playlist.get(ACTIVE)
    status.set(file + "-Playing")
    pygame.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(loops=0)

# function to stop a song
def stop_song():
    file = playlist.get(ACTIVE)
    status.set(file + "-Stopped")
    pygame.mixer.music.stop()

# function to pause a song
def pause_song():
    file = playlist.get(ACTIVE)
    status.set(file + "-Paused")
    pygame.mixer.music.pause()

# function to unpause a song
def unpause_song():
    file = playlist.get(ACTIVE)
    status.set(file + "-Playing")
    pygame.mixer.music.unpause()

# buttons for the music player
play_button = Button(label_play2,text="play Song",command=play_music)
play_button.pack(side=LEFT)

pause_song_button = Button(label_play2,text="pause",command=pause_song)
pause_song_button.pack(side=LEFT)

unpause_song_button= Button(label_play2,text="Unpause",command=unpause_song)
unpause_song_button.pack(side=LEFT)

stop_play_button = Button(label_play2,text="stop song",command=stop_song)
stop_play_button.pack(side=LEFT)

# music selection box
songs_frame = LabelFrame(root,text="Song Playlist",font=15,bg="grey",fg="white",bd=5)
songs_frame.place(x=340,y=0,width=360,height=154)
scroll_bar = Scrollbar(songs_frame,orient=VERTICAL)
scroll_bar.pack(side=RIGHT,fill=Y)
playlist = Listbox(songs_frame,yscrollcommand=scroll_bar.set,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)
playlist.pack()
scroll_bar.pack(side=RIGHT,fill=Y)
scroll_bar.config(command=playlist.yview)
playlist.pack(fill=BOTH)

# songs directory
os.chdir("songs")
song_tracks = os.listdir()
for track in song_tracks:
    playlist.insert(END,track)

root.mainloop()


