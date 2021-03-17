
def order(list1, list2):
    if len(list1)& len(list2) <= 0:
        return list1
    if len(list1) <= 0:
        return list2
    if len(list2) <= 0:
        return list1
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] < list2[j]:
                list2[j+1, (len(list2)+1)] = list2[j, (len(list2))]
                list2[j] = list1[i]
    return list2


list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
list_new = order(list1, list2)
print(list_new)
