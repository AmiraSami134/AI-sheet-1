from __future__ import print_function

fruitPrices = {'apples': 2.00, , 'pears': 1.75,
               'limes': 0.75, }

def buyLotsOfFruit(orderList):
    
    totalCost = 0.0
    totalCost = (2*orderList[0][1]+1.75*orderList[1][1]+0.75*orderList[2][1])
    
    return totalCost

# Main Method
if __name__ == '__main__':
    orderList = [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)]
    print('Cost of', orderList, 'is', buyLotsOfFruit(orderList))
