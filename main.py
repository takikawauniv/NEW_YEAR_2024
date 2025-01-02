import tkinter as tk
from pygame import mixer

from PIL import Image, ImageTk


def command():
    text.set("yarimashita")
    mixer.music.play(loops=1)

mixer.init()
mixer.music.load("./sound/yarimasune.mp3")
root = tk.Tk()
root.title("2:30pm")
root.geometry("400x600")

canvas = tk.Canvas(root, bg="white",height=400, width=400)
canvas.place(x=0, y=0)
image = Image.open("./image/2_30.jpg")
w_size = 400
h_size = 400
tk_image = ImageTk.PhotoImage(image.resize((w_size, h_size)))
image = tk.PhotoImage()
canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
canvas.pack()

frame = tk.Frame(root)
frame.pack(fill = tk.BOTH, expand = True)

text = tk.StringVar(frame)
text.set("yarimasuka?")

button = tk.Button(frame, textvariable=text, command=command)
button.pack()


root.mainloop()

