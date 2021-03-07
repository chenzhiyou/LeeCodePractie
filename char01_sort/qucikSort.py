# 快速排序
# 缺点：浪费空间
# 原理：以列表中的任意一个数为基数，一般选择列表中的第一个数，将列表氛围左右前后两个列表：左列表的数要比
# 基准数小，右边列表的数要比基准数大，然后继续把左边子列表和右边子列表按同样的方法继续分解，比较，一直到分无可分为止

from char01_sort.randomList import random_list


i_list = random_list(20)
print(i_list)


def quick_sort(i_list):
    if len(i_list) <= 1:
        return i_list
    left_list = []
    right_list = []
    for i in i_list[1:]:
        if i <= i_list[0]:
            left_list.append(i)
        else:
            right_list.append(i)
    return quick_sort(left_list) + [i_list[0]] + quick_sort(right_list)


if __name__ == "__main__":
    m_list = quick_sort(i_list)
    print(m_list)
