import sys
from copy import deepcopy

file1=open('input.txt', 'r')
N=file1.readline()                                          #N*N board
N= ''.join(c for c in N if c not in '\n ''')
N=int(N)
#print N
mode=file1.readline()                                       #minimax or alphabeta                     
mode=''.join(c for c in mode if c not in '\n ''')
#print mode
play=file1.readline()                                       #play='X' or 'O'
play=''.join(c for c in play if c not in '\n ''')
#print play
d=file1.readline()
d=''.join(c for c in d if c not in '\n ''')
depth_of_search=int(d)
#print depth_of_search

if play=="X":
    enemy="O"
else:
    enemy="X"

heu=[[0 for x in range(N)] for y in range(N)] 
for i in range(N):                                          #heuristic
    h=file1.readline()
    h=h.split()
    for j in range(N):
        heu[i][j]=int(h[j])

#print "Heuristic", heu
    
board=[[0 for x in range(N)] for y in range(N)] 
m=[]
m=file1.read()
m= ''.join(c for c in m if c not in '\n ''')
c=0
for i in range(N):                                          #board status
    for j in range(N):
        board[i][j]=m[c]
        c=c+1
file1.close()
#print "board", board   

class node:
    def __init__(self, n):
        self.n=n
        self.d=0
        self.act=0
        self.u=0
        self.move="Stake"

    def __setitem__(self,n):
        self.n=n

    def get(self,n):
        return self.n
    
    def actions(self,n):
        for i in range(N):
            for j in range(N):
                if self.n[i][j]=='.':
                    self.act=self.act+1
        return self.act
    

def at(n):
        at=0
        for i in range(N):
            for j in range(N):
                if n[i][j]=='.':
                    at=at+1
        return at        


root=node(board)
def terminal(state,d):          #pass the depth and board state
    empty=0
    if d==depth_of_search:
        return True
    else:
        for i in range(N):
            for j in range(N):
                if state[i][j]=='.':
                    empty=empty+1
                
        if empty==0:
            return True
        else:
            return False

def utility(state):
    x=0
    o=0
    for i in range(N):
        for j in range(N):
            if state[i][j]==play:
                x=x+heu[i][j]
            elif state[i][j]!='.' and state[i][j]!=play:
                o=o+heu[i][j]
            else:
                continue
    score=x-o
    return score

def make_obj(c,state,mov):
    child=node(c)
    child.d=state.d+1
    if mov!=0:
        child.move="Raid"
    child.u=utility(child.get(child))
    #print "child", child.get(child)
    return child
    

visit=[]
def successor(state,play):
    c1=deepcopy(state.get(state))
    s1=deepcopy(state.get(state))
    if state.get(state) not in visit:
        visit.append(state.get(state))
    else:
        b=0
        flag=visit.count(state.get(state))
        visit.append(state.get(state))
        for i in range(N):
            for j in range(N):
                if s1[i][j]=="." and b!=flag:
                    if at(s1)>1:
                        s1[i][j]="yee"
                        b=b+1
    move=0
    #print "c1", c1
    #print "s1", s1
    r=range(N)
    for i in range(N):
        for j in range(N):
            if s1[i][j]=='.':
                c1[i][j]=play
                if i-1 in r and j in r:
                    if c1[i-1][j]==play:
                        if i in r and j+1 in r:
                            if c1[i][j+1]!=play and c1[i][j+1]!='.':
                                c1[i][j+1]=play
                                move=move+1
                        if i in r and j-1 in r:
                            if c1[i][j-1]!=play and c1[i][j-1]!='.':
                                c1[i][j-1]=play
                                move=move+1
                        if i+1 in r and j in r:
                            if c1[i+1][j]!=play and c1[i+1][j]!='.':
                                c1[i+1][j]=play
                                move=move+1
                if i in r and j-1 in r:
                    if c1[i][j-1]==play:
                        if i-1 in r and j in r:
                            if c1[i-1][j]!=play and c1[i-1][j]!='.':
                                c1[i-1][j]=play
                                move=move+1
                        if i+1 in r and j in r:
                            if c1[i+1][j]!=play and c1[i+1][j]!='.':
                                c1[i+1][j]=play
                                move=move+1
                        if i in r and j+1 in r:
                            if c1[i][j+1]!=play and c1[i][j+1]!='.':
                                c1[i][j+1]=play
                                move=move+1
                if i+1 in r and j in r:
                    if c1[i+1][j]==play:
                        if i-1 in r and j in r:
                            if c1[i-1][j]!=play and c1[i-1][j]!='.':
                                c1[i-1][j]=play
                                move=move+1
                        if i in r and j+1 in r:
                            if c1[i][j+1]!=play and c1[i][j+1]!='.':
                                c1[i][j+1]=play
                                move=move+1
                        if i in r and j-1 in r:
                            if c1[i][j-1]!=play and c1[i][j-1]!='.':
                                c1[i][j-1]=play
                                move=move+1
                if i in r and j+1 in r:
                    if c1[i][j+1]==play:
                        if i-1 in r and j in r:
                            if c1[i-1][j]!=play and c1[i-1][j]!='.':
                                c1[i-1][j]=play
                                move=move+1
                        if i+1 in r and j in r:
                            if c1[i+1][j]!=play and c1[i+1][j]!='.':
                                c1[i+1][j]=play
                                move=move+1
                        if i in r and j-1 in r:
                            if c1[i][j-1]!=play and c1[i][j-1]!='.':
                                c1[i][j-1]=play
                                move=move+1
                return make_obj(c1,state,move)
 
