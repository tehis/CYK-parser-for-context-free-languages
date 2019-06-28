# def findEpsPro(prods):
#     for left, right in prods.items():
#         if "e" in right:
#             return left
#     return None
#
#
# def calcAllCombinations(specificRight, numberOfEpsPro, epPro):
#     newSpecialProds = []
#     for i in range(2**numberOfEpsPro):
#         n = 0
#         # tempProd = []
#         tempProd = ""
#         for p in specificRight:
#             if p == epPro:
#                 if i & (1 << n):
#                     tempProd += p
#                 n += 1
#             else:
#                 tempProd += p
#         newSpecialProds.append(tempProd)
#     return newSpecialProds
#
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
#
# def removeEps(prods):
#     while True:
#         epsilonPro = findEpsPro(prods)
#
#         if epsilonPro is None:
#             break
#
#         # delete epsilon rule
#         prods[epsilonPro].remove("e")
#
#         for left in prods:
#             rightHand  = prods[left]
#             newProds = []
#
#             for p in rightHand:
#                 numberOfEpsPro = p.count(epsilonPro)
#                 if numberOfEpsPro == 0:
#                     newProds.append(p)
#                 else:
#                     newProds.extend(calcAllCombinations(p, numberOfEpsPro, epsilonPro))
#
#             removeDuplicatdPros(newProds)
#             prods[left] = newProds
#     removeEmptyStrings(prods)

def addAll(prod, right, nullable, newGrammar):
    nullableIndices = []

    for i, r in enumerate(right):
        if r in nullable:
            nullableIndices.append(i)
    if len(nullableIndices) == 0:
        if prod in newGrammar:
            newGrammar[prod].append(right)
        else:
            newGrammar[prod] = [right]
        return

    nP = len(nullableIndices)
    # print(f"right = {right}")
    # print((f"nullable indices = {nullableIndices}"))
    for n in range(2**nP):
        tmp = []
        mustBeRemoveIndex = []
        nBin = "{0:b}".format(n)
        nBin = (nP - len(nBin)) * '0' + nBin
        for i, p in enumerate(nBin):
            if p == '0':
                tmp.append(i)
        # print("tmp = ", tmp)
        # print("nbin = ", nBin)
        for x in tmp:
            mustBeRemoveIndex.append(nullableIndices[x])
        # print(f"nust remove indices : {mustBeRemoveIndex}")
        newRight = ""
        for i in range(len(right)):
            if i not in mustBeRemoveIndex:
                newRight += right[i]
        # print(f"new right : {newRight}")
        if prod in newGrammar:
            newGrammar[prod].append(newRight)
        else:
            newGrammar[prod] = [newRight]
        # print("new grammer : ", newGrammar)




def deleteFromAllRules(prods, var):
    for prod in prods:
        for right in prods[prod]:
            right.remove(var)
    removeEmptyStrings(prods)



def findNullable(prods):
    nullable = set()
    for i in range(len(prods)):
        for prod in list(prods):
            rightHand = prods[prod]
            if "e" in rightHand:
                if len(rightHand) == 1:
                    del prods[prod]
                    deleteFromAllRules(prods, prod)
                else:
                    rightHand.remove("e")
                    nullable.add(prod)
                continue

            for right in rightHand:
                nullableRight = True
                for r in right:
                    if r.islower() or (r not in nullable):
                        nullableRight = False
                if nullableRight:
                    nullable.add(prod)
    return nullable

def removeEpsilon(prods):
    nullable = findNullable(prods)
    newGrammar = {}
    # print(f"nullables : {nullable}")
    for prod in prods:
        for right in prods[prod]:
            addAll(prod, right, nullable, newGrammar)
    removeEmptyStrings(newGrammar)
    removeDuplicatdPros(newGrammar)
    return  newGrammar



