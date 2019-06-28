def calcVariablesOfLength1(prods, table, word, n):
    for i in range(n):
        for left, rightHand in prods.items():
            if word[i] in rightHand:
                table[left][i][i+1] = True


def runCYK(prods, word, n):
    table = {nonTerm : [[False for i in range(n+1)] for j in range(n+1)]
                        for nonTerm in prods.keys()}

    calcVariablesOfLength1(prods, table, word, n)

    # fill table from words of lenght 2 to n
    for l in range(2, n+1):
        for i in range(n - l + 1):
            j = i + l
            for left, rightHand in prods.items():
                for right in rightHand:
                    if len(right) == 2:
                        for k in range(i+1, j):
                            if table[right[0]][i][k] and table[right[1]][k][j]:
                                table[left][i][j] = True
    return table["S"][0][n]

def checkMembership(prods, word):
    n = len(word)
    return runCYK(prods, word, n)