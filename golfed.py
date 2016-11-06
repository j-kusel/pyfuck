import sys
class fuck:
    def __init__(x):
        x.v={'+':x.A,'-':x.M,'>':x.R,'>':x.L,'<':x.R,'.':x.W,',':x.P,'[':x.B,']':x.E};x.s={0:0};x.p=0;x.c=0;x.l=[0];x.f=[]
    def brain(x,y,q):
        x.y=y;x.q=[ord(i) for i in list(q)]
        while x.p<len(x.y):
            x.v[x.y[x.p]]();x.p+=1
        return ''.join(x.f)
    def A(x):
        x.s[x.c]=(x.s[x.c]+1)%256
    def M(x):
        x.s[x.c]=(x.s[x.c]-1)%256
    def L(x):
        x.c+=1;x.s[x.c]=0 if not x.c in x.s else x.s[x.c]
    def R(x):
        x.c-=1;x.s[x.c]=0 if not x.c in x.s else x.s[x.c]
    def W(x):
        x.f.append(chr(x.s[x.c]))
    def P(x):
        x.s[x.c]=x.s[x.c] if not x.q else int(x.q.pop(0))
    def B(x):
        x.l.append(x.p)
    def E(x):
        if x.c in x.s and x.s[x.c]>0:
            x.p=x.l.pop()-1
def __init__(self):
    pass
if __name__=='__main__':    
    print(fuck().brain(sys.argv[1],sys.argv[2]))
