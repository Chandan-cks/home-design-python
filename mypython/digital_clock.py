from tkinter import Label,Tk
import time

#import tkinter and time
app =Tk()
#load window 
app.title("Digital clock")
app.geometry("420x150")
app.resizable(1,1)
#geometry resize
text_font=("Boulder",68,'bold')
background="#f2e750"
foreground="#363529"
border_width=25
#color width and color
label=Label(app,font=text_font,
bg=background,fg=foreground,
bd=border_width)
label.grid(row=0,column=1)
#grid show time
def digital_clock():
    time_live=time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200,digital_clock)
#function to check live time 
digital_clock()

app.mainloop()
