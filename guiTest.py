import tkinter as tk
import time
#from tkinter import filedialog
from tkinter.ttk import *
from tkinter import *
from tkinter.filedialog import askopenfile

root = tk.Tk()
root.title("GOTCHA")
logo = tk.PhotoImage(file="Gotcha.png")
logo2 = tk.PhotoImage(file="FBI.gif")
#fileName2 = filedialog.askopenfilename()


top_frame = tk.Frame(root).pack()
bottom_frame = tk.Frame(root).pack(side = "bottom")

w1 = tk.Label(root, image=logo).pack(side="top",pady = 10)


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

def alert_popup(title, message):
    root2 = tk.Toplevel()
    canvas = tk.Canvas(root2,width = 300, height = 200, bg = 'white')
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'C:\\Users\\efrai\\Desktop\\Gotcha\\FBI.gif')
    canvas.create_image(50, 10, image = gif1, anchor = NW)
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
    root.update_idletasks()
    pDisplay = progress['value']
    DisplayM = Message(root, text = pDisplay)
    time.sleep(1)

    progress['value'] = 40
    root.update_idletasks()
    pDisplay = progress['value']
    DisplayM = Message(root, text = pDisplay)

    time.sleep(1)

    progress['value'] = 50
    root.update_idletasks()
    pDisplay = progress['value']
    DisplayM = Message(root, text = pDisplay)

    time.sleep(1)

    progress['value'] = 60
    root.update_idletasks()
    pDisplay = progress['value']
    DisplayM = Message(root, text = pDisplay)

    time.sleep(1)

    progress['value'] = 80
    root.update_idletasks()
    pDisplay = progress['value']
    DisplayM = Message(root, text = pDisplay)

    time.sleep(1)

    progress['value'] = 100
    pDisplay = progress['value']
    DisplayM = Message(root, text = pDisplay)
    DisplayM.config(width=50)
    DisplayM.pack()
    if pDisplay == 100:
        alert_popup("Gottem!","100%  Plagiarism")

progress.pack(pady = 1,side = "top")
# This button will initialize
# the progress bar
Button(root, text = 'Scan', command = bar).pack(pady = 10, side = "bottom")


tk.mainloop()
