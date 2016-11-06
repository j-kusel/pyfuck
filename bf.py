import sys
DEBUG = False

class fuck:
    def __init__(self):
        self.command = {'+':self._plus,'-':self._minus,'>':self._right,'>':self._left,'<':self._right,'.':self._out,',':self._read,'[':self._loopleft,']':self._loopright}
        self.stack = {0:0,}
        self.pointer = 0
        self.cell = 0
        self.loops = [0,]

    def brain(self,code,input):
        self.code = code
        self.input = [ord(i) for i in list(input)]
        while self.pointer < len(self.code):
            self.command[self.code[self.pointer]]()
            self.pointer += 1
        return DEBUG and self.stack or ''.join([chr(self.stack[s]) for s in range(0,len(self.stack))])

    def _plus(self):
        self.stack[self.cell] += 1
    def _minus(self):
        self.stack[self.cell] -= 1
    def _left(self):
        print('left')
        self.cell += 1
        self.stack[self.cell] = 0 if not self.cell in self.stack else self.stack[self.cell]
    def _right(self):
        print('right')
        self.cell -= 1
        self.stack[self.cell] = 0 if not self.cell in self.stack else self.stack[self.cell]
    def _out(self):
        print(self.stack[self.cell])
    def _read(self):
        print('read')
        self.stack[self.cell] = self.stack[self.cell] if not self.input else int(self.input.pop(0))
    def _loopleft(self):
        print('leftloop')
        self.loops.append(self.pointer)
    def _loopright(self):
        print('rightloop')
        if self.cell in self.stack and self.stack[self.cell] > 0:
            self.pointer = self.loops.pop() - 1

def main(st, input):
    interpreter = fuck(st, input)
    print(interpreter.brain())

if __name__ = '__main__':    
    main(sys.argv[1], sys.argv[2])
