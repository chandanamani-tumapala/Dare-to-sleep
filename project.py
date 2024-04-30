from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from captcha.image import ImageCaptcha
import datetime
from pygame import mixer
import random
import string
mixer.init()

root=Tk()
root.geometry("600x429")
background_frame=Frame(root,bg="#05ACD3")
background_2=Frame(root,bg="#05ACD3")
background_2.pack(fill=BOTH)
#global declaration of images used
background=ImageTk.PhotoImage(Image.open("C:/Users/niran/OneDrive/Desktop/background.jpg"))
submit_clock=ImageTk.PhotoImage(Image.open("C:/Users/niran/OneDrive/Desktop/submit_clock.jpg"))
imcolor=Image.open("C:/Users/niran/OneDrive/Desktop/imcolor.jpg")
img_color=ImageTk.PhotoImage(imcolor)
calculate=Image.open("C:/Users/niran/OneDrive/Desktop/calculate.jpg")
img_calculate=ImageTk.PhotoImage(calculate)
text=Image.open("C:/Users/niran/OneDrive/Desktop/text.jpg")
img_text=ImageTk.PhotoImage(text)
imcaptcha=Image.open("C:/Users/niran/OneDrive/Desktop/imcaptcha.jpg")
img_captha=ImageTk.PhotoImage(imcaptcha)
frame1=Frame(background_frame,bg="white",borderwidth=2)
frame2=Frame(background_frame,bg="#05ACD3",borderwidth=5)
nextback=Frame(frame1,bg="#05ACD3",borderwidth=3)
frame3=Frame(nextback,bg="white",borderwidth=2)
frame4=Frame(background_frame,bg="#05ACD3")
button_frame=Frame(background_frame,bg="white")
hours_variable=StringVar()
minutes_variable=StringVar()
seconds_variable=StringVar()
hours_entry=Entry(frame2,textvariable=hours_variable) 
minutes_entry=Entry(frame2,textvariable=minutes_variable) 
seconds_entry=Entry(frame2,textvariable=seconds_variable) 
hours=Label(frame2,text="Hrs",fg="white",bg="#05ACD3",font=("Lucida Bright",20))
minutes=Label(frame2 ,text="Min",fg="white",bg="#05ACD3",font=("Lucida Bright",20))
seconds=Label(frame2 ,text="Sec",fg="white",bg="#05ACD3",font=("Lucida Bright",20))
nextback.pack()
frame1.pack()
frame3.pack()
frame4.pack()
frame2.pack()
label1=Label(frame3,text="Set your alarm",bg="#05ACD3",fg="white",font=("Lucida Bright",30))
plane_lable=Label(frame4,text="\n\n",bg="#05ACD3")
def condition(dis,ent):
    t=ent.get()
    if(str(dis)==str(t)):
        mixer.music.pause()
        root.destroy()
    else:
        messagebox.showwarning("Warning","Try again")

def clearall():
    button_label.destroy()
    for buttons in background_2.winfo_children():
        buttons.destroy()
def color():
    root.geometry("400x600")
    clearall()
    l=['red','black','grey','green','blue','pink','yellow','orange','white']
    color_label=Label(background_2,text="Identify the color",bg="#05ACD3",fg="white",font=("Lucida Bright",30),padx=10,pady=50)
    color_label.grid(row=1,column=15)
    can_widget=Canvas(background_2,bg="#05ACD3",width='300',height='300')
    can_widget.grid(row=2,column=15)
    k=random.choice(l)
    can_widget.create_oval(50,50,250,250,fill=k)
    color_variable=StringVar()
    color_entry=Entry(background_2,textvariable=color_variable)
    color_entry.grid(row=5,column=15,pady=10)
    sub_forcolor=Button(background_2,text="Submit",anchor="s",command=lambda: condition(k,color_variable))
    sub_forcolor.grid(row=6,column=15,pady=10)
def solve_problem():
    clearall()
    root.geometry("400x500")
    problem_label=Label(background_2,text="Solve the Problem",bg="#05ACD3",fg="white",font=("Lucida Bright",30),highlightbackground="white",highlightcolor="white",highlightthickness=3)
    problem_label.grid(row=1,column=15,padx=10,pady=10)
    k1=random.randint(10000,99999)
    k2=random.randint(10000,99999)
    string1=Label(background_2,text=str(k1),bg="#05ACD3",fg="white",font=("Lucida Bright",15),highlightbackground="white",highlightcolor="white",highlightthickness=3)
    string1.grid(row=2,column=15,padx=10,pady=10)
    plus=Label(background_2,text="+",bg="#05ACD3",fg="white",font=("Lucida Bright",15),padx=10,pady=10)
    plus.grid(row=3,column=15)
    string2=Label(background_2,text=str(k2),bg="#05ACD3",fg="white",font=("Lucida Bright",15),highlightbackground="white",highlightcolor="white",highlightthickness=3)
    string2.grid(row=4,column=15,padx=10,pady=10)
    sumof=k1+k2
    solve_variable=IntVar()
    solve_entry=Entry(background_2,textvariable=solve_variable)
    solve_entry.grid(row=5,column=15,pady=10)
    sub_forprob=Button(background_2,text="Submit",anchor="s",command=lambda: condition(sumof,solve_variable))
    sub_forprob.grid(row=6,column=15,pady=10)
