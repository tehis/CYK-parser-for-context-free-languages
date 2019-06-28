def checkRechable(left, var, numberOfCall):
    if numberOfCall == n:
        return False
    numberOfCall += 1
    # print(f"left {left}, var : {var}")
    res = False
    for right in prods[left]:
        # print(f"r : {right}")
        for r in right:
            if var in r:
                return True
    for right in prods[left]:
        for r in right:
            if r != "S" and r.isupper():
                res = res or checkRechable(r, var, numberOfCall)
    return res

def removeUnrechable():
    for prod in list(prods):
        if prod == "S":
            continue
        if not checkRechable("S", prod, 0):
            del prods[prod]

def checkUsefulness(useful, s):
    for s1 in s:
        if s1.isupper() and (s1 not in useful):
            return False
    return True

def findTerminalVars(prods, useful):
    for left in prods:
        for right in prods[left]:
            if right.islower():
                useful.add(left)

def findUseful(prods, useful):
    for i in range(len(prods)):
        for prod in prods:
            for right in prods[prod]:
                if checkUsefulness(useful, right):
                    useful.add(prod)

def removeUselessRules(prods1):
    global prods
    prods = prods1
    useful = set()

    findTerminalVars(prods, useful)
    findUseful(prods, useful)

    global n
    n = len(prods)
    for prod in list(prods):
        if prod not in useful:
            del prods[prod]
            continue
        for right in prods[prod]:
            for var in right:
                if var.isupper() and var not in useful:
                    prods[prod].remove(right)
    # print(prods)
    removeUnrechable()




