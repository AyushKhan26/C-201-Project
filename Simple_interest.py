from tkinter import *

window = Tk()

def calculate():
    p = float(principal_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())
    i= p*r*t/100
    interest= round(i,2)

    showLabel.destroy()

    output_message = Label(result_frame,text='Your interest is '+ str(i) + ' RS ',bg='cyan',font=('Calibri',12),width=42) 
    output_message.place(x=20,y=40)
    output_message.pack()


window.title('SIMPLE INTEREST CALCULATOR')
window.geometry('400x400')
window.configure(bg= 'blue')

header_label = Label(window,text='SIMPLE INTEREST CALCULATOR',fg ='black',bg='yellow')
header_label.place(x= 100,y=20)

principal_label = Label(window,text='Principal',fg ='black',bg='yellow')
principal_label.place(x= 50,y= 120)

principal_entry = Entry(window,text='1')
principal_entry.place(x=150,y=120)

rate_label = Label(window,text='Rate of interest',fg ='black',bg='yellow')
rate_label.place(x=50,y=150)

rate_entry = Entry(window,text='2')
rate_entry.place(x=150,y=150)

time_label = Label(window,text='Time',fg ='black',bg='yellow')
time_label.place(x=50,y=180)

time_entry = Entry(window,text='3')
time_entry.place(x=150,y=180)

calculate_button = Button(window,text='Calculate',fg='black',bg='orange',command=calculate,width=10,height=2)
calculate_button.place(x=100,y=300)

result_frame = LabelFrame(window,text='Result',bg = 'grey',font=('Calibri',12),width=55)
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

showLabel = LabelFrame(window,text='Your Result will be displayed here',bg = 'grey',font=('Calibri',12),width=55)
showLabel.place(x=20,y=20)
showLabel.pack()

window.mainloop()



