import tkinter
from shapely.geometry import Point, LineString
from shapely.geometry.polygon import Polygon
import math
from queue import PriorityQueue
import time


left_point = None
right_point = None

is_rightclicked = False
is_leftclicked = False

graph = {}

drawarray = []
draw_graph_array = []
draw_graph_bool = False

vertex = None
maparray = []

n = 0
m = 0

def map1():
    global maparray
    for i in range(len(maparray)):
        canvas.delete(maparray[i])
    global coordinates
    
    global is_leftclicked
    global is_rightclicked
    global leftclicked_id
    global rightclicked_id

    global left_point
    global right_point

    global drawarray

    
    
    if (is_leftclicked==True):
        canvas.delete(leftclicked_id)
    if (is_rightclicked==True):
        canvas.delete(rightclicked_id)
    is_leftclicked = False
    is_rightclicked = False
    left_point = None
    right_point = None

    for i in range(len(drawarray)):
        canvas.delete(drawarray[i])
    drawarray = []

    coordinates = []
    maparray = []
    global line

    with open("points.txt") as file:
        line = file.read().splitlines()

    for i in range(len(line)-1):
        a = line[i].split(" ")
        b = line[i+1].split(" ")
        coordinates.append((int(a[0]), int(a[1])))
        tmp = canvas.create_line(int(a[0]), int(a[1]), int(b[0]), int(b[1]), fill="black", width=5)
        maparray.append(tmp)
    coordinates.append((int(line[0].split(" ")[0]), int(line[0].split(" ")[1])))

def map2():
    global maparray
    for i in range(len(maparray)):
        canvas.delete(maparray[i])
    global coordinates
    
    global is_leftclicked
    global is_rightclicked
    global leftclicked_id
    global rightclicked_id

    global left_point
    global right_point

    global drawarray

    if (is_leftclicked==True):
        canvas.delete(leftclicked_id)
    if (is_rightclicked==True):
        canvas.delete(rightclicked_id)
    is_leftclicked = False
    is_rightclicked = False
    left_point = None
    right_point = None

    for i in range(len(drawarray)):
        canvas.delete(drawarray[i])
    drawarray = []

    coordinates = []
    maparray = []

    

    global line

    with open("points2.txt") as file:
        line = file.read().splitlines()

    for i in range(len(line)-1):
        a = line[i].split(" ")
        b = line[i+1].split(" ")
        coordinates.append((int(a[0]), int(a[1])))
        tmp = canvas.create_line(int(a[0]), int(a[1]), int(b[0]), int(b[1]), fill="black", width=5)
        maparray.append(tmp)
    coordinates.append((int(line[0].split(" ")[0]), int(line[0].split(" ")[1])))

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

def draw_graph():
    global vertex
    global graph
    global coordinates
    global n
    global m
    global draw_graph_array
    global draw_graph_bool

    if not draw_graph_bool:
        vertex['text'] = "Turn off graph drawing"
        draw_graph_bool = True
        main_polygon = Polygon(coordinates)
        for i in range(len(coordinates)):
            for j in range(len(coordinates)):
                if (i!=j):
                    
                    path = LineString([coordinates[i], coordinates[j]])
                    point = path.interpolate(0.5)

                    if not path.crosses(main_polygon):
                        if (main_polygon.contains(point) or abs(j-i)==1):
                            tmp =canvas.create_line(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1], fill="green", width=1)
                            draw_graph_array.append(tmp)
    else:
        vertex['text'] = "Turn on graph drawing"
        for i in range(len(draw_graph_array)):
            canvas.delete(draw_graph_array[i])
        draw_graph_array = []
        draw_graph_bool = False

