def whichOrder(available, orders):
    orderWorking = []
    numOfTotalOrders = len(orders)
    for i in range(numOfTotalOrders):
        order = orders[i]
        orderIngredients = order.split()
        if set(orderIngredients) <= set(available):
            val = 'Yes'
        else:
            val = 'Not'
        orderWorking.append(val)
    if 'Yes' in orderWorking:
        return orderWorking.index('Yes')
    else:
        return -1