import tkinter as tk
from tkinter import filedialog
from tkinter import *

root = tk.Tk()
root.title("GOTCHA")
logo = tk.PhotoImage(file="Gotcha.png")
#fileName2 = filedialog.askopenfilename()


top_frame = tk.Frame(root).pack()
bottom_frame = tk.Frame(root).pack(side = "bottom")

w1 = tk.Label(root, image=logo).pack(side="top")
text1 = "None"

def UploadAction():
    fN = filedialog.askopenfilename()
    fN2 = open(fN, "r")

    text1 = fN2.read()

    fN2.close()

btn3 = tk.Button(root,bottom_frame,text = "Import File", fg = "red",command=UploadAction).pack(side = "right")

btn4 = tk.Button(root,bottom_frame,text = "Import File", fg = "green",command=UploadAction).pack(side = "left")

T = tk.Text(root, height=10, width=30,borderwidth = 2, relief="groove")
T.pack(side=tk.RIGHT,padx=10)

T.insert(tk.END, text1)

T2 = tk.Text(root, height=10, width=30,borderwidth = 2, relief="groove")
T2.pack(side=tk.LEFT, padx=10)

T2.insert(tk.END, text1)



tk.mainloop()
