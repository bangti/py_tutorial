from tkinter import *

def submit():
    print("The temperature is: "+str(scale.get())+" degrees C")

window = Tk()

hotImage = PhotoImage(file='fire.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient="vertical",
              font=('Consolas',20),
              tickinterval=10,
            #   showvalue=0,
              resolution=5,
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg='#111111')
scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()

iceImage = PhotoImage(file='ice.png')
iceLabel = Label(image=iceImage)
iceLabel.pack()

button = Button(window,
                text='submit',
                command=submit)
button.pack()

window.mainloop()


