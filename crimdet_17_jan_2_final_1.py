# Python Program to find if the given face passed is present in the video clip passed and return the frame number.
import pandas as pd
import plotly.express as px
import cv2
import csv
import tkinter
from tkinter import *
from tkinter import Tk
import tkinter.font as font
from tkinter.filedialog import askopenfilename
import face_recognition
from PIL import ImageTk, Image
#import tkinter
import pandas
import csv
from tkinter import *
import face_recognition
from datetime import datetime
import numpy as np
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename
import pandas
import tkinter
from tkinter import ttk,messagebox,Frame
import pandas as pd
import plotly.express as px
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter.font as f
# Defining methods to input image file and object file
def img():
    global filename
    filename = askopenfilename()


def video():
    global filename1
    filename1 = askopenfilename()


def removeBracket(string):
    return string[1:len(string)-1]

# Code to design the input window
window = Tk()
window.geometry("1000x600")
lbl_port = tkinter.Label(window, text="Port", fg="green")
ent_port = tkinter.Entry(window)
buttonFont = font.Font(family='Times', size=16, weight='bold', slant="roman")
label1 = Label(window, text="Criminal Detection using Python Modules",
               fg="black", background='whitesmoke', font=buttonFont)
label1.pack()
image = ImageTk.PhotoImage(Image.open("car.jpg"))
limg = Label(window, i=image)
limg.pack()
buttonFont = font.Font(family='Helveltica', size=10,
                       weight='normal', slant="roman")
l = Button(window, text=" Choose the Image file ", command=img,
           font=buttonFont, background='aliceblue')
q = Button(window, text=" Choose the Video file ", command=video,
           font=buttonFont, background='aliceblue')
buttonFont = font.Font(family='Helveltica', size=13, weight='bold')
p = Button(window, text=" Click to continue ", command=window.destroy,
           font=buttonFont, background='deepskyblue', fg='white')
l.place(relx=0.5, rely=0.35, anchor=CENTER)
q.place(relx=0.5, rely=0.5, anchor=CENTER)
p.place(relx=0.5, rely=0.65, anchor=CENTER)
window.mainloop()

# Face Recognition part
unknown = face_recognition.load_image_file(filename)
vidcap = cv2.VideoCapture(filename1)
success, image = vidcap.read()
count = 0
while success:
    cv2.imwrite("frame%d.jpg" % count, image)
    success, image = vidcap.read()
    count += 1
pic = -1

# To write into a csv file
fields = ['FrameNo', 'PercentageMatch']
rows = []
percent_values = []
dec_values = []
# csvname = "framedata.csv"
# csvfile = open(csvname, 'w')
csvfile = open("framedata.csv","w")
csvfile.write("Status")
csvfile.write("\n")
# csvwriter.writerow(fields)
for i in range(count): # Iterates along all the frames of the video to find the match
    pic = i
    s = "frame{}.jpg".format(i)
    known = face_recognition.load_image_file(s)
    try:
        known_encoding = face_recognition.face_encodings(known)[0]
    except:
        csvfile.write("Not detected")
        csvfile.write("\n")
        continue
    unknown_encoding = face_recognition.face_encodings(unknown)[0]
    result = face_recognition.compare_faces([known_encoding], unknown_encoding)
    face_distances = face_recognition.face_distance([known_encoding], unknown_encoding)
    element = [str(i), round(float(removeBracket(str(face_distances))), 2)]
    dec_values.append(element[1])
    percent_values.append(face_distances)
    rows.append(element)
    # csvwriter.writerow(element)
    print(element)
    if element[0] :
        csvfile.write("detected")
    else:
        csvfile.write("Not detected")
    csvfile.write("\n")
   

csvfile.close()

m = max(dec_values)

df = pd.read_csv('framedata.csv')
# fig = px.scatter(df, x = 'FrameNo', y = 'PercentageMatch', color = 'PercentageMatch', title = 'Frame number v/s Percentage of Match')
# fig.show()
fig2 = px.pie(df,values = 'Status')
fig2.write_image("File.jpg")





def timestamp():
    cap = cv2.VideoCapture(filename1)
    global framespersecond
    framespersecond = int(cap.get(cv2.CAP_PROP_FPS))
    # print(framespersecond)

timestamp()

# Code to design output window
def screen_time():
    window1.destroy()
    global root
    root=Tk()
    h=pd.read_csv('framedata.csv')
    df=pd.read_csv("framedata.csv")
    root.geometry("1000x600")
    root.title("Welcome Student")
    k=Label(root,text='hi').place(x=900,y=900,anchor ='ne')
    root['background']='skyblue'
    bfont1 = f.Font(family='Courier', slant = 'italic', size = 25)
    l=Label(root,text="Screen-time",font=bfont1,bg='skyblue')
    l.place(x=400,y=20)
    l.pack()
    bfont1 = f.Font(family='Courier', slant = 'italic', size = 10)
    m=Label(root,text="The Screen-time is {}".format(df['Status'].value_counts()['detected']/(framespersecond)),font=bfont1,bg='skyblue')
    m.place(x=400,y=100)
    m.pack()
    df=pd.read_csv("framedata.csv")
    fig = px.pie(df, title='Screen-time', names='Status')
    fig.write_image("fig1.jpg")
    print('end')
    image = Image.open('fig1.jpg')
    new_image = image.resize((600,600))
    new_image.save('fig1.jpg')

        # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("fig1.jpg"))

        #Create a Label Widget to display the text or Image
    label = Label(root, image = img,height=600,width=600)
    label.image=img
    label.place(x=400,y=500)
    label.pack()
    btn=Button(root, text="Get Back to detection page",command=we1)
    btn.place(relx=0.5,rely=0.2,anchor=CENTER)
    root.mainloop()
