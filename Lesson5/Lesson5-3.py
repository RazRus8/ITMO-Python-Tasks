#3

#first way
def power_number1(number, power):
    result = 1
    while(power != 0):
        result *= number
        power -= 1
    return result

val = power_number1(2, 3)
print("Answer in first way: ", val)

#second way
def power_number2(number, power):
    if power == 0:
        return 1
    else:
        return number * power_number2(number, power - 1)

val = power_number2(2, 3)
print("Answer in second way: ", val)