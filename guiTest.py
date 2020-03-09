import tkinter as tk
import time
import base64
#from tkinter import filedialog
from tkinter.ttk import *
from tkinter import *
from tkinter.filedialog import askopenfile
from urllib.request import urlopen
from PIL import Image
import requests


root = tk.Tk()
root.title("GOTCHA")
url = "https://i.imgur.com/HZCR1G2.png"
url2 = "https://i.imgur.com/ElKpHkG.png"

respond = requests.get(url2)
img_byt = urlopen(url2).read()
img_b64 = base64.encodestring(img_byt)
logo = tk.PhotoImage(data = img_b64)

response = requests.get(url)
image_bt = urlopen(url).read()
image_FBI = base64.encodestring(image_bt)
logo2 = tk.PhotoImage(data = image_FBI)


top_frame = tk.Frame(root).pack()
bottom_frame = tk.Frame(root).pack(side = "bottom")

w1 = tk.Label(root, image = logo).pack(side="top",pady = 10)


T = tk.Text(root, height=10, width=30,borderwidth = 2, relief="groove")
T.pack(side=tk.RIGHT,padx=10)

T2 = tk.Text(root, height=10, width=30,borderwidth = 2, relief="groove")
T2.pack(side=tk.LEFT, padx=10)

#def UploadAction():filename = filedialog.askopenfilename()

def open_file1():
    file = askopenfile(mode ='r', filetypes =[('Text files', '*.txt')])
    if file is not None:
        content = file.read()
        #print(content)
    T.configure(state=NORMAL)
    T.delete(0.0, "end")
    T.insert(0.0,content)
    T.configure(state=DISABLED)

def open_file2():
    file = askopenfile(mode ='r', filetypes =[('Text files', '*.txt')])
    if file is not None:
        content = file.read()
        #print(content)
    T2.configure(state=NORMAL)
    T2.delete(0.0, "end")
    T2.insert(0.0,content)
    T2.configure(state=DISABLED)

btn3 = tk.Button(root,bottom_frame,text = "Import File", fg = "red",command=open_file1).pack(side = "right")
btn4 = tk.Button(root,bottom_frame,text = "Import File", fg = "green",command=open_file2).pack(side = "left")
#/Users/khoale/Documents/GitHub/Gotcha
def alert_popup(title, message):
    root2 = tk.Toplevel()
    canvas = tk.Canvas(root2,width = 925, height = 500, bg = 'white')
    canvas.pack(expand = YES, fill = BOTH)
    canvas.create_image(50, 50, image = logo2, anchor = NW)
    #popGif = tk.Label(root2, image=logo2).pack(side="top",pady = 10)
    w = 400     # popup window width
    h = 200     # popup window height
    m = message
    m += '\n'
    w = Label(root2, text=m, width=69, height=5)
    w.pack()
    b = Button(root2, text="OK", command=root2.destroy, width=10)
    b.pack()
    mainloop()

#widget_object = Progressbar(parent, **options)
# Progress bar widget
pDisplay ='Plagiarism Percentage'
DisplayM = Message(root, text = pDisplay)
DisplayM.config(bg='lightgreen',width=200)
DisplayM.pack(side = "top")

progress = Progressbar(root, orient = HORIZONTAL,
              length = 200, mode = 'determinate')
# Function responsible for the updation
# of the progress bar value

def bar():
    import time
    progress['value'] = 20
    pDisplay = progress['value']
    DisplayM = Message(root, text = pDisplay)
    DisplayM.pack()
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 40
    pDisplay = progress['value']
    DisplayM.config(text = pDisplay)
    DisplayM.pack()
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 50
    pDisplay = progress['value']
    DisplayM.config(text = pDisplay)
    DisplayM.pack()
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 60
    pDisplay = progress['value']
    DisplayM.config(text = pDisplay)
    DisplayM.pack()
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 80
    pDisplay = progress['value']
    DisplayM.config(text = pDisplay)
    DisplayM.pack()
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 100
    pDisplay = progress['value']
    DisplayM.config(text = pDisplay)
    DisplayM.config(width=50)
    DisplayM.pack()
    if pDisplay == 100:
        alert_popup("Gottem!","100%  Plagiarism")

progress.pack(pady = 1,side = "top")
# This button will initialize
# the progress bar
Button(root, text = 'Scan', command = bar).pack(pady = 10, side = "bottom")


tk.mainloop()
