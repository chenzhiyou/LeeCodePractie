# 冒泡排序
import random


def random_list(n):
    iList = []
    for i in range(n):
        iList.append(random.randrange(1000))
    return iList


def bubble_sort():
    ilist = random_list(20)
    if len(ilist) <= 1:
        return ilist
    for i in range(1, len(ilist)):
        for j in range(0, len(ilist)-1):
            if ilist[j] > ilist[j+1]:
                ilist[j], ilist[j+1] = ilist[j+1], ilist[j]
            print(ilist)
    return ilist


if __name__ == "__main__":
    ilist = bubble_sort()
    print(ilist)
