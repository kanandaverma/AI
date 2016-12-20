
import operator
import Queue as Q
file1=open('input.txt', 'r')
algo=file1.readline()
algo =''.join(c for c in algo if c not in '\n ''')
start=file1.readline()
start=''.join(c for c in start if c not in '\n ''')
end=file1.readline()
end=''.join(c for c in end if c not in '\n ''')
ed=file1.readline()
edge=int(ed)

graph_bd={}

graph_u={}

for i in range(1,edge+1):
    q=[]
    v=[]
    qu=[]
    vu=[]
    edges=file1.readline()
    edges=edges.split()
    key=edges[0]
    value=edges[1]
    cost=edges[2]
    if graph_bd.has_key(key):
        v=graph_bd[key]
        v.append(value)
        graph_bd[key]=v
    else:
        q.append(value)
        graph_bd[key]=q
        
    if graph_u.has_key(key):
        vu=graph_u[key][0]
        vu.append(value)
        graph_u[key][0]=vu
        c=graph_u[key][1]
        c.append(cost)
        graph_u[key][1]=c
        graph_u.update({key:([vu,c])})
    else:
        graph_u.update({key:([[value],[cost]])})
        
heuristic={}
vertex=int(file1.readline())
for i in range(1,vertex+1):
    A=file1.readline()
    A=A.split()
    vert=A[0]
    heu=A[1]
    heuristic.update({vert:(heu)})
 
file1.close()   

def pathtrack_bfs(parent, start, end):
    path = [end]
    while path[-1] != start:
        h=parent[path[-1]][0]
        path.append(h)
    return path

def bfs(graph, start, end):
    parent = {}
    queue = []
    queue.append(start)
    answer={}
    visited=[]
    r=[]
    while queue:
        node = queue.pop(0)
        if node == end:
            path=pathtrack_bfs(parent, start, end)
        if node not in visited:                                         
            visited.append(node)
            for neighbour in graph.get(node, []):
                if parent.has_key(neighbour):
                    r.append(parent[neighbour])
                    r.append(node)
                    parent[neighbour]=r
                else:
                    parent[neighbour]=node     
                queue.append(neighbour)  
    length=len(path)
    while path:
        length=length-1
        k=path.pop(0)
        answer[k]=length
    sorted_answer=sorted(answer.items(), key=operator.itemgetter(1))
    new_list = []
    for item in sorted_answer:
        new_list.append([item[0],item[1]])
    return new_list
    
        
def pathtrack(parent, start, end):
    path = [end]
    while path[-1] != start:
        h=parent[path[-1]]
        path.append(h)
    return path


def dfs(graph, start, end):
    parent = {}
    stack = []
    stack.append(start)
    visited=[]
    answer={}
    while stack:
        node = stack.pop()
        if node == end:
            path=pathtrack(parent, start, end)
        if node not in visited:
            visited.append(node)
            for neighbour in graph.get(node, []):
                parent[neighbour] = node
                stack.append(neighbour)
    length=len(path)
    while path:
        length=length-1
        k=path.pop(0)
        answer[k]=length
    sorted_answer=sorted(answer.items(), key=operator.itemgetter(1))
    return sorted_answer
    new_list = []
    for item in sorted_answer:
        new_list.append([item[0],item[1]])
    return new_list

prqu=Q.PriorityQueue()

def path_track(i,NPC,path,start):
    for j in range(i):
        if NPC[i][1] in NPC[j][0] and NPC[j][2]<NPC[i][2]:
            path.append([NPC[j][0],NPC[j][2]])
            if NPC[j][0]==start:
                break
            else:
                path=path_track(j, NPC, path,start) 
            break
    return path

