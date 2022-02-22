from re import X
import tkinter
import numpy



class point:
    X
    y

if __name__ == '__main__':
    window = tkinter.Tk()
    window.title("Shortest path GUI")
    window.geometry("1500x700")

    
    canvas = tkinter.Canvas(window, width=1500, height=600)
    canvas.pack()



    canvas.create_line(100,200,200,35, fill="green", width=4)

    
    window.mainloop()  