def normi():
    window1.destroy()
    global root
    df=pd.read_csv("framedata.csv")
    pic=len(df)
    for i in range(pic):
        if(rows[i][1] == m):
            print('Image found at {} frame.'.format(i))
            print("Frame rate: {}".format(framespersecond))
            print("Time stamp: {}".format(round(i/framespersecond, 2)))
            print("Percentage Match: {}".format(m))
            root = Tk()
            root.title("Image Found!!")
            root.geometry("400x600+200+200")
            bg = ImageTk.PhotoImage(Image.open(r"frame{}.jpg".format(i)))
            label1 = Label(root, image=bg)
            label1.place(relx=0.5, rely=0.5, anchor=CENTER)
            btn=Button(root, text="Get Back to detection page" ,command=we1)
            btn.place(relx=0.5,rely=0.6,anchor=CENTER)
            buttonFont = font.Font(family='Helveltica', size=9, weight='bold')
            l = Label(root, text='Image found at {} frame.'.format(i), width=25,height=2, background='black', fg='white', font=buttonFont)
            l.place(relx=0.5, rely=0.9, anchor=CENTER)
            f = Label(root, text='Frame Timestamp: {}'.format(round(i/framespersecond, 2)),width=30, height=2, background='black', fg='white', font=buttonFont)
            f.place(relx=0.5, rely=0.8, anchor=CENTER)
            k = Label(root, text='Percentage Match: {}'.format(m),width=30, height=2, background='black', fg='white',font=buttonFont)
            k.place(relx=0.5, rely=0.7, anchor=CENTER)
            root.mainloop()
            break
# print("Length of dec_values : {}".format(len(dec_values)))
                
# print("Percentage Match: {}".format(dec_values[pic - 1]))
if (result):
    pass
else:
    print('Image not found!')
def maxi():
    global root
    window1.destroy()
    df=pd.read_csv("framedata.csv")
    pic=len(df)
    for i in range(pic):
        if(rows[i][1] == max(dec_values)):
            print('Image found at {} frame.'.format(i))
            print("Frame rate: {}".format(framespersecond))
            print("Time stamp: {}".format(round(i/framespersecond, 2)))
            print("Percentage Match: {}".format(m))
            root = Tk()
            root.title("Image Found!!")
            root.geometry("400x600+200+200")
            bg = ImageTk.PhotoImage(Image.open(r"frame{}.jpg".format(i)))
            label1 = Label(root, image=bg)
            label1.place(relx=0.5, rely=0.5, anchor=CENTER)
            btn=Button(root, text="Get Back to detection page" ,command=we1)
            btn.place(relx=0.5,rely=0.6,anchor=CENTER)
            buttonFont = font.Font(family='Helveltica', size=9, weight='bold')
            l = Label(root, text='Image found at {} frame.'.format(i), width=25,height=2, background='black', fg='white', font=buttonFont)
            l.place(relx=0.5, rely=0.9, anchor=CENTER)
            f = Label(root, text='Frame Timestamp: {} '.format(round(i/framespersecond, 2)),width=30, height=2, background='black', fg='white', font=buttonFont)
            f.place(relx=0.5, rely=0.8, anchor=CENTER)
            k = Label(root, text='Percentage Match: {} '.format(m),    width=30, height=2, background='black', fg='white',font=buttonFont)
            k.place(relx=0.5, rely=0.7, anchor=CENTER)
            root.mainloop()
            break
global we1
def we1():
    root.destroy()
    we()
global we
def we():
    global window1
    window1 = Tk()
    window1.geometry("1000x600")
    lbl_port = tkinter.Label(window1, text="Port", fg="green")
    ent_port = tkinter.Entry(window1)
    buttonFont = font.Font(family='Times', size=16, weight='bold', slant="roman")
    label1 = Label(window1, text="Criminal Detection using Python Modules",
                   fg="black", background='whitesmoke', font=buttonFont)
    label1.pack()
    image = ImageTk.PhotoImage(Image.open("car.jpg"))
    limg = Label(window1, i=image)
    limg.pack()
    buttonFont = font.Font(family='Helveltica', size=13,
                           weight='normal', slant="roman")
    l = Button(window1, text=" Detect-face ", command=normi,
               font=buttonFont, background='aliceblue')
    q = Button(window1, text=" Detect-max-match face ", command=maxi,
               font=buttonFont, background='aliceblue')
    buttonFont = font.Font(family='Helveltica', size=13, weight='bold')
    p = Button(window1, text=" Detect screen time ", command=screen_time,
               font=buttonFont, background='deepskyblue', fg='white')
    l.place(relx=0.5, rely=0.35, anchor=CENTER)
    q.place(relx=0.5, rely=0.5, anchor=CENTER)
    p.place(relx=0.5, rely=0.65, anchor=CENTER)
    window1.mainloop()
we()
