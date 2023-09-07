#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    strings = dir(hidden_4)
    index = 9

    for n in range(9, 12):
        print("{:s}".format(strings[index]))
        index += 1
