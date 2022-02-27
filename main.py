from operator import contains
from re import X
import tkinter
from shapely.geometry import Point, LineString
from shapely.geometry.polygon import Polygon
import math

is_rightclicked = False
is_leftclicked = False
graph = {}

n = 0
m = 0
startpoint = 0
endpoint = 0

def create_graph():
    global coordinates
    global graph
    global n
    global m
    n = 0
    m = 0
    graph = {}
    main_polygon = Polygon(coordinates)

    for i in range(len(coordinates)):
        graph[i]=[]
        n = n+1

    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            if (i!=j):
                m = m+1
                
                path = LineString([coordinates[i], coordinates[j]])
                point = path.interpolate(0.5)

                if not path.crosses(main_polygon):
                    if (main_polygon.contains(point) or abs(j-i)==1):
                        tmp1 = [j, math.sqrt((coordinates[i][0]-coordinates[j][0])**2 + (coordinates[i][1]-coordinates[j][1])**2)]
                        graph[i].append(tmp1)
                        canvas.create_line(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1], fill="green", width=1)

def draw_line_right(event):
    global startpoint
    global is_rightclicked
    global rightclicked_id

    global right_point
    global n
    global m

    x1=event.x-5
    y1=event.y-5
    x2=event.x+5
    y2=event.y+5
    x = event.x
    y = event.y
    tmppoint = Point(x, y)
    right_point = tmppoint
    polygon = Polygon(coordinates)
    if polygon.contains(tmppoint):
        
        if not is_rightclicked:
            n=n+1
            startpoint = n-1
            rightclicked_id = canvas.create_oval(x1,y1,x2,y2,fill="green", outline="")
            is_rightclicked = True

            for i in range(len(coordinates)-1):
                path = LineString([coordinates[i], tmppoint])
                if not path.crosses(polygon):
                    tmp1 = [n-1, math.sqrt((coordinates[i][0]-tmppoint.x)**2 + (coordinates[i][1]-tmppoint.y)**2)]
                    graph[n-1].append(tmp1)
                    m=m+1


        else:
            canvas.delete(rightclicked_id)
            rightclicked_id = canvas.create_oval(x1,y1,x2,y2,fill="green", outline="")
            for i in range(len(coordinates)-1):
                
                path = LineString([coordinates[i], tmppoint])

                if not path.crosses(polygon):
                    tmp1 = [n-1, math.sqrt((coordinates[i][0]-tmppoint.x)**2 + (coordinates[i][1]-tmppoint.y)**2)]
                    graph[n-1].append(tmp1)  
                    m=m+1            
    

def draw_line_left(event):
    global ebdpoint
    global is_leftclicked
    global leftclicked_id
    
    global left_point
    global n
    global m

    x1=event.x-5
    y1=event.y-5
    x2=event.x+5
    y2=event.y+5
    x = event.x
    y = event.y
    tmppoint = Point(x, y)
    left_point = tmppoint
    polygon = Polygon(coordinates)
    
    if polygon.contains(tmppoint):

        if not is_leftclicked:
            
            n=n+1
            leftclicked_id = canvas.create_oval(x1,y1,x2,y2,fill="red", outline="")
            is_leftclicked = True

            for i in range(len(coordinates)-1):
                path = LineString([coordinates[i], tmppoint])
                if not path.crosses(polygon):
                    tmp1 = [101, math.sqrt((coordinates[i][0]-tmppoint.x)**2 + (coordinates[i][1]-tmppoint.y)**2)]
                    graph[101].append(tmp1)
                    m=m+1
            
        else:
            canvas.delete(leftclicked_id)
            leftclicked_id = canvas.create_oval(x1,y1,x2,y2,fill="red", outline="")
            for i in range(len(coordinates)-1):
                path = LineString([coordinates[i], tmppoint])

                if not path.crosses(polygon):
                    tmp1 = [101, math.sqrt((coordinates[i][0]-tmppoint.x)**2 + (coordinates[i][1]-tmppoint.y)**2)]
                    graph[101].append(tmp1)
                    m=m+1

    
def dijkstra():
    if (is_leftclicked == True and is_rightclicked == True):
        print(right_point)
        print(left_point)
        print("Dijkstra")

if __name__ == '__main__':
    window = tkinter.Tk()
    window.title("Shortest path GUI")
    window.geometry("1500x800")

    btn_dijkstra = tkinter.Button(window, text="Dijkstra", command=dijkstra)
    btn_dijkstra.pack()

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
        canvas.create_line(int(a[0]), int(a[1]), int(b[0]), int(b[1]), fill="black", width=5)
    coordinates.append((int(line[0].split(" ")[0]), int(line[0].split(" ")[1])))
    coordinates_shapely = []
    #new thing here


    create_graph()

    


    canvas.bind('<Button-1>', draw_line_left)
    canvas.bind('<Button-3>', draw_line_right)
    window.mainloop() 