def draw_line_right(event):
    global is_rightclicked
    global rightclicked_id

    global right_point
    global n
    global m

    global drawarray

    for i in range(len(drawarray)):
        canvas.delete(drawarray[i])
    drawarray = []

    x1=event.x-5
    y1=event.y-5
    x2=event.x+5
    y2=event.y+5
    x = event.x
    y = event.y
    tmppoint = Point(x, y)
    
    polygon = Polygon(coordinates)
    if polygon.contains(tmppoint):
        right_point = tmppoint
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

    global drawarray

    for i in range(len(drawarray)):
        canvas.delete(drawarray[i])
    drawarray = []

    x1=event.x-5
    y1=event.y-5
    x2=event.x+5
    y2=event.y+5
    x = event.x
    y = event.y
    tmppoint = Point(x, y)
    
    polygon = Polygon(coordinates)
    
    if polygon.contains(tmppoint):
        left_point = tmppoint
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

    start_time = time.time()
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
                #canvas.create_line(coordinates[i][0], coordinates[i][1], left_point.x, left_point.y, fill="red", width=1)

        path = LineString([right_point, left_point])
        if not path.crosses(polygon):
            tmp1 = [n-1, math.sqrt((right_point.x-left_point.x)**2 + (right_point.y-left_point.y)**2)]
            graph[n-2].append(tmp1)

            tmp2 = [n-2, math.sqrt((right_point.x-left_point.x)**2 + (right_point.y-left_point.y)**2)]
            graph[n-1].append(tmp2)
            #canvas.create_line(right_point.x, right_point.y, left_point.x, left_point.y, fill="purple", width=1)
        
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
        distancetoend = distance[end]
        coordinates.append((right_point.x, right_point.y))
        coordinates.append((left_point.x, left_point.y))
        while par[end] != None:
            
            tmp = canvas.create_line(coordinates[par[end]][0], coordinates[par[end]][1], coordinates[end][0], coordinates[end][1], fill="purple", width=5)
            print(end, " ", par[end], " ", coordinates[end], " ", coordinates[par[end]])
            drawarray.append(tmp)
            end = par[end]
        coordinates.pop()
        coordinates.pop()
    elapsed_time = time.time() - start_time
    timetext['text'] = "Time Executed: " + "{:.2f}".format(elapsed_time) + " seconds"
    print(distance[end])
    distancetext['text'] = "Distance: " + "{:.2f}".format(distancetoend)

if __name__ == '__main__':
    
    window = tkinter.Tk()
    window.title("Shortest path GUI")
    window.geometry("1500x800")
    window['bg'] = 'white'
    btn_dijkstra = tkinter.Button(window, text="Find the shortest path", command=dijkstra, fg = 'black', bg = 'yellow')
    btn_dijkstra.place(rely=0.05, relx=0.3, anchor="center")
    
    vertex = tkinter.Button(window, text="Turn on graph drawing", command=draw_graph, fg = 'black', bg = 'yellow')
    vertex.place(rely=0.05, relx=0.4, anchor="center")

    map1 = tkinter.Button(window, text="Map 1", command=map1, fg = 'black', bg = 'yellow')
    map1.place(rely=0.05, relx=0.5, anchor="center")

    map2 = tkinter.Button(window, text="Map 2", command=map2, fg = 'black', bg = 'yellow')
    map2.place(rely=0.05, relx=0.6, anchor="center")

    canvas = tkinter.Canvas(window, width=1500, height=700, bg="white")
    canvas.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
    
    timetext = tkinter.Label(window, text="Time Executed: ")
    timetext.place(relx=0.4, rely=0.1, anchor=tkinter.CENTER)

    distancetext = tkinter.Label(window, text="Distance: ")
    distancetext.place(relx = 0.6, rely=0.1, anchor=tkinter.CENTER)

    coordinates = []

    global line
    with open("points.txt") as file:
        line = file.read().splitlines()

    for i in range(len(line)-1):
        a = line[i].split(" ")
        b = line[i+1].split(" ")
        coordinates.append((int(a[0]), int(a[1])))
        tmp = canvas.create_line(int(a[0]), int(a[1]), int(b[0]), int(b[1]), fill="black", width=5)
        maparray.append(tmp)
    coordinates.append((int(line[0].split(" ")[0]), int(line[0].split(" ")[1])))

    
    #new thing here


    create_graph()

    canvas.bind('<Button-1>', draw_line_left)
    canvas.bind('<Button-3>', draw_line_right)

    #display timer dijkstra in the window
    
    window.mainloop() 
