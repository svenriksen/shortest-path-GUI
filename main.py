from re import X
import tkinter
from shapely.geometry import Point, LineString
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
    x = event.x
    y = event.y
    tmppoint = Point(x, y)
    polygon = Polygon(coordinates)
    if polygon.contains(tmppoint):
        if not is_rightclicked:
            rightclicked_id = canvas.create_oval(x1,y1,x2,y2,fill="green", outline="")
            is_rightclicked = True

            for i in range(len(coordinates)-1):
                path = LineString([coordinates[i], tmppoint])
                if not path.crosses(polygon):
                    canvas.create_line(coordinates[i][0], coordinates[i][1], tmppoint.x, tmppoint.y, fill="green", width=3)

        else:
            canvas.delete(rightclicked_id)
            rightclicked_id = canvas.create_oval(x1,y1,x2,y2,fill="green", outline="")
            for i in range(len(coordinates)-1):
                path = LineString([coordinates[i], tmppoint])
                print(path.intersects(polygon), ' ', path)


                if not path.crosses(polygon):
                    canvas.create_line(coordinates[i][0], coordinates[i][1], tmppoint.x, tmppoint.y, fill="green", width=3)
    
        


def draw_line_left(event):
    global is_leftclicked
    global leftclicked_id
    x1=event.x-5
    y1=event.y-5
    x2=event.x+5
    y2=event.y+5
    x = event.x
    y = event.y
    tmppoint = Point(x, y)
    polygon = Polygon(coordinates)

    if polygon.contains(tmppoint):

        if not is_leftclicked:
            
            leftclicked_id = canvas.create_oval(x1,y1,x2,y2,fill="red", outline="")
            is_leftclicked = True

            for i in range(len(coordinates)-1):
                path = LineString([coordinates[i], tmppoint])
                if not path.crosses(polygon):
                    canvas.create_line(coordinates[i][0], coordinates[i][1], tmppoint.x, tmppoint.y, fill="red", width=3)
            
        else:
            canvas.delete(leftclicked_id)
            leftclicked_id = canvas.create_oval(x1,y1,x2,y2,fill="red", outline="")
            for i in range(len(coordinates)-1):
                path = LineString([coordinates[i], tmppoint])
                print(path.intersects(polygon), ' ', path)


                if not path.crosses(polygon):
                    canvas.create_line(coordinates[i][0], coordinates[i][1], tmppoint.x, tmppoint.y, fill="red", width=3)
    


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

    coordinates_shapely= []
        
    for i in range(len(coordinates)):
        coordinates_shapely.append(Point(coordinates[i][0], coordinates[i][1]))
    
    #check if one point to another is inside the polygon




    canvas.bind('<Button-1>', draw_line_left)
    canvas.bind('<Button-3>', draw_line_right)
    window.mainloop() 
