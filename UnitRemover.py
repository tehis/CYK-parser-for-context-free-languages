def removeUnitRules(prods):
    while True:
        unitRule = None
        for left, rightHand in prods.items():
            for idx, r in enumerate(rightHand):
                if len(r) == 1 and r.isupper():
                    unitRule = (left, r, idx)
        if unitRule is None:
            break

        left, right, rightIdx = unitRule[0], unitRule[1], unitRule[2]
        # print(left, " ", right, " ", rightIdx)

        # Remove A -> B
        del prods[left][rightIdx]

        # Replace B -> x
        for right2 in prods.get(right):
            prods[left].append(right2)

