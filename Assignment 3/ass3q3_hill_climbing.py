# QS-3 HILL CLIMBING 
import copy
visited_state=[]
queue=[]

def compare(s,g):
    if(s==g):
        return True
    return False 
            
def find_space(current_state):
    l=[]
    for i in range(len(current_state)):
        for j in range(len(current_state[0])):
            if current_state[i][j]==0:
                l+=[i,j]
                return l
                
def move_up(current_state,pos):
    new_state=copy.deepcopy(current_state)
    row=pos[0]
    col=pos[1]
    if row==0:
        return current_state
    new_state[row][col]=new_state[row-1][col]
    new_state[row-1][col]=0
    return new_state
    
def move_down(current_state,pos):
    new_state=copy.deepcopy(current_state)
    row=pos[0]
    col=pos[1]
    if row==len(current_state)-1:
        return current_state
    new_state[row][col]=new_state[row+1][col]
    new_state[row+1][col]=0
    return new_state
    
def move_left(current_state,pos):
    new_state=copy.deepcopy(current_state)
    row=pos[0]
    col=pos[1]
    if col==0:
        return current_state
    new_state[row][col]=new_state[row][col-1]
    new_state[row][col-1]=0
    return new_state
    
def move_right(current_state,pos):
    new_state=copy.deepcopy(current_state)
    row=pos[0]
    col=pos[1]
    if col==(len(current_state[0])-1):
        return current_state
    new_state[row][col]=new_state[row][col+1]
    new_state[row][col+1]=0
    return new_state

def enqueue(new_state):
    global visited_state
    if new_state[1] not in visited_state:
        global queue
        queue += [new_state]

def dequeue():
    global queue
    if len(queue)==0:
        print('not found')
        exit()
    new_state=queue[0]
    queue=[]
    return new_state
    
def heuristic(s,g):
    count=0
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j]!=g[i][j]:
                count=count+1
    return count

def main():
    final_state=[[1,2,3],[8,0,4],[7,6,5]]
    initial_state=[[2,0,3],[1,8,4],[7,6,5]]
    if compare(initial_state,final_state):
        print('yes')
        return 
    
    global visited_state
    while(True):
        curr_pos=find_space(initial_state)
        
        new_state=move_up(initial_state,curr_pos)
        if compare(new_state,final_state):
            print('Found')
            print(new_state)
            return
        else:
            dist= heuristic(new_state,final_state)
            enqueue([dist,new_state])

        new_state=move_down(initial_state,curr_pos)
        if compare(new_state,final_state):
            print('Found')
            print(new_state)
            return
        else:
            dist= heuristic(new_state,final_state)
            enqueue([dist,new_state])
        
        new_state=move_left(initial_state,curr_pos)
        if compare(new_state,final_state):
            print('Found')
            print(new_state)
            return
        else:
            dist= heuristic(new_state,final_state)
            enqueue([dist,new_state])
            
        new_state=move_right(initial_state,curr_pos)
        if compare(new_state,final_state):
            print('Found')
            print(new_state)
            return
        else:
            dist= heuristic(new_state,final_state)
            enqueue([dist,new_state])
        
        queue.sort()
        newone=dequeue()
        new_one_state=newone[1]
        visited_state=visited_state +[initial_state]
        initial_state=new_one_state
        print(initial_state)
    
main()