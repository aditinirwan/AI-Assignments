# If the initial  and final  statesare as below,  
# find  the value  ofHeuristic  function,  by  taking
# (i)Euclidean  Distance(ii)Manhattan  Distance(iii)Minkowski  Distance
import math

s=[[2,0,3],
  [1,8,4],
  [7,6,5]]
g=[[1,2,3],
   [8,4,0],
   [7,6,5]]

def manhattan_dist(initial_state,final_state):
    sum=0
    for i in range(len(initial_state)):
        for j in range(len(initial_state[0])):
            for x in range(len(final_state)):
                flag=False
                for y in range(len(final_state[0])):
                    if initial_state[i][j]==final_state[x][y]:
                        sum+=(abs(x-i)) + abs(y-j)
                        flag=True
                        break
                if flag == True:
                    break
    return sum

def Eucledian_dist(initial_state,final_state):
    sum=0
    for i in range(len(initial_state)):
        for j in range(len(initial_state[0])):
            for x in range(len(final_state)):
                flag=False
                for y in range(len(final_state[0])):
                    if initial_state[i][j]==final_state[x][y]:
                        sum+=(((x-i)**2) + ((y-j)**2))**(1/2)
                        flag=True
                        break
                if flag == True:
                    break
    return sum

def Minkowski_dist(initial_state,final_state):
    sum=0
    p=3
    for i in range(len(initial_state)):
        for j in range(len(initial_state[0])):
            for x in range(len(final_state)):
                flag=False
                for y in range(len(final_state[0])):
                    if initial_state[i][j]==final_state[x][y]:
                        sum+=((abs(x-i)**p) + (abs(y-j)**p))**(1./p)
                        flag=True
                        break
                if flag==True:
                    break
    return sum


def main():
    print("Manhattan: ")
    m=manhattan_dist(s,g)
    print(m)
    print("Eucledian: ")
    e=Eucledian_dist(s,g)
    print(e)
    print("Minkowski: ")
    min=Minkowski_dist(s,g)
    print(min)

main()


