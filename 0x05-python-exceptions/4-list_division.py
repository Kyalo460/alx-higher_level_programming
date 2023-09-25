#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists"""

    result_list = []

    for n in range(0, list_length):
        try:
            num = my_list_1[n] / my_list_2[n]
            result_list.append(num)

        except IndexError:
            print("out of range")
            result_list.append(0)

        except TypeError:
            print("wrong type")
            result_list.append(0)

        except ZeroDivisionError:
            print("division by 0")
            result_list.append(0)

        finally:
            pass

    return result_list
