# 插入排序
from char01_sort.randomList import random_list


def insertion_sort():
    ilist = random_list(20)
    print(ilist)
    if len(ilist) <= 1:
        return ilist
    for right in range(1,len(ilist)):
        target = ilist[right]
        for left in range(0, right):
            if target <= ilist[left]:
                ilist[left+1: right+1] = ilist[left:right]
                ilist[left] = target
                break
    return ilist


if __name__ == "__main__":
    ilist = insertion_sort()
    print(ilist)