def uniform_cost_search(graph, start, end):
    pq=Q.PriorityQueue()
    arr=[]
    path=[]
    pq.put([0,start])
    NPC_len=0
    NPC=[]
    NPC.append([start,None,0])
    while pq:
        node=pq.get()
        if node[1]==end:
            result=node
            NPC_len=len(NPC)
            for i in range(NPC_len):
                if end in NPC[i][0] and NPC[i][2]==int(result[0]):
                        path.append([NPC[i][0],NPC[i][2]])
                        path=path_track(i, NPC, path,start)
                        break
            path.reverse()
            return path 
            break
        arr=graph[node[1]]
        count=0
        for i in arr[0]:
            cost=int(graph[node[1]][1][count])+node[0]
            kid=graph[node[1]][0][count]
            pq.put([cost, kid])
            count=count+1
            NPC.append([kid,node[1],cost])  
                              
def find_way(i,data,start,end,NPC_len,way):
    for g in range(NPC_len):
        if data[i][0] in data[g][1]:
            way.append([data[g][0],data[g][2]])
            if data[g][0]==end:
                break
            else:
                way=find_way(g,data,start,end,NPC_len,way)
            break
    return way        
            
def A_star(graph,start,end):
    pq=Q.PriorityQueue()
    pqa=Q.PriorityQueue()
    arr=[]
    path=[]
    pq.put([0,start])
    NPC=[]
    NPC_len=0
    NPC.append([start,"nothingg",0])
    way=[]
    data=[]
    while pq:
        node=pq.get()           
        if node[1]==end:
            result=node
            NPC_len=len(NPC)
            for i in range(NPC_len):
                if end in NPC[i][0] and NPC[i][2]==int(result[0]):
                        path.append([NPC[i][0],NPC[i][2]])
                        path=path_track(i, NPC, path,start)
                        break
            path.reverse() 
            break
        arr=graph[node[1]]
        count=0
        for i in arr[0]:
            cost=int(graph[node[1]][1][count])+node[0]
            kid=graph[node[1]][0][count]
            pq.put([cost, kid])
            count=count+1
            NPC.append([kid,node[1],cost])  
    NPC_A=NPC
    for i in range(NPC_len):
        h=int(heuristic[NPC[i][0]]) 
        fn=NPC[i][2]+h
        NPC_A.append([NPC_A[i].append(h),NPC_A[i].append(fn)])  
    for i in range(NPC_len):
        NPC_A.pop()   
    for k in range(NPC_len):
        pqa.put([NPC_A[k][4],[NPC_A[k][0],NPC_A[k][1],NPC_A[k][2]]])
    for k in range(NPC_len):
        nod=pqa.get()
        if nod[1] not in data:
            data.append(nod[1])
    for b in range(NPC_len):
        if start==data[b][0]:
            way.append([start,0])
            for d in range(NPC_len):
                if data[b][0] == data[d][1]:
                    way.append([data[d][0], data[d][2]])
                    way=find_way(d,data,start,end,NPC_len,way)
                    break
    return way         
     
f=open("output.txt",'w')
if algo == "BFS":
    path=bfs(graph_bd, start, end)
    leng=len(path)
    if start==end:
        f.write(start+" "+"0")
    else:
        for i in range(leng):
            co=str(path[i][1])
            f.write(path[i][0]+" "+co+"\n")
            
if algo == "DFS":
    path=dfs(graph_bd, start, end)
    leng=len(path)
    if start==end:
        f.write(start+" "+"0")
    else:
        for i in range(leng):
            co=str(path[i][1])
            f.write(path[i][0]+" "+co+"\n")
            
if algo == "UCS":
    path=uniform_cost_search(graph_u,start,end)
    leng=len(path)
    if start==end:
        f.write(start+" "+"0")
    else:
        for i in range(leng):
            co=str(path[i][1])
            f.write(path[i][0]+" "+co+"\n")
            
if algo == "A*":
    path=A_star(graph_u,start,end)
    leng=len(path)
    if start==end:
        f.write(start+" "+"0")
    else:
        for i in range(leng):
            co=str(path[i][1])
            f.write(path[i][0]+" "+co+"\n")
f.close()

print path
