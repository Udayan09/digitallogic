from tkinter import *

def clk_signal(window, canvas, clk, coords, prev_sig = 0):
    if len(clk) == 0:
        return
    
    period = 50
    high_len = 50

    curr_sig = clk[0]
    newx = coords[-1][0]
    newy = coords[-1][1]

    if prev_sig == curr_sig:
        newx += period
    elif prev_sig == 0 and curr_sig == 1:
        newy -= high_len
        coords.append((newx,newy))
        newx += period
    elif prev_sig == 1 and curr_sig == 0:
        newy += high_len
        coords.append((newx,newy))
        newx += period

    coords.append((newx,newy))

    canvas.delete("clk")
    canvas.create_line(coords, fill = "green", tag = "clk")
    
    window.after(500,clk_signal,window, canvas, clk[1:],coords,curr_sig)

def create_clk(parent):
    canvas = Canvas(parent, width=800, height = 200, bg = "white")
    canvas.pack()
    
    return canvas

def run_clk(window, canvas, clk, coords):
    canvas.create_line(0, 100, 20, 100, fill = "red")
    clk_signal(window, canvas, clk, coords)


