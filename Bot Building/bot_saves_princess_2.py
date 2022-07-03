#

#!/usr/bin/python

def nextMove(n,r,c,grid):
#print all the moves here
    for i in range(n):
        for j in range(n):
            if(grid[i][j]=='p'):
                pos1=i
                pos2=j
                break
    
    mid1=r
    mid2=c
            #return next move??????
            # if(grid[mid1][mid2-1]=='p'):
            #     return "DOWN"
    stk=[]
    if(pos1>mid1):
        while(mid1!=pos1):
            mid1+=1
            stk.append("DOWN")
    elif(pos1<mid1):
        while(mid1!=pos1):
            mid1-=1
            stk.append("UP")
    if(pos2>mid2):
        while(mid2!=pos2):
            mid2+=1
            stk.append("RIGHT")
    elif(pos2<mid2):
        while(mid2!=pos2):
            mid2-=1
            stk.append("LEFT")
    return stk.pop()

        

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))