global v  
ve=[]  
ans=[]
answer=[]
def minimax(state):
    v=max_value(state)
    return v

def max_value(state):
    if terminal(state.get(state),state.d):
        return utility(state.get(state))        
    v=-sys.maxint
    for i in range(state.actions(state)):
        s=successor(state,play)
        v=max(v,min_value(s))
        ve.append(v)
        answer.append(s)
        ans.append(s.get(s))            
    return v

def min_value(state):
    if terminal(state.get(state),state.d):
        return utility(state.get(state))
    v=sys.maxint
    for i in range(state.actions(state)):
        s=successor(state,enemy)
        v=min(v,max_value(s))
        state.ut=v
        ve.append(v)
        answer.append(s)
        ans.append(s.get(s))
    return v
#final_board=[] 
a=[]       
if mode=="MINIMAX":      
    minimax(root)
    lengthh=len(ve)
    last=ve[lengthh-1]
    if depth_of_search==1:
        #print "in if of depth"
        for i in range(lengthh):
            ve[i]=utility(answer[i].get(answer[i]))
        m=max(ve)
        for i in range(lengthh):
            if ve[i]==m:
                #print "finding max"
                a.append(answer[i])
        for i in range((len(a))):
            if a[i].move=="Raid":
                if (len(a))==1:
                    final_board=a[i].get(a[i])
                    final_move=a[i].move
                #print "in if of raid"
                for j in range(i,len(a)):
                    if a[j].move=="Stake":
                        #print "in if of raid stake"
                        final_board=a[j].get(a[j])
                        final_move=a[j].move
                        break
                break
            else:
                #print "in if of stake"
                final_board=a[i].get(a[i])
                final_move=a[i].move
                break   
    else:
        for i in range(lengthh):
            if ve[i]==last and at(ans[i])==at(board)-1:
                final_board=ans[i]
                final_move=answer[i].move
                break
        
  
def alpha_beta(state):
    v=max_val(state,-sys.maxint,sys.maxint)
    return v

def max_val(state, al, be):
    if terminal(state.get(state), state.d):
        return utility(state.get(state))
    v=-sys.maxint
    for i in range(state.actions(state)):
        s=successor(state, play)
        #print s.get(s)
        v=max(v,min_val(s,al,be))
        if v>=be:
            return v 
        al=max(al,v)
        ve.append(v)
        answer.append(s)
        ans.append(s.get(s))
    return v
def min_val(state,al,be):
    if terminal(state.get(state),state.d):
        return utility(state.get(state))
    v=sys.maxint
    for i in range(state.actions(state)):
        s=successor(state, enemy)
        #print s.get(s)
        v=min(v,max_val(s,al,be))
        if v<=al:
            return v
        be=min(be,v)
        ve.append(v)
        answer.append(s)
        ans.append(s.get(s))
    return v    

a=[]

if mode=="ALPHABETA":
    alpha_beta(root)
    lengthh=len(ve)
    last=ve[lengthh-1]    
    if depth_of_search==1:
        #print "in if of depth"
        for i in range(lengthh):
            ve[i]=utility(answer[i].get(answer[i]))
        m=max(ve)
        for i in range(lengthh):
            if ve[i]==m:
                #print "finding max"
                a.append(answer[i])
        for i in range((len(a))):
            if a[i].move=="Raid":
                if (len(a))==1:
                    final_board=a[i].get(a[i])
                    final_move=a[i].move
                #print "in if of raid"
                for j in range(i,len(a)):
                    if a[j].move=="Stake":
                        #print "in if of raid stake"
                        final_board=a[j].get(a[j])
                        final_move=a[j].move
                        break
                break
            else:
                #print "in if of stake"
                final_board=a[i].get(a[i])
                final_move=a[i].move
                break                 
    else:      
        for i in range(lengthh):
            if ve[i]==last and at(ans[i])==at(board)-1:
                final_board=ans[i]
                final_move=answer[i].move
                break

movee=''
for i in range(N):
    for j in range(N):
        if board[i][j]=="." and final_board[i][j]!=".":
            ch=str(i+1)
            movee=chr(65+j)+ ch
            break

print movee, final_move
for k in range(N):
        print final_board[k]     

f=open("output.txt",'w')
f.write(movee+" "+final_move)
f.write('\n')
for k in range(N):
    for j in range(N):
        f.write(final_board[k][j])
    f.write("\n")
    



