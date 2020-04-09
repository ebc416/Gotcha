import tkinter as tk
import time
import base64
import docx2txt
from tkinter.ttk import *
from tkinter import *
from tkinter import filedialog
from urllib.request import urlopen
from PIL import Image
import requests
from functions import pCheck
from functions import efrainspChecker



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


content = "tested"

def open_file1():
    file = filedialog.askopenfilename(title="Select File", filetypes=(("Word files", "*.docx"), ("Text files", "*.txt")))


    if file is not None:
        global content
        if file[-3:] == "ocx":
            content = docx2txt.process(file)
        elif file[-3:] == "txt":
            infile = open(file,'r')
            content = infile.read()


    T.configure(state=NORMAL)
    T.delete(0.0, "end")
    T.insert(0.0,content)
    T.configure(state=DISABLED)


content2 = "test"
def open_file2():
    file = filedialog.askopenfilename(title="Select File", filetypes= ( ("Word files", "*.docx"), ("Text files", "*.txt") ) )

    if file is not None:
        global content2
        if file[-3:] == "ocx":
            content2 = docx2txt.process(file)
        elif file[-3:] == "txt":
            infile = open(file,'r')
            content2 = infile.read()


    T2.configure(state=NORMAL)
    T2.delete(0.0, "end")
    T2.insert(0.0,content2)
    T2.configure(state=DISABLED)

btn3 = tk.Button(root,bottom_frame,text = "Import File", fg = "red",command=open_file1).pack(side = "right")
btn4 = tk.Button(root,bottom_frame,text = "Import File", fg = "green",command=open_file2).pack(side = "left")

def alert_popup(title, message):
    root2 = tk.Toplevel()
    canvas = tk.Canvas(root2,width = 925, height = 500, bg = 'white')
    canvas.pack(expand = YES, fill = BOTH)
    canvas.create_image(50, 50, image = logo2, anchor = NW)

    w = 400     # popup window width
    h = 200     # popup window height
    m = message
    m += '\n'
    w = Label(root2, text=m, width=69, height=5)
    w.pack()
    b = Button(root2, text="OK", command=root2.destroy, width=10)
    b.pack()
    mainloop()

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

    #S_value = pCheck(content,content2)
    #changes into new algo
    #S_value = pCheck(content,content2)
    S_value = efrainspChecker(content,content2)
    import time
    progress['value'] = S_value
    pDisplay = progress['value']
    DisplayM = Message(root, text = str(pDisplay)+"%")
    DisplayM.pack()
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = S_value
    pDisplay = progress['value']
    DisplayM.config(text = str(pDisplay)+"%")
    DisplayM.config(width=50)
    DisplayM.pack()
    if pDisplay == 100:
        alert_popup("Gottem!","100%  Plagiarism")

progress.pack(pady = 1,side = "top")

Button(root, text = 'Scan', command = bar).pack(pady = 10, side = "bottom")


tk.mainloop()
