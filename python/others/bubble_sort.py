def bubble_sort(lists):
    len_list=len(lists)
    for i in range(len_list):
        for j in range(len_list-i-1):
            if lists[j]>lists[j+1]:
                lists[j],lists[j+1]=lists[j+1],lists[j]
    print(lists)
    return lists
list=[1,4,2,3,5]
bubble_sort(list)