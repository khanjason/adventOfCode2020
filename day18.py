li=[]
import re
with open('day18input.txt') as f:
    l=f.readline()
    while l:
        r=l.strip().replace('(','( ')
        r=r.replace(')',' )')
        li.append(r)
        l=f.readline()

#i was stuck on this one, thanks to a friend who suggested using RPN ;)
class StackClass:

    def __init__(self, itemlist=[]):
        self.items = itemlist

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def peek(self):
        return self.items[-1:][0]

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)
        return 0






#adapted from stackoverflow
def infixtopostfix(infixexpr):

    s=StackClass()
    outlst=[]
    prec={}
    prec['/']=3
    prec['*']=2
    prec['+']=2
    prec['-']=2
    prec['(']=1
    oplst=['/','*','+','-']

    tokenlst=infixexpr.split()
    for token in tokenlst:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            outlst.append(token)
        
        elif token == '(':
            s.push(token)
        
        elif token == ')':
            topToken=s.pop()
            while topToken != '(':
                outlst.append(topToken)
                topToken=s.pop()
        else:
            while (not s.isEmpty()) and (prec[s.peek()] >= prec[token]):
                
                outlst.append(s.pop())
                
            
            s.push(token)
            

    while not s.isEmpty():
        opToken=s.pop()
        outlst.append(opToken)
        
    return outlst
    
#https://leetcode.com/problems/evaluate-reverse-polish-notation/discuss/971487/Python-stack-implementation
def eval( left, right, operation):
        if operation == '+':
            return left + right
        elif operation == '-':
            return left - right
        elif operation == '*':
            return left * right
        if operation == '/':
            return int(left / right)
    
def evalRPN(tokens):
    stack = []
    operators = ['*','/','+','-']

    for item in tokens:
        if item in operators:
            right = stack.pop()
            left = stack.pop()

            stack.append(eval(left, right, item))
        else:
            stack.append(int(item))

    return stack[0]
#part 1
tot=0


for t in li:
    
    
    tm=(infixtopostfix(t))
    tot+=(evalRPN(tm))

print(tot)

#part 2



#https://stackoverflow.com/questions/11714582/good-infix-to-prefix-implementation-in-python-that-covers-more-operators-e-g
#this rpn implementation allowed me to change the precedence

SYMBOL = ['+', '-', '*', '/', '^', 'VAR', '(', ')']
INPUT_PRECEDENCE = [3, 1, 1, 3, 6, 7, 9, 0]
STACK_PRECEDENCE = [4, 2, 2, 4, 5, 8, 0, None]
RANK = [-1, -1, -1, -1, -1, 1, None, None]

def getIndex (symbol):
    if (symbol.isalnum()):
        index = 5
    else:
        index = SYMBOL.index (symbol)
    return index



def InfixToReversePolish (INFIX):
    #initialize
    POLISH = []
    STACK = []
    #append ')' to infix
    INFIX = INFIX + ')'
    #push '(' on to the stack
    STACK.append (SYMBOL[6])
    for i in range(0, len(INFIX)):
        #read the next char in the infix
        NEXT = INFIX[i]
        #what is the index of next in the precedence and rank tables?
        index = getIndex (NEXT)
        if (len (STACK) == 0):
            print ('Invalid input string')
            return
        #if we encounter ')', we pop the stack till we find '('. we discard both '(' and ')'
        if index == 7:
            ch = STACK.pop()
            while getIndex (ch) != 6:
                POLISH.append (ch)
                ch = STACK.pop()
            continue
        #while next input precedence is less than or equal to the top stack precedence    
        while (INPUT_PRECEDENCE[index] <= STACK_PRECEDENCE[getIndex(STACK[len(STACK) - 1])]):
            POLISH.append (STACK.pop())
        #push next on to the stack
        STACK.append (NEXT)
    return POLISH
tot=0
for t in li:
    
    INFIX=t.replace(' ','')
    ex = (InfixToReversePolish (INFIX))

    tot+=(evalRPN(ex))
print(tot)
