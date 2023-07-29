from tkinter import *

from tkcalendar import *
cl= Tk()
cl.geometry('700x425') #Selecting calendar display size

#this command will basically automatically select the written date whenever we run code
caal = Calendar(cl,selectmode='day',year=2023,month=7,day=29)

caal.pack(pady=25)
#defining function for selecting date
def pick_date():
    my_label.config(text="Selected Date Is  " + caal.get_date())
but= Button(cl, text='Show Date',command=pick_date) # This coomand creating "show date" named button 
but.pack(pady=25)

my_label= Label(cl,text="") # this command is giving label for showing selected date
my_label.pack(pady=25)

cl.mainloop()