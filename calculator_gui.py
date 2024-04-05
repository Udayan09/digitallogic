from tkinter import *
import digitallogic

def button_task(val1,val2, option, type):
    
    if type == "Bin":
        v1 = digitallogic.createbin(val1)
        v2 = digitallogic.createbin(val2)
        if option == "AND":
            v3 = digitallogic.binary_and(v1,v2)
        elif option == "OR":
            v3 = digitallogic.binary_or(v1,v2)
        else:
            v3 = digitallogic.binary_xor(v1,v2)
    else:
        v1 = digitallogic.createhex(val1)
        v2 = digitallogic.createhex(val2)
        if option == "AND":
            v3 = digitallogic.hex_and(v1,v2)
        elif option == "OR":
            v3 = digitallogic.hex_or(v1,v2)
        else:
            v3 = digitallogic.hex_xor(v1,v2)
    l4.config(text="Result: "+v3.value)

window = Tk()
window.title("Calculator")
window.geometry("430x200")

l2 = Label(window, text="Value 1: ",font = ("Arial",12),  height=2,width=8)
l3 = Label(window, text="Value 2: ",font = ("Arial",12),  height=2,width=8)
l5 = Label(window, text = "Operation: ", font = ("Arial",12),  height=2,width=10)

v1 = StringVar()
v2 = StringVar()
data_type1 = StringVar()
data_type1.set(" ")
dd_select_option = StringVar()
dd_select_option.set("AND")

e1 = Entry(window, textvariable = v1, width=15)
e2 = Entry(window, textvariable = v2, width=15)

dd_options = ["AND","OR","XOR"]

dd1 = OptionMenu(window,dd_select_option, *dd_options)
dd1.grid(row=2,column=1,columnspan=2)

l2.grid(row=0,column=0)
l3.grid(row=0,column=2)
l5.grid(row=2,column=0)
e1.grid(row=0,column=1)
e2.grid(row=0,column=3)

rb1 = Radiobutton(window, text = "Binary", variable = data_type1, value = "Bin")
rb2 = Radiobutton(window, text = "Hex", variable = data_type1, value = "Hex")

rb1.grid(row=1,column=1,sticky="e",padx=2)
rb2.grid(row=1,column=2, sticky="w",padx=2)

l4 = Label(window, text="Result",font = ("Arial",15),  height=2,width=20)
l4.grid(row=4,column=1,columnspan=2)

b1 = Button(window,text="Calculate",height=2,width=20,command=lambda: button_task(v1.get(), v2.get(),dd_select_option.get(),data_type1.get()))
b1.grid(row=3,column=1,columnspan=2,pady=5)



window.mainloop()

