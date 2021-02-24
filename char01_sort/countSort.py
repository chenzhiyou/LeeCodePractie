# 计数排序

from char01_sort.randomList import random_list


i_list = random_list(20)
print(i_list)


def count_sort(i_list):
    if len(i_list) <= 1:
        return i_list
    list_len = len(i_list)
    right_list = [None] * list_len
    for i in range(list_len):
        small = 0
        same = 0
        for j in range(list_len):
            if i_list[j] < i_list[i]:
                small = small + 1
            elif i_list[j] == i_list[i]:
                same = same + 1

        for k in range(small, same+small):
            right_list[k] = i_list[k]

    return right_list


if __name__ == "__main__":
    m_list = count_sort(i_list)
    print(m_list)
