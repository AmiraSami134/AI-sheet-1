
from __future__ import print_function
import shop


def shopSmart(orderList, fruitShops):
   
    Cost1 = fruitShops[0].getPriceOfOrder(orderList)
    Cost2 = fruitShops[1].getPriceOfOrder(orderList)
    if (Cost1 > Cost2):
        shop=fruitShops[1]
    else:
        shop=fruitShops[0]
    return shop 


if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orders = [('apples', 1.0), ('oranges', 3.0)]
    
    dir1 = {'apples': 2.0, 'oranges': 1.0}
    shop1 = shop.FruitShop('shop1', dir1)
    
    dir2 = {'apples': 1.0, 'oranges': 5.0}
    shop2 = shop.FruitShop('shop2', dir2)
    
    shops = [shop1, shop2]
    print("For orders ", orders, ", the best shop is", shopSmart(orders, shops).getName())
    orders = [('apples', 3.0)]
    print("For orders: ", orders, ", the best shop is", shopSmart(orders, shops).getName())
