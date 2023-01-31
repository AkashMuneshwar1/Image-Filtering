from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from pil import Image, ImageTk
import cv2


def upload_file():
    global img
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    image = cv2.imread(filename)
    resized1 = cv2.resize(image, (600, 680))
    resizeshow = cv2.resize(image, (300, 300))
    cv2.imshow('Image', resizeshow)


    def fil1():
        gb = cv2.GaussianBlur(resized1, (7, 7), 0)
        re1 = cv2.resize(gb, (350, 350))
        cv2.imshow('GaussianBlur', re1)

        def save1():
            file = filedialog.asksaveasfilename(filetypes=(('image', '*.jpg'), ('All', '*.*')),defaultextension='*.jpg')
            cv2.imwrite(file, re1)

        button0 = Button(window, text='Save', font=('Times_New_Roman', 12), bg='blue', foreground='white',command=save1)
        button0.place(x=450, y=155,width = 74,height = 31)

    b0 = Button(text="Gaussion", font="roboto 12 bold", relief="flat", bg="#007cc7", fg="#fff",command=fil1)
    b0.place(x=444, y=106, width=89, height=40)


    def fil2():
        mb = cv2.medianBlur(resized1, 7)
        re1 = cv2.resize(mb, (350, 350))
        cv2.imshow('Median_Blur', re1)

        def save2():
            file = filedialog.asksaveasfilename(filetypes=(('image', '*.jpg'), ('All', '*.*')),defaultextension='*.jpg')
            cv2.imwrite(file, re1)
        button1 = Button(window, text='Save', font=('Times_New_Roman', 12), bg='blue', foreground='white',command=save2)
        button1.place(x=580, y=155,width = 74,height = 31)

    b1 = Button(text="Median", font="roboto 12 bold", relief="flat", bg="#007cc7", fg="#fff",command=fil2)
    b1.place(x=572, y=106,width=89,height=40)



    def fil3():
        b = cv2.bilateralFilter(resized1, 10, 80, 80)
        re1 = cv2.resize(b, (350, 350))
        cv2.imshow('Bilateral_Filter', re1)

        def save3():
            file = filedialog.asksaveasfilename(filetypes=(('image', '*.jpg'), ('All', '*.*')),defaultextension='*.jpg')
            cv2.imwrite(file, re1)

        button2 = Button(window, text='Save', font=('Times_New_Roman', 12), bg='blue', foreground='white',command=save3)
        button2.place(x=450, y=255,width = 74,height = 31)

    img2 = PhotoImage(file=f"img2.png")
    b2 = Button(text="Bilateral", font="roboto 12 bold", relief="flat", bg="#007cc7", fg="#fff",command=fil3)
    b2.place(x=444, y=205,width=89,height=40)


    def fil4():
        g = cv2.cvtColor(resized1, cv2.COLOR_BGR2GRAY)
        re1 = cv2.resize(g, (350, 350))
        cv2.imshow('Gray', re1)

        def save4():
            file = filedialog.asksaveasfilename(filetypes=(('image', '*.jpg'), ('All', '*.*')),defaultextension='*.jpg')
            cv2.imwrite(file, re1)

        button3 = Button(window, text='Save', font=('Times_New_Roman', 12), bg='blue', foreground='white',command=save4)
        button3.place(x=580, y=255,width = 74,height = 31)

    img4 = PhotoImage(file=f"img4.png")
    b4 = Button(text="Gray", font="roboto 12 bold", relief="flat", bg="#007cc7", fg="#fff",command=fil4)
    b4.place(x=572, y=205,width=89,height=40)


window = Tk()
window.geometry("704x409")
window.configure(bg = "#FFFFFF")
window.title("Filter V0.1")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 409,
    width = 704,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")


canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    490.0, 292.0,
    image=background_img)


canvas.create_text(
    560.5, 63.0,
    text = "Filter",
    fill = "#ffffff",
    font = ("Gabriola", int(50.0)))



img5 = PhotoImage(file = f"img5.png")
select = Button(image = img5,borderwidth = 0,highlightthickness = 0,command = upload_file,relief = "flat")
select.place(x = 520, y = 328,width = 74,height = 31)


window.resizable(False, False)
window.mainloop()
