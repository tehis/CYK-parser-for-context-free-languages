from EpsilonRemover import *
from UnitRemover import *
from Useless import *
from GetCNF import *

def printGrammer():
    print("========================================")
    for left in prods:
        print(left, " -> ", end="")
        for r in prods[left]:
            print(r, " | ", end="")
        print()
    print("=========================================")
def getInput():
    while True:
        prod = input().split("->")
        if prod == ['$']:
            break

        # print("prod = ",  prod)
        leftSide = prod[0].replace(" ", "")
        rightSide = prod[1].replace(" ", "")

        prods[leftSide] = rightSide.split("|")

if __name__ == '__main__':
    prods = dict()
    print("Enter grammar!")
    getInput()
    # printGrammer()

    print("Remove epsilon rules")
    removeEps(prods)
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

    print("CYK algorithm")


