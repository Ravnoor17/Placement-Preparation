import queue
from copy import deepcopy

def up(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate):
    if startX-1>=0 and startX-1<=endX and startY>=0 and startY<=endY:
        if maze[startX-1][startY] not in visited:
            temp=deepcopy(maze[startX-1][startY])
            path.append(temp)
            cell=(startX-1, startY)
            backtrack[cell]=startX, startY
            coordinate.append((startX-1, startY))

def down(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate):
    if startX+1>=0 and startX+1<=endX and startY>=0 and startY<=endY:
        if maze[startX+1][startY] not in visited:
            temp=deepcopy(maze[startX+1][startY])
            path.append(temp)
            coordinate.append((startX+1, startY))
            backtrack[startX+1, startY]=startX,startY


def right(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate):
    if startX>=0 and startX<=endX and startY+1>=0 and startY+1<=endY:
        if maze[startX][startY+1] not in visited:
            temp=deepcopy(maze[startX][startY+1])
            path.append(temp)
            coordinate.append((startX, startY+1))
            backtrack[startX, startY+1]=startX,startY

def left(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate):
    if startX>=0 and startX<=endX and startY-1>=0 and startY-1<=endY:
        if maze[startX][startY-1] not in visited:
            temp=deepcopy(maze[startX][startY-1])
            path.append(temp)
            coordinate.append((startX, startY-1))
            backtrack[startX, startY-1]=startX,startY


def bfs(maze, movements, startX, startY, endX, endY):
    
    path=queue.deque() #path traversed
    visited=[] #visited or not
    backtrack={}
    coordinate=queue.deque() #store coordinate of current element
    
    current=deepcopy(maze[startX][startY]) #current value
    path.append(current)

    backtrack[startX, startY]=startX,startY #backtrack

    coordinate.append((startX, startY)) #coordinate

    

    while len(path)>0:
        current=deepcopy(path.popleft())
        startX, startY=coordinate.popleft()
        move=movements[current]

        if move==1:
            up(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)              

            
        elif move==2:
            down(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)

            
        elif move==3:
            right(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
            
        
        elif move==4:
            left(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
            

        elif move==5:
            up(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
            down(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)

        
        elif move==6:
            up(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
            right(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
                    
        elif move==7:
            up(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
            left(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
            
           

        elif move==8:
            down(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
            right(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
            
        
        elif move==9:
            down(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
            left(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)

            
        
        elif move==10:
            right(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
            left(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
           
        
        elif move==11:
            up(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
            down(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
            right(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)

            
        
        elif move==12:
            up(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
            down(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
            left(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
           
        
        elif move==13:
            up(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
            right(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
            left(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
            
        
        elif move==14:
            down(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
            right(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
            left(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)

            
        
        elif move==15:
            up(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
            down(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
            left(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
            right(maze, startX, startY, endX, endY, visited, path, backtrack, coordinate)
        
        visited.append(current)


    

    final_path=[]

    temp=maze[endX][endY]
    final_path.append(temp)

    while (endX, endY) != (0, 0):
        temp = backtrack[endX, endY]
        m_x, m_y=temp
        temp=maze[m_x][m_y]
        final_path.append(temp)
        endX,endY=backtrack[endX,endY]

    final_path.reverse()

    for x in final_path:
        print(x, end=" ")

    
    



m, n=map(int, input().split())
startX, startY=0,0
endX, endY=m-1,n-1
movements={}
column=[]
maze=[]
for i in range(1, m*n+1):

    pixelNumber, u, r, d, l=map(int, input().split())

    if(u==1 and d==0 and r==0 and l==0):
        move=1
    elif(d==1 and u==0 and r==0 and l==0):
        move=2 
     
    elif(r==1 and u==0 and d==0 and l==0):
        move=3 
    
    elif(l==1 and u==0 and d==0 and r==0):
        move=4 
     
    elif(u==1 and d==1 and r==0 and l==0):
        move=5 
     
    elif(u==1 and r==1 and d==0 and l==0):
        move=6 
     
    elif(u==1 and l==1 and d==0 and r==0):
        move=7 
     
    elif(d==1 and r==1 and u==0 and l==0):
        move=8 
     
    elif(d==1 and l==1 and u==0 and r==0):
        move=9
     
    elif(r==1 and l==1 and u==0 and d==0):
        move=10 
     
    elif(u==1 and d==1 and r==1 and l==0):
        move=11 
     
    elif(u==1 and d==1 and l==1 and r==0):
        move=12 
     
    elif(u==1 and r==1 and l==1 and d==0):
        move=13  
    elif(d==1 and r==1 and l==1 and u==0):
        move=14
    elif(u==1 and l==1 and d==1 and r==1):
        move=15

    if i%n != 0:
        column.append(i)
    elif i%n==0:
        column.append(i)
        column=tuple(column)
        maze.append(column)
        column=[]

    movements[i]=move

maze=tuple(maze)


bfs(maze, movements, startX, startY, endX, endY)