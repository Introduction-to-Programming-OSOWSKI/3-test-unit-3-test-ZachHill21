def countB(w):
    count = 0
    for i in range (0 ,len(w)):
        if w[i] == "b":
            count = (count + 1) 
    return count
print (countB("bob"))

def removeLast(w):
    x=""
    for i in range (0, len(w)-1):
        x=x+ w[i]
    return x 
print(removeLast("raise"))

def sumBetweenOdd(x, y):
    z=0
    for n in range(x,y):
        z += (n%2)* n
    print(z)
print(sumBetweenOdd(5, 13))

def firstLast(w):
    if (w[0] == w[-1]):
        return True 
    else: 
        return False
print(firstLast("ripple"))