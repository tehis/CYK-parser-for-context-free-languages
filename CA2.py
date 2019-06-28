from EpsilonRemover import *
from UnitRemover import *
from Useless import *
from GetCNF import *
from CYK import *


def printGrammer():
    print("========================================")
    for left in prods:
        print(left, " -> ", end="")
        for r in prods[left]:
            print(r, " | ", end="")
        print()
    print("=========================================")
def getGrammar():
    while True:
        prod = input().split("->")
        if prod == ['$']:
            break

        # print("prod = ",  prod)
        leftSide = prod[0].replace(" ", "")
        rightSide = prod[1].replace(" ", "")

        prods[leftSide] = rightSide.split("|")

def getWord():
    print("Enter your words to check membership:")
    while True:
        word = input().strip()
        if word == "$":
            break
        if checkMembership(prods, word):
            print("Accepted")
        else:
            print("Rejected")

if __name__ == '__main__':
    prods = dict()
    print("Enter grammar!")
    getGrammar()

    if not checkCNF(prods):
        print("The grammar is not CNF")
        print("Remove epsilon rules")
        prods = removeEpsilon(prods)
        printGrammer()

        print("Remove unit rules")
        removeUnitRules(prods)
        printGrammer()

        print("Remove Useless rules")
        removeUselessRules(prods)
        printGrammer()

        print("Convert to chomsky form")
        convertToCnf(prods)
        printGrammer()
    else:
        print("The grammar is CNF")

    getWord()




