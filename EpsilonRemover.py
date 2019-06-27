def findEpsPro():
    for left, right in prods.items():
        if left == 'S':
            continue
        for i in range(len(right)):
            if right[i] == 'e':
                return left, i
    return None, None


def calcAllCombinations(specificRight, numberOfEpsPro, epPro):
    newSpecialProds = []
    for i in range(2**numberOfEpsPro):
        n = 0
        # tempProd = []
        tempProd = ""
        for p in specificRight:
            if p == epPro:
                if i & (1 << n):
                    tempProd += p
                n += 1
            else:
                tempProd += p
        newSpecialProds.append(tempProd)
    return newSpecialProds

def removeDuplicatdPros(newProds):
    newProds = sorted(newProds)
    newProds = [newProds[i] for i in range(len(newProds))
                            if i == 0 or newProds[i] != newProds[i-1]]

def removeEps():
    while True:
        epsilonPro, indexOfEpsilon  = findEpsPro()
        if epsilonPro is None:
            break

        del prods[epsilonPro][indexOfEpsilon]
        print("epsilon pro : ", epsilonPro)

        for left in prods:
            right  = prods[left]
            newProds = []

            for p in right:
                numberOfEpsPro = p.count(epsilonPro)
                if numberOfEpsPro == 0:
                    newProds.append(p)
                else:
                    newProds.extend(calcAllCombinations(p, numberOfEpsPro, epsilonPro))

            removeDuplicatdPros(newProds)
            prods[left] = newProds





if __name__ == '__main__':
    prods = dict()
    prod = ''
    getInput()
    print(prods)

    removeEps()
    print(prods)


