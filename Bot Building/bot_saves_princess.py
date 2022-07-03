#!/usr/bin/python

def displayPathtoPrincess(n,grid):
#print all the moves here
    for i in range(n):
        for j in range(n):
            if(grid[i][j]=='p'):
                pos1=i
                pos2=j
                break
    mid1=int(n/2)
    mid2=mid1
    if(pos1>mid1):
        while(mid1!=pos1):
            mid1+=1
            print("DOWN")
        if(pos2>mid2):
            while(mid2!=pos2):
                print("RIGHT")
                mid2+=1
        elif(pos2<mid2):
            while(mid2!=pos2):
                print("LEFT")
                mid2-=1
        else:
            return
        
    elif(pos1<mid1):
        while(mid1!=pos1):
            mid1-=1
            print("UP")
        if(pos2>mid2):
            while(mid2!=pos2):
                print("RIGHT")
                mid2+=1
        elif(pos2<mid2):
            while(mid2!=pos2):
                print("LEFT")
                mid2-=1
        else:
            return
    
    else:
        return
        
    
    

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
