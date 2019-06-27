from EpsilonRemover import *
from UnitRemover import *


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
    getInput()
    printGrammer()

    removeEps(prods)
    printGrammer()

    removeUnitRules(prods)
    printGrammer()

