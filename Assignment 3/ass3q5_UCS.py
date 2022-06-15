from queue import Queue, PriorityQueue

def ucs_weight(from_node, to_node, weights=None):
    if weights:
        return weights.get((from_node, to_node), 10e100) 
    else: 
        1

def ucs(graph, start, goal, weights): 
    visited = [] 
    path = [start]
    fringe = PriorityQueue() 
    fringe.put((0, start, path, visited)) 
    order=[]
    while not fringe.empty():
        depth, current_node, path, visited = fringe.get() 
        order.append(current_node)
        if current_node == goal:
            print("Order of the graph according to UCS:",order) 
            print("Shortest cost path from start togoal:",path) 
            print("Total shortestcost=",depth)
            return
        visited = visited + [current_node] 
        child_nodes = graph[current_node] 
        for node in child_nodes:
            if node not in visited:
                depth_of_node = depth+ucs_weight(current_node, node, weights)
                fringe.put((depth_of_node, node, path + [node],visited))

ucs_test_graph = {
'S': ['A', 'B', 'C'],
'A': ['S','G'],
'B': ['S','G'],
'C': ['S','G'],
'G': ['A', 'B', 'C']
}
ucs_test_weight={
    ('S',	'A'):	1,
('S',	'B'):	5,
('S',	'C'):	15,
('A',	'G'):	10,
('A',	'S'):	1,
('B',	'S'):	5,
('B',	'G'):	5,
('C',	'S'):	15,
('C',	'G'):	5,
('G',	'A'):	10,
('G',	'B'):	5,
('G',	'C'):	5,
}

ucs(ucs_test_graph, 'S', 'G',ucs_test_weight)
