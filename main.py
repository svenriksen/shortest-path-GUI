from operator import contains
from re import X
import tkinter
from turtle import distance
from shapely.geometry import Point, LineString
from shapely.geometry.polygon import Polygon
import math
from queue import PriorityQueue


is_rightclicked = False
is_leftclicked = False
graph = {}

drawarray = []

n = 0
m = 0

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
                        #canvas.create_line(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1], fill="green", width=1)

def draw_line_right(event):
    global is_rightclicked
    global rightclicked_id

    global right_point
    global n
    global m

    for i in range(len(drawarray)):
        canvas.delete(drawarray[i])

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
            rightclicked_id = canvas.create_oval(x1,y1,x2,y2,fill="green", outline="")
            is_rightclicked = True          
        else:
            canvas.delete(rightclicked_id)
            rightclicked_id = canvas.create_oval(x1,y1,x2,y2,fill="green", outline="") 

def draw_line_left(event):
    global is_leftclicked
    global leftclicked_id
    
    global left_point
    global n
    global m

    for i in range(len(drawarray)):
        canvas.delete(drawarray[i])

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
            
            
            leftclicked_id = canvas.create_oval(x1,y1,x2,y2,fill="red", outline="")
            is_leftclicked = True

            
            
        else:
            canvas.delete(leftclicked_id)
            leftclicked_id = canvas.create_oval(x1,y1,x2,y2,fill="red", outline="")
            
def dijkstra():
    global n
    global m
    global drawarray
    if (is_leftclicked == True and is_rightclicked == True):
        print(right_point)
        print(left_point)
        print("Dijkstra")
        create_graph()
        
        graph[n] = []
        n=n+1
        graph[n] = []
        n=n+1
        
        polygon = Polygon(coordinates)
        for i in range(len(coordinates)-1):
            path = LineString([coordinates[i], right_point])
            if not path.crosses(polygon):
                tmp1 = [i, math.sqrt((coordinates[i][0]-right_point.x)**2 + (coordinates[i][1]-right_point.y)**2)]
                graph[n-2].append(tmp1)

                tmp2 = [n-2, math.sqrt((coordinates[i][0]-right_point.x)**2 + (coordinates[i][1]-right_point.y)**2)]
                graph[i].append(tmp2)
                #canvas.create_line(coordinates[i][0], coordinates[i][1], right_point.x, right_point.y, fill="blue", width=1)

        for i in range(len(coordinates)-1):
            path = LineString([coordinates[i], left_point])
            if not path.crosses(polygon):
                tmp1 = [i, math.sqrt((coordinates[i][0]-left_point.x)**2 + (coordinates[i][1]-left_point.y)**2)]
                graph[n-1].append(tmp1)

                tmp2 = [n-1, math.sqrt((coordinates[i][0]-left_point.x)**2 + (coordinates[i][1]-left_point.y)**2)]
                graph[i].append(tmp2)
                #canvas.create_line(coordinates[i][0], coordinates[i][1], left_point.x, left_point.y, fill="yellow", width=1)

        path = LineString([right_point, left_point])
        if not path.crosses(polygon):
            tmp1 = [n-1, math.sqrt((right_point.x-left_point.x)**2 + (right_point.y-left_point.y)**2)]
            graph[n-2].append(tmp1)

            tmp2 = [n-2, math.sqrt((right_point.x-left_point.x)**2 + (right_point.y-left_point.y)**2)]
            graph[n-1].append(tmp2)
            #canvas.create_line(right_point.x, right_point.y, left_point.x, left_point.y, fill="purple", width=1)
        print(graph[0][1])
        start = n-2
        end = n-1
        visited = []
        distance = []
        par = []
        for i in range(n):
            visited.append(False)
            distance.append(float('inf'))
            par.append(None)
        distance[start] = 0
        pq = PriorityQueue()
        pq.put((0, start))
        while not pq.empty():
            (d, v) = pq.get()
            visited[v] = True
            for i in range(len(graph[v])):
                if not visited[graph[v][i][0]] and distance[v] + graph[v][i][1] < distance[graph[v][i][0]]:
                    distance[graph[v][i][0]] = distance[v] + graph[v][i][1]
                    par[graph[v][i][0]] = v
                    pq.put((distance[graph[v][i][0]], graph[v][i][0]))
        print(distance[end])
        print(par)
        coordinates.append((right_point.x, right_point.y))
        coordinates.append((left_point.x, left_point.y))
        while par[end] != None:
            print(par[end])
            tmp = canvas.create_line(coordinates[par[end]][0], coordinates[par[end]][1], coordinates[end][0], coordinates[end][1], fill="purple", width=5)
            drawarray.append(tmp)
            end = par[end]
        coordinates.pop()
        coordinates.pop()


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
