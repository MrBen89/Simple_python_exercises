from tkinter import *

window = Tk()
window.title("My first GUI")
window.minsize(640, 480)
window.config(padx=20, pady=20)


input = Entry()
input.grid(row=0, column=1)

my_label = Label(text=" miles", font=("Arial", 24))
my_label.grid(row=0, column=2)

my_label2 = Label(text="is equal to", font=("Arial", 24))
my_label2.grid(row=1, column=0)

my_label3 = Label(text="0", font=("Arial", 24))
my_label3.grid(row=1, column=1)

my_label4 = Label(text="Km", font=("Arial", 24))
my_label4.grid(row=1, column=2)

def button_clicked():
    my_label3["text"] = round(int(input.get()) *1.60)

button = Button(text="Calculate", command= button_clicked)
button.grid(row=2, column=1)






window.mainloop()
