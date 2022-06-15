# Best first search - h(f)=no. of misplaced tiles
import copy

visited=[]
q=[]

def compare(s,g):
    if(s==g):
        return True
    return False 

def heuristic(s,g):
    count=0
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j]!=g[i][j]:
                count=count+1
    return count

# def find_space(curr):
#     for i in range(len(curr)):
#         for j in range(len(curr[0])):
#             if curr[i][j]==0:
#                 return [i,j]

def find_space(curr):
    l=[]
    for i in range(len(curr)):
        for j in range(len(curr[0])):
            if curr[i][j]==0:
                l+=[i,j]
                return l

def up(curr,space):
    a=curr.copy()
    i=space[0]
    j=space[1]
    if i==0:
        return a
    else: 
        temp=a[i][j]
        a[i][j]=a[i+1][j]
        a[i-1][j]=temp
        # visited.append(a)
        return a
            
def down(curr,space):
    a=curr.copy()
    i=space[0]
    j=space[1]
    if i==2:
        return a
    else:  
        temp=a[i][j]
        a[i][j]=a[i-1][j]
        a[i+1][j]=temp
        # visited.append(a)
        return a

def left(curr,space):
    a=curr.copy()
    i=space[0]
    j=space[1]
    if j==0:
        return a
    else: 
        temp=a[i][j]
        a[i][j]=a[i][j+1]
        a[i][j-1]=temp
        # visited.append(a)
        return a

def right(curr,space):
    a=curr.copy()
    i=space[0]
    j=space[1]
    if j==2: 
        return a 
    else: 
        temp=a[i][j]
        a[i][j]=a[i][j-1]
        a[i][j+1]=temp
        # visited.append(a)
        return a

def enqueue(s):
    global visited
    if s[1] not in visited:
        global q
        q = q + [s]

def dequeue():
    global q
    new=q[0]
    del q[0]
    return new

# def action(curr,g):
#     if curr==g:
#         return g
#     space=find_space(curr)
#     up(curr,space)
#     down(curr,space)
#     left(curr,space)
#     right(curr,space)




def main():
    s=[[2,0,3],
       [1,8,4],
       [7,6,5]]
    g=[[1,2,3],
       [8,0,4],
       [7,6,5]]
    # curr=s
    # h=heuristic(curr,g)
    # space=find_space(curr) #spcace will return a list 
    # print(h)
    # while s!=g or h==0:
    #     action(curr,g)
    if compare(s,g):
        print("Initial and final states are same")
        return 
    
    global visited
    while(True):
        space=find_space(s)
        
        new=up(s,space)
        if compare(new,g):
            print('Found')
            return
        else:
            dist= heuristic(s,g)
            enqueue([dist,new])

        new=down(s,space)
        if compare(new,g):
            print('Found')
            return
        else:
            dist= heuristic(s,g)
            enqueue([dist,new])
        
        new=left(s,space)
        if compare(new,g):
            print('Found')
            return
        else:
            dist= heuristic(s,g)
            enqueue([dist,new])
            
        new=right(s,space)
        if compare(new,g):
            print('Found')
            return
        else:
            dist= heuristic(s,g)
            enqueue([dist,new])
        
        q.sort()
        newone=dequeue()
        new_one_state=newone[1]
        visited=visited +[s]
        s=new_one_state
        print(new_one_state)

main()