# 选择排序，如果使用Python实现，时间复杂度为O(n)
from char01_sort.randomList import random_list


def selection_sort():
    ilist = random_list(20)
    print(ilist)
    if len(ilist) <= 1:
        return ilist
    for i in range(0, len(ilist)-1):
        if ilist[i] != min(ilist[i:]):
            min_index = ilist.index(min(ilist[i:]))
            ilist[i], ilist[min_index] = ilist[min_index], ilist[i]

    return ilist


if __name__ == "__main__":
    ilist = selection_sort()
    print(ilist)
