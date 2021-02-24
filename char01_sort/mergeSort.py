# 归并排序

from char01_sort.randomList import random_list
i_list = random_list(20)
print(i_list)


def merge_sort(i_list):
    if len(i_list) <= 1:
        return i_list
    midle = len(i_list)//2

    left_list = i_list[0: midle]
    right_list = i_list[midle:]

    return merge_list(merge_sort(left_list), merge_sort(right_list))


def merge_list(left, right):
    m_list = []

    while left and right:
        if left[0] > right[0]:
            m_list.append(right.pop(0))
        else:
            m_list.append(left.pop(0))

    while left:
        m_list.append(left.pop(0))

    while right:
        m_list.append(right.pop(0))

    return m_list


if __name__ == "__main__":
    m_list = merge_sort(i_list)
    print(m_list)




