# def calcVariablesOfLength1(prods, table, word, n):
#     for i in range(n):
#         for left, rightHand in prods.items():
#             if word[i] in rightHand:
#                 table[left][i][i+1] = True
#
#
# def runCYK(prods, word, n):
#     table = {nonTerm : [[False for i in range(n+1)] for j in range(n+1)]
#                         for nonTerm in prods.keys()}
#
#     calcVariablesOfLength1(prods, table, word, n)
#
#     # fill table from words of lenght 2 to n
#     for l in range(2, n+1):
#         for i in range(n - l + 1):
#             j = i + l
#             for left, rightHand in prods.items():
#                 for right in rightHand:
#                     if len(right) == 2:
#                         for k in range(i+1, j):
#                             if table[right[0]][i][k] and table[right[1]][k][j]:
#                                 table[left][i][j] = True
#     return table["S"][0][n]

def getComb(prods, table, i, j, k):
    B = table[i][k]
    C = table[k][j]
    for prod in prods:
        rightHand = prods[prod]
        for right in rightHand:
            if len(right) == 2:
                if right[0] in B and right[1] in C:
                    table[i][j].add(prod)

def runCYK2(prods, word):
    n = len(word)
    table = [[ {None} for i in range(n+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for prod in prods:
            if word[i-1] in prods[prod]:
                table[i-1][i].add(prod)
    for j in range(2, n+1):
        for i in range(j-2, -1, -1):
            for k in range(i+1, j):
                """
                  add new variable "A" to table[i,j] if A-> BC 
                  and B belongs to table[i,k]
                  and C belongs to table[k,j
                """
                getComb(prods, table, i, j, k)
    if "S" in table[0][n]:
        return True
    return False

def checkMembership(prods, word):
    n = len(word)
    return runCYK2(prods, word)
    # return runCYK(prods, word, n)