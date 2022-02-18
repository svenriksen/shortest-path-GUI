import tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

def plot():
  
    fig = Figure(figsize = (5, 5), dpi = 100)
  
  
    plot1 = fig.add_subplot(111)
  
  
    canvas = FigureCanvasTkAgg(fig, master = window)  
    canvas.draw()
  
    canvas.get_tk_widget().pack()
  
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
  
    canvas.get_tk_widget().pack()

if __name__ == '__main__':
    window = tkinter.Tk()
    window.title("Shortest path GUI")
    window.geometry("1000x600")

    

    button1 = tkinter.Button(window, text="Click me", width=10, height=1, command = plot)
    
    button1.pack()
    window.mainloop()  