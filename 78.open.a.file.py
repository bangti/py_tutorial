from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir='D:\\study\\python\\py_tutorial',
                                          title='open file okay?',
                                          filetypes=(("text files","*.txt"),
                                                     ("all files","*.*")))
    # print(filepath)
    file = open(filepath, 'r')
    print(file.read())
    file.close()

window = Tk()

button = Button(text="open",command=openFile)
button.pack()

window.mainloop()


