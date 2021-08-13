import re
from itertools import permutations

def solution(expression):
    answer = 0
    ex = re.split('([-+*])',expression)
    oper = list(permutations('+-*',3))

    for op in oper:
        exp = ex.copy()
        for o in op:
            while o in exp:
                i = exp.index(o)
                exp = exp[:i-1] + [calc(o,exp[i-1],exp[i+1])] + exp[i+2:]
        answer = max(answer,abs(int(exp[0])))
    return answer

def calc(op,a,b):
    if op == '+':
        return str(int(a)+int(b))
    elif op == '-':
        return str(int(a)-int(b))
    else:
        return str(int(a)*int(b))