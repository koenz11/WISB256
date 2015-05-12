
def findRoot(f, a, b, epsilon):
    #solutions = []
    
    m = float((a + b)/2)
    if abs(b-a) < float(epsilon):
        #solutions.append(m)
        return m
    else:
        left = f(a)
        if left == 0:
            return a
        right = f(b)
        if right == 0:
            return b
        middle = f(m);
        if middle == 0:
            return m
        if left*middle <= 0:
            #print("left*middle: {0} = {1} * {2}".format(left*middle, left, middle))
            return findRoot(f, a, m, epsilon)
            #solutions.extend(findRoot(f, a, m, epsilon))
        elif right*middle <= 0:
            #print("right*middle: {0} = {1} * {2}".format(right*middle, right, middle))
            return findRoot(f, b, m, epsilon)
            #solutions.extend(findRoot(f, m, b, epsilon))
        #return solutions



def findAllRoots(f, a, b, epsilon):
    solutions = []
    
    m = float((a + b)/2)
    if abs(b-a) < float(epsilon):
        solutions.append(m)
    else:
        left = f(a)
        if left == 0:
            solutions.append(a)
            a = a+epsilon;
            left = f(a);
        right = f(b)
        if right == 0:
            solutions.append(b)
            solutions.extend(findAllRoots(f, m, b-epsilon, epsilon))
            b = b+epsilon;
            right = f(b);
        middle = f(m);
        if middle == 0:
            solutions.append(m)
            solutions.extend(findAllRoots(f, a, m-epsilon, epsilon))
            solutions.extend(findAllRoots(f, m+epsilon, b, epsilon))
            return solutions
        
        if left*middle <= 0:
            #print("left*middle: {0} = {1} * {2}".format(left*middle, left, middle))
            #return findRoot(f, a, m, epsilon)
            solutions.extend(findAllRoots(f, a, m, epsilon))
        if right*middle <= 0:
            #print("right*middle: {0} = {1} * {2}".format(right*middle, right, middle))
                #return findRoot(f, b, m, epsilon)
            solutions.extend(findAllRoots(f, m, b, epsilon))
    
    return solutions
