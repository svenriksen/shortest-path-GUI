from pydoc import classname
import tkinter



if __name__ == '__main__':
    window = tkinter.Tk()
    window.title("Shortest path GUI")
    window.geometry("1000x600")

    

    button1 = tkinter.Button(window, text="Click me", command=lambda: print("Button1"), width=10, height=1).grid(padx=50, pady=20, row=1, column=1)
    button1 = tkinter.Button(window, text="Click me", command=lambda: print("Button1")).grid(padx=50, pady=20, row=1, column=2)
    window.mainloop()
