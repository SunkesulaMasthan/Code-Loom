world=[["s","b","p","b"],
   ["st","s","b","s"],
   ["w","g","p","b"],
   ["st","s","b","p"]
   ]        
a=True
score=0
x,y=0,0
while True:
    print("position:",(x,y),"->",world[x][y])
    move=input("move(u/d/l/r):")
    if  move=='u':x-=1
    elif move=='d':x+=1
    elif move=='l':y-=1
    elif move=='r':y+=1
    else:
        print("invalid choice")
        continue
    if x<0 or x>3 or y<0 or y>3:
        print("you hit the world")
        break
    cell=world[x][y]
    if cell=="w" or cell=="p":
        print("game over")
        score-=1000
        break
    if cell=="g":
        print("you found the gold")
        score+=1000
        break
    if cell=="st" and a:
        shoot=input("shoot arrow(y/n):")
        if shoot=="y":
            direction=input("direction(u/d/l/r):")
            if direction=="d" and world[x+1][y]=="w":
                print( "wumpus kiled")
                score+=1000
                world[x+1][y]="safe"
            else:
                print("missed")
                score+=10
            a=False
print("score:",score)
'''output:
position: (0, 0) -> s
move(u/d/l/r):d
shoot arrow(y/n):y
direction(u/d/l/r):d
wumpus kiled
position: (1, 0) -> st
move(u/d/l/r):d
position: (2, 0) -> safe
move(u/d/l/r):l
you hit the world
'''
score: 1000
                
    
