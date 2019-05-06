def theIndex(carrots, amount):
    amountLeft = amount
    while amountLeft > 0:
        largestBoxAmt = -9999
        largestBoxIndex = -9999
        for i in carrots:
            if i > largestBoxAmt:
                largestBoxAmt = i
                largestBoxIndex = carrots.index(i)
        carrots[largestBoxIndex] -= 1
        amountLeft -= 1
    return largestBoxIndex