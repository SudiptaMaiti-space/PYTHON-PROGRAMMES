
def p1(x):
    for i in range(1,x+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print("")

def p2(x):
    for i in range(1,x+1):
        for j in range(x,i,-1):
            print(" ",end=" ")
        for k in range(1,i+1):
            print("*",end=" ")
        print("")

def p3(x):
    for i in range(1,x+1):
        for j in range(x,i,-1):
            print(" ",end=" ")
        for k in range(1,i+1):
            print("*  ",end=" ")
        print("")

def p4(x):
    a=1
    for i in range(1,x+1):
        for j in range(1,i+1):
            print(a,end=" ")
            a+=1
        a=1
        print("")

def p5(x):
    a=1
    for i in range(1,x+1):
        for j in range(1,i+1):
            print(a,end=" ")
            a+=1
        print("")

