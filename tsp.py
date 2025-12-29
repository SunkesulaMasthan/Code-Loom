from sys import maxsize
from itertools import permutations
v=4
def tsp(graph,s):
    vertex=[]
    for i in range(v):
        if i!=s:
            vertex.append(i)
    mp=maxsize
    nextpermutations=permutations(vertex)
    for i in nextpermutations:
        cp=0
        k=s
        print("0",end=" ")
        for j in i:
            cp+=graph[k][j]
            print("---->",j,end=" ")
            k=j
        cp+=graph[k][s]
        print("---0",end=" ")
        print("|cost=",cp)
        mp=min(mp,cp)
    return mp
if __name__=="__main__":
    graph=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
    s=0
print("the cost is:",tsp(graph,s))
'''output:
0 ----> 1 ----> 2 ----> 3 ---0 |cost= 95
0 ----> 1 ----> 3 ----> 2 ---0 |cost= 80
0 ----> 2 ----> 1 ----> 3 ---0 |cost= 95
0 ----> 2 ----> 3 ----> 1 ---0 |cost= 80
0 ----> 3 ----> 1 ----> 2 ---0 |cost= 95
0 ----> 3 ----> 2 ----> 1 ---0 |cost= 95
the cost is: 80
'''
            
