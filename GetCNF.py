import string
import random

# def isCNF():
def generateNewVar(prods):
    al = list(string.ascii_uppercase)
    while True:
        a = random.choice(al)
        if a not in prods:
            return a


def handlingRrulesOfLengthTwo(prods):
    neededRules = set()
    for left, rightHand in prods.items():
        for right in rightHand:
            if len(right) == 2:
                neededRules.add((left, right))

    for left, right in neededRules:
        r = list(right)

        newVar1 = generateNewVar(prods)

        # if both of them are terminal
        if r[0].islower() and r[1].islower():
            newVar2 = generateNewVar(prods)
            while newVar1 == newVar2:
                newVar2 = generateNewVar(prods)
            prods[newVar1] = [r[0]]
            prods[newVar2] = [r[1]]
            prods[left].remove(right)
            prods[left].append(newVar1 + newVar2)
        elif r[0].islower():
            prods[newVar1] = [r[0]]
            prods[left].remove(right)
            prods[left].append(newVar1 + r[1])
        elif r[1].islower():
            prods[newVar1] = [r[1]]
            prods[left].remove(right)
            prods[left].append(r[0] + newVar1)


def addNewStartVar(prods):
    pass

def convertToCnf(prods):

    # Hanling very long rules
    while True:
        longRule = None
        for left, rightHand in prods.items():
            for right in rightHand:
                if len(right) > 2:
                    longRule = (left, right)
        if longRule is None:
            break

        left, right = longRule
        restOfRight = right[1:]
        newVar = generateNewVar(prods)
        prods[left].remove(right)
        prods[left].append(right[0] + newVar)
        prods[newVar] = [restOfRight]

    #handling two
    handlingRrulesOfLengthTwo(prods)

def checkCNF(prods):
    for prod in prods:
        rightHand = prods[prod]
        for right in rightHand:
            if right == "e":
                return False
            if len(right) > 2:
                return False
            else:
                if len(right) == 1 and right.isupper():
                    return False
                if len(right) == 2:
                    if right[0].islower() or right[1].islower():
                        return False
    return True









