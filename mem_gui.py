from tkinter import *
from tkinter import ttk
import memory_code

window = Tk()
window.title("Memeory")
window.geometry("800x670")

table_frame = Frame(window)
table_frame.pack(expand=True,fill=BOTH)

# gui_frame = Frame(window,bg = "blue",height=100,width=500)
# gui_frame.pack()

mem = ttk.Treeview(table_frame)
mem['columns'] = ("Add1", "Data1", "Add2", "Data2","Add3","Data3","Add4","Data4")

mem.column("#0", width=0, stretch= NO)  
mem.column("Add1", anchor=CENTER, width = 100)
mem.column("Data1", anchor=CENTER, width = 100)
mem.column("Add2", anchor=CENTER, width = 100)
mem.column("Data2", anchor=CENTER, width = 100)
mem.column("Add3", anchor=CENTER, width = 100)
mem.column("Data3", anchor=CENTER, width = 100)
mem.column("Add4", anchor=CENTER, width = 100)
mem.column("Data4", anchor=CENTER, width = 100)

mem.heading("#0", text="", anchor= CENTER)
mem.heading("Add1",text = "Add", anchor=CENTER)
mem.heading("Data1",text = "Data", anchor=CENTER)
mem.heading("Add2",text = "Add", anchor=CENTER)
mem.heading("Data2",text = "Data", anchor=CENTER)
mem.heading("Add3",text = "Add", anchor=CENTER)
mem.heading("Data3",text = "Data", anchor=CENTER)
mem.heading("Add4",text = "Add", anchor=CENTER)
mem.heading("Data4",text = "Data", anchor=CENTER)

mem_adds = list(memory_code.main_memory.regs.keys())
for i in range(32):
    add1 = mem_adds[i]
    add2 = mem_adds[i+32]
    add3 = mem_adds[i+64]
    add4 = mem_adds[i+96]
    data1 = memory_code.main_memory.regs[add1].byte()
    data2 = memory_code.main_memory.regs[add2].byte()
    data3 = memory_code.main_memory.regs[add3].byte()
    data4 = memory_code.main_memory.regs[add4].byte()
    l = ("0x"+add1, data1, "0x"+add2, data2, "0x"+add3, data3, "0x"+add4, data4)
    mem.insert(parent='',index='end',text='',values = l)
mem.pack(expand=True, fill = BOTH)


window.mainloop()