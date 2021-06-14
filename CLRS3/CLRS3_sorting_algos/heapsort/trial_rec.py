def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_pal(str):
    if len(str) == 1:
        return True

    if first(str) == last(str) and len(str) > 1:
        return is_pal(middle(str))
    else:
        return False


if __name__ == '__main__':
    print(is_pal("redivider"))
    print(is_pal("redividera"))