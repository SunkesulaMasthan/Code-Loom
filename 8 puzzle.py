from collections import deque
goal="012345678"
def move(state,i,j):
    s=list(state)
    s[i],s[j]=s[j],s[i]
    return ''.join(s)
def get_moves(state):
    i=state.index('0')
    moves=[]
    if i not in [0,1,2]:
        moves.append(move(state,i,i-3))
    if i not in [6,7,8]:
        moves.append(move(state,i,i+3))
    if i not in [0,3,6]:
        moves.append(move(state,i,i-1))
    if i not in [2,5,8]:
        moves.append(move(state,i,i+1))
    return moves
def solve(start):
    visited={start:None}
    q=deque([start])
    while q:
        state=q.popleft()
        if state==goal:
            path=[]
            while state:
                path.append(state)
                state=visited[state]
            return path[::-1]
        for m in get_moves(state):
            if m not in visited:
                visited[m]=state
                q.append(m)
    return None
start="123406758"
path=solve(start)
if path:
    print(f"solved in{len(path)-1}moves...")
    for p in path:
        print(p[0:3])
        print(p[3:6])
        print(p[6:9])
        print()
else:
    print("no solution foud")
'''output:
solved in20moves...
123
406
758

123
460
758

120
463
758

102
463
758

012
463
758

412
063
758

412
603
758

412
630
758

410
632
758

401
632
758

431
602
758

431
652
708

431
652
078

431
052
678

031
452
678

301
452
678

310
452
678

312
450
678

312
405
678

312
045
678

012
345
678
'''
