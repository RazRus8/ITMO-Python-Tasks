#1
degree_list = [16, None, 20, 22, None, 21, 19, None, 16]

def clearing_list(degree_list):
    clear_list = list()
    for i in degree_list:
        if i != None:
            clear_list.append(i)
    return clear_list

def average_value(degree_list):
    return sum(degree_list) / len(degree_list)

print(clearing_list(degree_list))
print(average_value(clearing_list(degree_list)))