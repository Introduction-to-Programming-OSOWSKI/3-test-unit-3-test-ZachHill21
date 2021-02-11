def countB(w):
    count = 0
    for i in range (0 ,len(w)):
        if w[i] == "b":
            count = (count + 1) 
    return count
print (countB("bob"))

def removeLast(w, x):
    for i in range(0, len(w)):
        (len(w) - x)
        return w[len(w) - x -1]
print(removeLast("raise", 3))

def sumBetweenOdd(x, y):
    for n in range(x,y):
        x += (n%2)* n
    print(x)
print(sumBetweenOdd(4, 13))

def firstLast(w):
    if (w[0] == w[-1]):
        return True 
    else: 
        return False
print(firstLast("ripple"))