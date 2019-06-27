from EpsilonRemover import *

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
    prod = ''
    getInput()
    print(prods)

    removeEps()
    print(prods)