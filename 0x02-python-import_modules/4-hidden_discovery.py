#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    strings = dir(hidden_4)
    index = 9

    for name in strings:
        if not name.startswith("__"):
            print(name)
