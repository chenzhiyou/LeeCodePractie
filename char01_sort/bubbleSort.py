# 冒泡排序
# 时间复杂度为O(n*n)
# 原理：通过不断交换大数的位置达到排序的目的
from char01_sort.randomList import random_list


def bubble_sort():
    ilist = random_list(20)
    print(ilist)
    if len(ilist) <= 1:
        return ilist
    for i in range(1, len(ilist)):
        for j in range(0, len(ilist)-i):
            if ilist[j] > ilist[j+1]:
                ilist[j], ilist[j+1] = ilist[j+1], ilist[j]
    return ilist


if __name__ == "__main__":
    ilist = bubble_sort()
    print(ilist)
