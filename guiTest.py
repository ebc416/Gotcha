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
from functions import read_report
from functions import documentSimilarity
from functions import stats
from functions import highlight




root = tk.Tk()
root.title("GOTCHA")
root.geometry("880x600")
root.resizable(0,0)
url = "https://i.imgur.com/HZCR1G2.png"
url2 = "https://i.imgur.com/yzNki6P.png"

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


w1 = tk.Label(root, image = logo,relief = "raised").pack(side="top",pady = 10)

T = tk.Text(root,top_frame,height=15, width=38,borderwidth = 2, relief="groove")
T.pack(side=tk.RIGHT,padx=10)

T2 = tk.Text(root,top_frame, height=15, width=38,borderwidth = 2, relief="groove")
T2.pack(side=tk.LEFT, padx=10)

T3 = tk.Text(root,bottom_frame,height=5,width=30,borderwidth = 2, relief="ridge")
T3.pack(side=tk.BOTTOM,pady=5)

T3.insert(1.0,"          Statistics:\n")
T3.configure(state=DISABLED)

content = None
fileone = None
filesec = None

def open_file1():
    global fileone
    fileone = filedialog.askopenfilename(title="Select File", filetypes=(("Word files", "*.docx"), ("Text files", "*.txt")))


    if fileone is not None:
        global content
        if fileone[-3:] == "ocx":
            content = docx2txt.process(fileone)
        elif fileone[-3:] == "txt":
            infile = open(fileone,'r')
            content = infile.read()


    T.configure(state=NORMAL)
    T.delete(0.0, "end")
    T.insert(0.0,content)


content2 = None

def open_file2():
    global filesec
    filesec = filedialog.askopenfilename(title="Select File", filetypes= ( ("Word files", "*.docx"), ("Text files", "*.txt") ) )

    if filesec is not None:
        global content2
        if filesec[-3:] == "ocx":
            content2 = docx2txt.process(filesec)
        elif filesec[-3:] == "txt":
            infile = open(filesec,'r')
            content2 = infile.read()


    T2.configure(state=NORMAL)
    T2.delete(0.0, "end")
    T2.insert(0.0,content2)
    T2.configure(state=NORMAL)

btn3 = tk.Button(root,bottom_frame,text = "Import File",relief = "raised", fg = "red",command=open_file1).pack(side = "right")
btn4 = tk.Button(root,bottom_frame,text = "Import File",relief = "raised", fg = "green",command=open_file2).pack(side = "left")

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
ptDisplay ='Plagiarism Percentage'
DisplayM = Message(root, text = ptDisplay)
DisplayM.config(bg='lightgreen',width=200,relief="raised")
DisplayM.pack(side = "top")

progress = Progressbar(root, orient = HORIZONTAL,
              length = 200, mode = 'determinate')
# Function responsible for the updation
# of the progress bar value
global scoreTracker
scoreTracker = StringVar()
scoreTracker.set("0%")
global DisplayMsg
DisplayMsg = Label(root,textvariable = scoreTracker)


def bar():
    read_report(fileone,filesec)
      #open similarFile and read line by line removing \n to search in our two text files
    with open("real_similarities.txt") as similarFile:
        sequence = similarFile.readlines()
        for line in sequence:
            highlight(T,line.strip())
            highlight(T2,line.strip())
            #print(line.strip())
    similarFile.close()

    if fileone != None:
        #global DisplayMsg
        #S_value = pCheck(content,content2)
        #changes into new algo
        #S_value = pCheck(content,content2)
        S_value = efrainspChecker(content,content2)
        progress['value'] = S_value
        pDisplay = progress['value']
        scoreTracker.set(str(pDisplay)+"%")
        #DisplayMsg = Label(root, textvariable = scoreTracker)
        DisplayMsg.pack(pady = 10,side = "top")
        root.update_idletasks()

        loadIn = stats(content)
        T3.configure(state=NORMAL)
        #T3.delete(0.0, "end")
        T3.insert(2.0,"Right-Side File\n")
        T3.insert(3.0,loadIn)
        loadIn2 = stats(content2)
        T3.insert(8.0,"\nLeft-Side File\n")
        T3.insert(9.0,loadIn2)
        T3.configure(state=DISABLED)

        if pDisplay == 100:
            alert_popup("Gottem!","100%  Plagiarism")

progress.pack(pady = 1,side = "top")

def Clear():
    global content, content2,fileone,filesec
    content = None
    content2 = None
    fileone = None
    filesec = None
    T.delete("1.0","end")
    T.update()
    T2.delete("1.0","end")
    T2.update()
    T3.configure(state = NORMAL)
    T3.delete("2.0","end")
    T3.update()
    T3.configure(state = DISABLED)
    progress['value'] = 0
    pDisplay = progress['value']
    if pDisplay == 0:
        scoreTracker.set("")
    elif content != None:
        scoreTracker.set(str(pDisplay)+"%")
    root.update_idletasks()

Button(root, text = 'Scan', command = bar).pack(pady = 10, side = "bottom")
Button(root, text = 'Clear', command = Clear).pack(pady = 25,side = "bottom")

tk.mainloop()
