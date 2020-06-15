import random as rnd

list1 = ["product1", "product2", "product3", "product4", "product5", "product6", "product7", "product8", "product9", "product10"]
list2 = list(range(10))
list3 = list(range(10))

for i in range(10):
    list2[i] = rnd.randint(1, 250)
    list3[i] = rnd.randint(100, 999)

print(list1)
print(list2)
print(list3)

mergeList = list(range(10))

for i in range(10):
    mergeList[i] = [list1[i], list2[i], list3[i]]


print(mergeList)