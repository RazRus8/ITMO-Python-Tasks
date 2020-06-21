#2
def negative_positive(*params):
    negative = list()
    positive = list()
    
    for i in params:
        if i < 0:
            negative.append(i)
        else:
            positive.append(i)

    negative.sort(reverse=True)
    positive.sort()

    tuple_lists = list(zip(negative, positive))

    return tuple_lists

t = negative_positive(-5,-3,-8,4,9,2,-2,-1,7,-7)

print(t)