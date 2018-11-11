class StackUnderflowError(Exception):
    pass

stack = []

def add():
    if(len(stack) < 2 ):raise StackUnderflowError("Cannot apply +")
    num2 , num1 = stack[-2:]
    ans = num2 + num1
    del stack[-2:]
    stack.append(ans)

def sub():
    if(len(stack) < 2 ):raise StackUnderflowError("Cannot apply -")
    num2 , num1 = stack[-2:]
    ans = num2 - num1
    del stack[-2:]
    stack.append(ans)

def mul():
    if(len(stack) < 2 ):raise StackUnderflowError("Cannot apply *")
    num2 , num1 = stack[-2:]
    ans = num2 * num1
    del stack[-2:]
    stack.append(ans)

def div():
    if(len(stack) < 2 ):raise StackUnderflowError("Cannot apply /")
    num2 , num1 = stack[-2:]
    if(num1 == 0):raise ZeroDivisionError("Number cannot be Divided with 0")
    ans = num2 // num1
    del stack[-2:]
    stack.append(ans)

def drop():
    if(len(stack) < 1 ):raise StackUnderflowError("Cannot Drop")
    del stack[-1]

def dup():
    if(len(stack) < 1 ):raise StackUnderflowError("Cannot Drop")
    stack.append(stack[-1])

def swap():
    if(len(stack) < 2 ):raise StackUnderflowError("Cannot apply Swap")
    num2 , num1 = stack[-2:]
    del stack[-2:]
    stack.append(num1)
    stack.append(num2)

def over():
    if(len(stack) < 2 ):raise StackUnderflowError("Cannot apply Over")
    num = stack[-2]
    stack.append(num)

common_func = {
"+" : add ,
"-" : sub ,
"*" : mul ,
"/" : div ,
"drop" : drop ,
"dup" : dup ,
"swap" : swap ,
"over" : over ,
}

userdefined = {}


def processuser(expr):
    if(len(expr) == 1):raise ValueError("Not Valid Evaluation")
    key = expr[0]
    if(key.isnumeric()):raise ValueError("Cannot key Numeric Values")
    del expr[0]
    expr = processstat(expr)
    userdefined[key] = expr

def processstat(expr):
    print(userdefined)
    while True:
        i = 0
        flag = True
        while i < len(expr):
            if(expr[i] in userdefined.keys()):
                expr = expr[0:i] + userdefined[expr[i]] + expr[i+1:]
                flag = False
            elif(expr[i] in common_func.keys() or expr[i].isnumeric() ):
                pass
            else:
                raise ValueError("Invalid userdefined Variable")
            i +=1
        if(flag):break
    return expr


def evaluate(input_data):
    global stack
    global userdefined
    stack = []
    userdefined = {}
    input_data = [i.lower() for i in input_data]
    for i in input_data:
        exprs = i.split()
        if(exprs[0] == ":" and exprs[-1] == ";"):
            processuser(exprs[1:-1])
            continue
        exprs = processstat(exprs)
        for j in exprs:
            if( j.isnumeric()):
                stack.append(int(j))
            else:
                if( j in common_func.keys() ):
                    common_func[j]()

    return stack
