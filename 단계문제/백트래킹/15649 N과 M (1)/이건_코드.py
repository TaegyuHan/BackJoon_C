import sys
sys.stdin = open('./15649.txt')

n,m=map(int,sys.stdin.readline().strip().split())
        
nlist=[str(x) for x in range(1,n+1)]
mlist=['0']*m

def NandM(nlist,mlist,a=0):
    if a<m:
        for x in nlist:
            mlist=mlist[:a]+["0"]*(m-a)
            if x not in mlist:
                mlist[a]=x
                NandM(nlist,mlist,a+1)
    else:
        print(" ".join(mlist))
            
NandM(nlist,mlist)
