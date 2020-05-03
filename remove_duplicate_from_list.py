def remove_duplicate(list1):
    list2 = []
    for i in list1:
        if i not in list2 :
            list2.append(i)
    print(list2)
# enter ny list in the place of list1 when calling remove_duplicate


remove_duplicate([1, 2, 3, 4, 4, 5, 6,97, 1, 5, 6])