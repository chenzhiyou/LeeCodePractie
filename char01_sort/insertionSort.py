# 插入排序
# 原理：讲数列分成两部分，数列的第一个数为left部分，其他部分为right部分，然后将right部分中的数注意取出，插入left部分中
# 合适的位置，让right部分为空时，left部分就成为了一个有序数列
from char01_sort.randomList import random_list


def insertion_sort():
    ilist = random_list(20)
    print(ilist)
    if len(ilist) <= 1:
        return ilist
    for right in range(1, len(ilist)):
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
