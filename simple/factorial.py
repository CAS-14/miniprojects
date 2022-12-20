def fact(num):

    num = int(num)
    fin = num
    new = num

    for i in range(num-3):
        new -= 1
        fin = num * fin

    return fin

print(fact(input("> ")))
