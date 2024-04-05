from tkinter import *
import digitallogic
import signal_gen_gui


window = Tk()
window.title("FlipFlop")
window.geometry("400x300")

f1 = digitallogic.Flipflip()

frame1 = Frame(window)
frame1.pack()
l1 = Label(frame1, text="Hello",height=5,width=10,font = ("ariel",20))
l1.pack()
clk = [0,1,1,0,1,0,1,1,1]
coords = [(20,100)]
clk_signal1 = signal_gen_gui.create_clk(window)
clk_signal1.pack()
signal_gen_gui.run_clk(window, clk_signal1,clk,coords)
window.mainloop()