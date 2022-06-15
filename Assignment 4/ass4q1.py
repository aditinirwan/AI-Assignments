import copy

visited_states = []

def heuristic(curr_state,goal_state):
    # the state of the final stack
    goal_=goal_state[3]
    # initially set the value to 0
    val=0
    #traverse each stack in state
    for i in range(len(curr_state)):
        # check val stores the value of the first stack in chosen state
        check_val=curr_state[i]
        # check if the stack has any blocks (length more than 0)
        if len(check_val)>0:
            # pick each block in teh stack one by one
            for j in range(len(check_val)):
                # check if it matches corresponding location in the goal state
                if check_val[j]!=goal_[j]:
                    # if it does not match then subtract j from heuristic value
                    # val-=1
                    val-=j
                else:
                    # if it matches then add j to heuristic value
                    # val+=1
                    val+=j
    # return the heuristic value
    return val
            
# this function generates the next state            
def generate_next(curr_state,prev_heu,goal_state):
    state = copy.deepcopy(curr_state)
    # choose each stack in the given state
    for i in range(len(state)):
        temp = copy.deepcopy(state)
        # for each stack in the state, check if length >=1, ie the stack is not empty
        if len(temp[i]) > 0:
            # if condition checks, store and then pop the element from this stack
            elem = temp[i].pop()
            # for each stack in temp
            for j in range(len(temp)):
                # create a copy of temp, and create new state
                temp1 = copy.deepcopy(temp)
                if j != i:
                    temp1[j].append(elem)
                    # check if the new state is not in visited array 
                    if (temp1 not in visited_states):
                        # find the current heuristic
                        curr_heu=heuristic(temp1,goal_state)
                        # compare the heuristic values
                        if curr_heu>prev_heu:
                            # if better solution exists then return the newly created state
                            return temp1
    return 0

def solution_(init_state,goal_state):
    global visited_states

    # checking if initial state is already the final state
    if (init_state == goal_state):
        print (goal_state)
        print("solution found!")
        return
    
    current_state = copy.deepcopy(init_state)
    
    # loop while goal is found or no better optimal solution is possible
    while(True):

        # add current state to visited to avoid repetition
        visited_states.append(copy.deepcopy(current_state))

        print(current_state)
        prev_heu=heuristic(current_state,goal_state)

        # generate possible better child from current state
        child = generate_next(current_state,prev_heu,goal_state)
        
        # No more better states are possible
        if child==0:
            print("Final state - ",current_state)
            return
            
        # change current state to child
        current_state = copy.deepcopy(child)  

init_state = [[],[],[],['B','C','D','A']]
goal_state = [[],[],[],['A','B','C','D']]
    
solution_(init_state,goal_state)
