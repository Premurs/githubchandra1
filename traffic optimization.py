import time
network = {'A':[('B',10),('C',15')],'B':[('A',10),('D',12),('E',15)],'C':[('A',12),('F'),15],'D':[('B',10),('G',12),('H',8)],'E':[('B',12),('I',15)],'F':[('C',8),('J',13)],'G':[('D',7),('K',14)],'H':[('D',12),('L',10)],'I':[('E',10),('M',8)],'J':[('F',15),('N',12)],'K':[('G',10),('O',10)],'L':[('H',10),('P',8)],'M':[('I',8),('Q',10)],'N':[('J',12),('R',15)],'O':[('K',10),('S',12)],'P':[('L',8),('T',15)],'Q':[('M',10),('U',10)],'R':[('N',15),('V',12)],'S':[('O',12),('W',10)],'T':[('P',15),('X',8)],'U':[('Q',10),('Y',15)],'V':[('R',12),('Z',10)],'W':[('S',10)],'X':[('T',8)],'Y':[('U',15)],'Z':[('V',10)]}
source='A'
destination="Z"
def bfs(source,destination):
    queue=[]
    visited=set()
    parent={}
    travel_time={}
    queue.append(source)
    visited.add(source)
    travel_time[source]=0
    while queue:
        node=queue.pop(0)
        if node==destination:
            path=[]
            time=travel_time[node]
            while node !=source:
                path.append(node)
                node=parent[node]
            path.append(source)
            path.reverse()
            return path,time
        for neighbor,time in network[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor]=node
                travel_time[neighbor]=travel_time[node]+time
    return None,None
def dfs(source,destination):
    stack=[]
    visited=set()
    parent={}
    travel_time={}
    stack.append(source)
    visited.add(source)
    while stack:
        node=stack.pop()
        if node==destination:
            path=[]
            time=travel_time[node]
            while node !=source:
                path.append(node)
                node=parent[node]
            path.append(source)
            path.reverse()
            return path,time
        for neighbor,time in network[node]:
            stack.append(neighbor)
            visited.add(neighbor)
            parent[neighbor]=node
            travel_time[neighbor]=travel_time[node]+time
    return None,None
bfs_path,bfs_time=bfs(source,destination)
dfs_path,dfs_time=dfs(source,destination)
print('Bfs path and time:'bfs_path,bfs)

            
            
                    

