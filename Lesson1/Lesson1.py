cost = [10, 15, 12, 40, 52, 27, 90, 33, 18, 75]
price = list(cost)

for i in range(0, 9):
    price[i] = cost[i] * 1.20

for i in price:
    print(i)