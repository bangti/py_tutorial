from tkinter import *

window = Tk()

photo = PhotoImage(file='person.png')

label = Label(window,
              text="bro, do you even code?",
              font=('Arial',40,'bold'),
              fg='#00FF00',
              background='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
label.pack()
# label.place(x=0,y=0)

window.mainloop()


