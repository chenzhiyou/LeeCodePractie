import random


def random_list(n):
    iList = []
    for i in range(n):
        iList.append(random.randrange(1000))
    return iList