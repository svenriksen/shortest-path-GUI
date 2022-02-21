import tkinter
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

is_rightclicked = False
is_leftclicked = False


def draw_line_right(event):
    global is_rightclicked
    global rightclicked_id
    x1=event.x-5
    y1=event.y-5
    x2=event.x+5
    y2=event.y+5

    tmppoint = Point(x1, y1)
    polygon = Polygon(coordinates)

    if polygon.contains(tmppoint):
        if not is_rightclicked:
            rightclicked_id = canvas.create_oval(x1,y1,x2,y2,fill="green", outline="")
            is_rightclicked = True

        else:
            canvas.delete(rightclicked_id)
            rightclicked_id = canvas.create_oval(x1,y1,x2,y2,fill="green", outline="")
        


def draw_line_left(event):
    global is_leftclicked
    global leftclicked_id
    x1=event.x-5
    y1=event.y-5
    x2=event.x+5
    y2=event.y+5
    tmppoint = Point(x1, y1)
    polygon = Polygon(coordinates)

    if polygon.contains(tmppoint):

        if not is_leftclicked:
            
            leftclicked_id = canvas.create_oval(x1,y1,x2,y2,fill="red", outline="")
            is_leftclicked = True

            for i in range(len(coordinates)-1):
                canvas.create_line(x1,y1,coordinates[i][0],coordinates[i][1],fill="red")
            
        else:
            canvas.delete(leftclicked_id)
            leftclicked_id = canvas.create_oval(x1,y1,x2,y2,fill="red", outline="")
            for i in range(len(coordinates)-1):
                canvas.create_line(x1,y1,coordinates[i][0],coordinates[i][1],fill="red")
    


if __name__ == '__main__':
    window = tkinter.Tk()
    window.title("Shortest path GUI")
    window.geometry("1500x800")

    canvas = tkinter.Canvas(window, width=1500, height=700)
    canvas.pack()

    coordinates = []

    global line

    with open("points.txt") as file:
        line = file.read().splitlines()

    for i in range(len(line)-1):
        a = line[i].split(" ")
        b = line[i+1].split(" ")
        coordinates.append((int(a[0]), int(a[1])))
        canvas.create_line(int(a[0]), int(a[1]), int(b[0]), int(b[1]), fill="black", width=3)

    
    
    canvas.bind('<Button-1>', draw_line_left)
    canvas.bind('<Button-3>', draw_line_right)
    window.mainloop() 