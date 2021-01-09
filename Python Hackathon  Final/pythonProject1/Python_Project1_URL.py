import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.geometry("600x400")
root.title("URL shortener")
root.configure(bg="#49A")
url = StringVar()
url_addrerss = StringVar()

def urlshhortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_addrerss.set(url_short)

def copyurl():
    url_short = url_addrerss.get()
    pyperclip.copy(url_short)



Label(root,text="My URL Shortener",font="poppins").pack(pady=20)
Label(root,text="Enter your URL",font="poppins").pack(pady=10)
Entry(root,textvariable=url).pack(pady=5)
Button(root,text="Generate Short URL", command=urlshhortener).pack(pady=10)
Entry(root,textvariable=url_addrerss).pack(pady=10)
Button(root,text="Copy URL", command=copyurl).pack(pady=5)

root.mainloop()