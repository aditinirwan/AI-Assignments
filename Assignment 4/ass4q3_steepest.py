import copy
visited =[]
steps = 0
def heuristic(curr):
    target = g[3]
    h_val =0
    state = copy.deepcopy(curr)
    for i in range (len(state)):
        check = state[i]
        if (len(check) > 0):
            for j in range(len(check)):
                if check[j] == target[j]:
                    h_val+=j
                else:
                    h_val-=j
    return h_val
def generate_next(curr):
    heuristic_val = []
    heuristic_arr = []
    state = copy.deepcopy(curr)
    for i in range (len(state)):
        temp = copy.deepcopy(state)
        if (len(temp[i])>0):
            elem = temp[i].pop()
            
            for j in range(len(temp)):
                temp1 = copy.deepcopy(temp)
                if j!=i:
                    temp1[j].append(elem)
                    if(temp1 not in visited):
                        heuristic_val.append(heuristic(temp1))
                        heuristic_arr.append(temp1)
            
            if len(heuristic_arr) >0:
                ind = heuristic_val.index(min(heuristic_val))
                return heuristic_arr[ind]
    return -1
def Solution():
    global steps
    if (i==g):
        print(g)
        return 
    
    curr = copy.deepcopy(i)
    while(True):
        visited.append(curr)
        steps +=1
        print(steps)
        print(curr)
        new = generate_next(curr)
        if new == -1:
            print("END")
            return
        curr = copy.deepcopy(new)
i=[[],[],['B','C'],['A']]
g=[[],[],[],['A','B','C']]
Solution()