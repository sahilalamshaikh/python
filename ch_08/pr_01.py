def maximum(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        else:
            return num3
    else:
        if num2 > num3:
            return num2
        else:
            return num3


if __name__ == '__main__':
    m = maximum(4, 5, 6)
    print("The value of maximum is " + str(m))
