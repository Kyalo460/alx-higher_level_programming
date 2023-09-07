#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    ac = len(argv) - 1
    arg = "arguments:"

    if (ac == 1):
        arg = "argument:"
    elif (ac == 0):
        arg = "arguments."

    print("{:d} {:s}".format(ac, arg))

    if ac >= 1:
        index = 1

        for av in range(1, ac + 1):
            print("{:d}: {:s}".format(index, argv[index]))
            index += 1
