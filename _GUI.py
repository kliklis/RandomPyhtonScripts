from tkinter import *



window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('600x800')

lbl = Label(window, text="Hello", font=("Arial", 20))
 
lbl.grid(column=0, row=0)

txt = Entry(window,width=10)
txt.grid(column=1, row=1)
txt.insert(0,'username')
txt.bind("<FocusIn>", lambda args: txt.delete('0', 'end'))



txt2 = Entry(window,width=10)
txt2.grid(column=1, row=2)


def clicked():
    if(txt.get() == 'k' and txt2.get() == 'k'):
        lbl.configure(text="You are in!")#text=txt.get())
    else:
        lbl.configure(text="Wrong credentials!")



btn = Button(window, text="Click Me", command=clicked).grid(column=1, row=0)

 
window.mainloop()



'''from tkinter import *
 
from tkinter.ttk import *
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')
 
combo = Combobox(window)
 
combo['values']= (1, 2, 3, 4, 5, "Text")
 
combo.current(1) #set the selected item
 
combo.grid(column=0, row=0)

#combo.get()
 
window.mainloop()'''

'''from tkinter import *
 
from tkinter.ttk import *
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')
 
chk_state = BooleanVar()
 
chk_state.set(False) #set check state
 
chk = Checkbutton(window, text='Choose', var=chk_state)
 
chk.grid(column=0, row=0)
 
window.mainloop()'''


'''from tkinter import *
 
from tkinter.ttk import *
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')
 
rad1 = Radiobutton(window,text='First', value=1)
rad2 = Radiobutton(window,text='Second', value=2)
rad3 = Radiobutton(window,text='Third', value=3)
 
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
 
window.mainloop()'''


'''from tkinter import *
 
from tkinter import scrolledtext
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')

txt = scrolledtext.ScrolledText(window,width=40,height=10)
txt.insert(INSERT,'You text goes here')
txt.grid(column=0,row=0)
#txt.delete(1.0,END)
 
window.mainloop()'''


'''from tkinter import *
 
from tkinter import messagebox
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')
 
def clicked():
 
    messagebox.showinfo('Message title', 'Message content')
 
btn = Button(window,text='Click here', command=clicked)
 
btn.grid(column=0,row=0)
 
window.mainloop()'''




