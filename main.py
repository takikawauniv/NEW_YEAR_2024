import tkinter as tk

from PIL import Image, ImageTk


root = tk.Tk()

root.title("2:30pm")

root.geometry("400x400")



canvas = tk.Canvas(root, bg="white",height=400, width=400)

canvas.place(x=0, y=0)

image = Image.open("./image/2_30.jpg")

w_size = 400
h_size = 400

tk_image = ImageTk.PhotoImage(image.resize((w_size, h_size)))

image = tk.PhotoImage()

canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)

canvas.pack()

root.mainloop()