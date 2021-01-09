from tkinter import *
import tkinter.font as tkFont
import wikipedia as wk
from gtts import gTTS
import threading as th

from pygame import mixer
window = Tk()
mixer.init()
window.title("JENIL WIKIPEDIA")

window.configure(padx=2,pady=2,bg="#ffffff", borderwidth=0, relief="flat")
window.wm_attributes('-alpha',0.955)
window.minsize(350,300)
window.maxsize(800,380)
window.resizable(0,0)


fontStyle = tkFont.Font(family="comic sans ms", size=10, weight="bold")
fontStyle1 = tkFont.Font(family="comic sans ms", size=10, weight="bold")
fontStyle2 = tkFont.Font(family="comic sans ms", size=6, weight="bold")
fontStyle3 = tkFont.Font(family="comic sans ms", size=10, weight="bold")
fontStyle4 = tkFont.Font(family="comic sans ms", size=9, weight="bold")

def move_window(event):
    global x
    global y
    window.geometry('+{0}+{1}'.format(event.x_root - x - 5, event.y_root - y - 4))


def get_mouse(event):
    global x
    global y
    x,y = event.x,event.y

title_bar = Label(window, text = "Wikipidea Search", justify="center", fg="#f8f8f8", bg="#ffffff", bd=0, padx=350 ,pady=5, font=fontStyle1)
#close_btn = Button(window, text = "X",command=window.destroy, justify="center", fg="#ffffff", bg="#ff6666", bd=0, padx=24 , pady=5 , font=fontStyle2)

title_bar.grid(row=0, column=0, columnspan=6, padx=1, pady=1)
#close_btn.grid(row=0, column=6, padx=1, pady=1,sticky=W+E)



#title_bar.bind("<B1-Motion>",move_window)
window.bind("<Button-1>",get_mouse)



def speech_get():
    global speech
    speech = gTTS(text=wk.summary(search_place.get()), lang="en", slow=False)

def search_place_insert():
    p6 = th.Thread(target=get_other_wiki)
    p6.start()
    searched_place.delete(1.0, END)
    searched_place.insert(END," Loading... ")


def content_place_insert():
    p2 = th.Thread (target= get_data_wiki)
    p2.start()
    content_place.delete(1.0, END)
    content_place.insert(END, " Loading... ")


def get_data_wiki():
    searched_data = wk.summary(search_place.get())
    content_place.delete(1.0, END)
    content_place.insert(END, searched_data)


def get_other_wiki():
    global a
    a = 1
    y = wk.search(search_place.get())
    searched_place.delete(1.0,END)
    for i in range(len(y)):
        searched_place.insert(END, " " + str(a) + " ) " + y[i] + "\n")
        a = (int(a) + 1)

def search_key():
    p3 = th.Thread(target=search_place_insert)
    p2 = th.Thread(target=speech_get)
    p4 = th.Thread(target=content_place_insert)
    p3.start()
    p2.start()
    p4.start()


def save_found():
    file1 = open("C:\\Users\\acer\\Documents\\jenil\\Saved\\" + search_place.get() + ".txt", "w")
    str1 = str(wk.summary(search_place.get()).encode('utf-8'))
    file1.write(str1)
    file1.close()


def down_found():
    p2 = th.Thread(target=down_found_load)
    p2.start()


def down_found_load():
    down_button = Button(window, text="Downloading Audio", command=down_found, fg="#ffffff", bg="#ff6666", bd=0, padx=0,
                         pady=0, font=fontStyle3)
    down_button.grid(row=2, column=2, columnspan=1, padx=1, pady=3)
    speech.save("C:\\Users\\acer\\Documents\\jenil\\Saved\\" + search_place.get() + ".mp3")
    down_button = Button(window, text="Download Audio", command=down_found, fg="#ffffff", bg="#afafaf", bd=0,
                         padx=10,
                         pady=0, font=fontStyle3)
    down_button.grid(row=2, column=2, columnspan=1, padx=1, pady=3)
def play_found():
    p8 = th.Thread(target=play_found_sound)
    p8.start()



def play_found_sound():

    mixer.music.load("C:\\Users\\acer\\Documents\\jenil\\Saved\\" + str(search_place.get()) + ".mp3")
    mixer.music.play(0)

def play_stop():

    mixer.music.stop()




search_place = Entry(window, bd=0, width=50, bg="#ffffff", justify="center", font=fontStyle)
search_button = Button(window, text="Search", command=search_key, fg="#ffffff", bg="#0f0f0f", bd=0, padx=10, pady=2, font=fontStyle3)
play_button = Button(window, text="Play", command= play_found, fg="#ffffff", bg="#afafaf", bd=0, padx=10, pady=0, font=fontStyle3)
stop_button = Button(window, text="Stop", command= play_stop, fg="#ffffff", bg="#afafaf", bd=0, padx=10, pady=0, font=fontStyle3)
down_button = Button(window, text="Download Audio", command= down_found, fg="#ffffff", bg="#afafaf", bd=0, padx=10, pady=0, font=fontStyle3)
save_button = Button(window, text="Save Txt", command= save_found, fg="#ffffff", bg="#afafaf", bd=0, padx=10, pady=0, font=fontStyle3)
content_place = Text(window, width=58, height=14, bg="#ffffff", bd=0, font=fontStyle3, wrap=WORD)
searched_place = Text(window, width=30, height=13, bg="#eaeaea", bd=0, font=fontStyle4, wrap=WORD, spacing3=4)

sounded = search_place.get()

search_place.grid(row=1, column=1, columnspan=3, padx=1, pady=1)
search_button.grid(row=1, column=4, columnspan=1, padx=1, pady=1)
down_button.grid(row=2, column=2, columnspan=1, padx=1, pady=3)
save_button.grid(row=2, column=0, columnspan=1, padx=1, pady=3)
play_button.grid(row=2, column=4, columnspan=1, padx=1, pady=3)
stop_button.grid(row=2, column=5, columnspan=1, padx=1, pady=3)
content_place.grid(row=3, column=1, columnspan=6, rowspan=5, pady=5, padx=3)
searched_place.grid(row=3, column=0, columnspan=2, rowspan=1, pady=10, padx=5)







window.mainloop()