def captcha():
    global photo_of_captcha
    clearall()
    captcha_label=Label(background_2,text="Enter the captcha",bg="#05ACD3",fg="white",font=("Lucida Bright",30),padx=10,pady=50)
    captcha_label.grid(row=1,column=30)
    image=ImageCaptcha(width=280,height=90)
    s=7
    captcha_text="".join(random.choices(string.ascii_uppercase+string.digits,k=s))
    data=image.generate(captcha_text)
    print(captcha_text)
    image.write(captcha_text,"CAPTCHA.png")
    root.geometry("500x300")
    image1 = Image.open("CAPTCHA.png")
    photo_of_captcha = ImageTk.PhotoImage(image1)
    label=Label(background_2,image=photo_of_captcha)
    label.grid(row=2,column=30,pady=10)
    captcha_variable=StringVar()
    captcha_entry=Entry(background_2,textvariable=captcha_variable)
    captcha_entry.grid(row=5,column=30,pady=10)
    sub_forprob=Button(background_2,text="Submit",anchor="s",command=lambda: condition(captcha_text,captcha_variable))
    sub_forprob.grid(row=6,column=30,pady=10)

def textit():
    clearall()
    text_label=Label(background_2,text="Rewrite the Text",bg="#05ACD3",fg="white",font=("Lucida Bright",30),highlightbackground="white",highlightcolor="white",highlightthickness=3)
    text_label.grid(row=1,column=15,padx=10,pady=10)
    root.geometry("900x320")
    l=['Python is a multi-paradigm programming language.',
    'Python, a dynamically typed language,eliminating hard rules for building features\n and offering more problem-solving flexibility with a variety of methods.',
    'Python is a widely used general-purpose, high level programming language.',
    "True love - that is, deep, abiding love that is impervious to emotional whims or fancy - is a choice.",
    "I really enjoyed getting to know you but if I'm honest,\n I'm not feeling a real connection between us.\n It was lovely meeting you."]
    string=random.choice(l)
    f_label=Label(background_2,text=string,bg="#05ACD3",fg="white",font=("Lucida Bright",15),highlightbackground="white",highlightcolor="white",highlightthickness=3)
    f_label.grid(row=5,column=15,padx=10,pady=10)
    text_variable=StringVar()
    text_entry=Entry(background_2,textvariable=text_variable,width=100)
    text_entry.grid(row=7,column=15,padx=10)
    sub_fortext=Button(background_2,text="Submit",anchor="s",command=lambda: condition(string,text_variable))
    sub_fortext.grid(row=10,column=15,padx=10)



button_label=Label(background_2,text="Select one option to off the alarm",bg="#05ACD3",fg="white",font=("Lucida Bright",30),padx=10,pady=50)
button_forcolor=Button(background_2,bg="white",fg="#05ACD3",text="Identify the color",image=img_color,compound=LEFT,font=("Lucida Bright",20),command=color,width=500,padx=10,pady=10)
button_problemsolve=Button(background_2,bg="white",fg="#05ACD3",text="solve it",image=img_calculate,compound=LEFT,font=("Lucida Bright",20),command=solve_problem,width=500,padx=10,pady=10)
button_captcha=Button(background_2,bg="white",fg="#05ACD3",text="Enter the Captcha",image=img_captha,compound=LEFT,font=("Lucida Bright",20),command=captcha,width=500,padx=10,pady=10)
button_textit=Button(background_2,bg="white",fg="#05ACD3",text="Can you Type",image=img_text,compound=LEFT,font=("Lucida Bright",20),command=textit,width=500,padx=10,pady=10)
def settype():
    root.geometry("700x500")
    i=2
    button_label.grid(row=1)
    for buttons in background_2.winfo_children():
        buttons.grid(row=i)
        i+=1
    mixer.music.load("C:/Users/niran/Downloads/Mahabharat ! bgm.mp3")
    mixer.music.play()
    
def check():
    if(int(hours_variable.get())<=24 or int(minutes_variable.get())<=60 or int(seconds_variable.get())<=60 or int(hours_variable.get())>=0 or int(minutes_variable.get())>=0 or int(seconds_variable.get())>=0):
        i=5
        for keys in background_frame.winfo_children():
            keys.destroy()
        button_label.grid(row=1)
        for buttons in background_2.winfo_children():
            i=i+1
            buttons.grid(row=i)
        n=1
        while(n==1):
            set_alarm_time=f"{hours_variable.get()}:{minutes_variable.get()}:{seconds_variable.get()}"
            current_time=datetime.datetime.now().strftime("%H:%M:%S")
            if(current_time==set_alarm_time):
                settype()
                break
    else:
        messagebox.showwarning("Warning","Enter correct time")
submit_time=Button(background_frame,image=submit_clock,anchor='e',command=check)

    
def setalarm():
    button1.destroy()
    root.geometry("500x450")
    background_frame.pack(fill=BOTH)
    label1.pack(fill=X)
    plane_lable.pack(fill=X)
    hours.grid(row=10,column=2)
    hours_entry.grid(row=11,column=2,padx=10)
    minutes.grid(row=10,column=6)
    minutes_entry.grid(row=11,column=6,padx=10)
    seconds.grid(row=10,column=10)
    seconds_entry.grid(row=11,column=10,padx=10)
    submit_time.pack()
button1=Button(root,image=background,command=setalarm)
button1.pack(fill=BOTH)
root.mainloop()