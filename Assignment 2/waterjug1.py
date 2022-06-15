def water():
    jug1=int(input("Enter maximum capacity og jug 1: "))
    jug2=int(input("Enter maximum capacity of jug 2: "))
    d=int(input("Enter final state capacity: "))
    x=0
    y=0
    curr=[[x,y]]
    while x!=d:
        # rule1
        if [jug1,y] not in curr and x<jug1:
            x=jug1
            curr.append([x,y])
        # rule2
        elif [x,jug2] not in curr and y<jug2:
            y=jug2
            curr.append([x,y])
        # rule3
        elif [0,y] not in curr and x>0:
            x=0
            curr.append([x,y])
        # rule4
        elif [x,0] not in curr and y>0:
            y=0
            curr.append([x,y])
        # rule 5
        elif [x+y,0] not in curr and y>=0 and x+y>0 and x+y<=jug1:
            x,y=x+y,0
            curr.append([x,y])
        # rule 6
        elif [0,y+x] not in curr and x>=0 and y+x>0 and y+x<=jug2:
            x,y=0,y+x
            curr.append([x,y])
        # rule 7
        elif [jug1,y-(jug1-x)] not in curr and y>0 and x+y>=jug1:
            x,y=jug1,y-(jug1-x)
            curr.append([x,y])
        # rule 8
        elif [x-(jug2-y),jug2] not in curr and x>0 and x+y<=jug2:
            x,y=x-(jug2-y),jug2
            curr.append([x,y])
    print(curr)
    print(len(curr))

water()