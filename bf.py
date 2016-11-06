import sys
DEBUG = False

class fuck:
    def __init__(self,code,input):
        self.code=code
        self.command={'+':self.plus,'-':self.minus,'>':self.right,'>':self.left,'<':self.right,'.':self.out,',':self.read,'[':self.loopleft,']':self.loopright}
        self.stack = {0:0,}
        self.pointer = 0
        self.input = [ord(i) for i in list(input)]
        self.cell = 0
        self.loops = [0,]

    def brain(self):
        while self.pointer < len(self.code):
            self.command[self.code[self.pointer]]()
            self.pointer+=1
        return DEBUG and self.stack or ''.join([chr(self.stack[s]) for s in range(0,len(self.stack))])

    def plus(self):
        self.stack[self.cell]+=1
    def minus(self):
        self.stack[self.cell]-=1
    def left(self):
        print('left')
        self.cell+=1
        self.stack[self.cell]=0 if not self.cell in self.stack else self.stack[self.cell]
    def right(self):
        print('right')
        self.cell-=1
        self.stack[self.cell]=0 if not self.cell in self.stack else self.stack[self.cell]
    def out(self):
        print(self.stack[self.cell])
    def read(self):
        print('read')
        self.stack[self.cell]=self.stack[self.cell] if not self.input else int(self.input.pop(0))
    def loopleft(self):
        print('leftloop')
        self.loops.append(self.pointer)
    def loopright(self):
        print('rightloop')
        if self.cell in self.stack and self.stack[self.cell]>0:
            self.pointer = self.loops.pop()-1
   

def main(st, input):
    interpreter = fuck(st, input)
    print(interpreter.brain())
    
main(sys.argv[1], sys.argv[2])
