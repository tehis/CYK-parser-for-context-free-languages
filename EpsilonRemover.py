def findEpsPro(prods):
    for left, right in prods.items():
        if "e" in right:
            return left
    return None


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

def removeEmptyStrings(prods):
    for prod in prods:
        right = prods[prod]
        for idx, p in enumerate(prods[prod]):
            if p == '':
                del prods[prod][idx]
            if len(prods[prod]) == 0:
                del prods[prod]

def removeEps(prods):
    while True:
        epsilonPro = findEpsPro(prods)
        print("epsPro : ", epsilonPro)

        if epsilonPro is None:
            break

        # delete epsilon rule
        prods[epsilonPro].remove("e")

        for left in prods:
            rightHand  = prods[left]
            newProds = []

            for p in rightHand:
                numberOfEpsPro = p.count(epsilonPro)
                if numberOfEpsPro == 0:
                    newProds.append(p)
                else:
                    newProds.extend(calcAllCombinations(p, numberOfEpsPro, epsilonPro))

            removeDuplicatdPros(newProds)
            prods[left] = newProds
    removeEmptyStrings(prods)
