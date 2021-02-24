# 快速排序

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
