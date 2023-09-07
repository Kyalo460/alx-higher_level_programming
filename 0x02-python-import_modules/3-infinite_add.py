#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    ac = len(argv)

    if ac < 2:
        print("0")

    else:
        ans = 0
        index = 1

        for num in range(1, ac):
            ans += int(argv[index])
            index += 1

        print("{:d}".format(ans))
