#!/usr/bin/python3
for num in range(0, 100):
    if num < 10:
        num = "0{}, ".format(num)

    elif num < 99:
        num = "{}, ".format(num)

    print("{}".format((num)), end='')

    if num == 99:
        print("")
