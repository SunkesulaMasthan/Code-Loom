graph={'a':['b','c'],'b':['d','e'],'c':['f'],'d':[],'e':['f'],'f':[]}
visited=set()
##queue=[]
def dfs(visited,graph,node):
    #visited.append(node)
    #queue.append(node)
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
             dfs(visited,graph,neighbour)
dfs(visited,graph,'a')
'''output:
a
b
d
e
f
c
'''
