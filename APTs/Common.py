def count(a, b):
    """
    return the integer number of characters in common
    to Strings a and b as described below
    """

    length = len(a)
    count = 0
    for i in range(length):
        if a[i] in b:
            index = b.find(a[i])
            b = b[:index] + b[(index + 1):]
            count += 1
    return count


if __name__ == '__main__':
    print(count("toots", "stout"))
    print(count("toots", "stout"))
