def sum_of_intervals(intervals):
    list1 = []
    for i in intervals:
        list2 = list(i)
        list3 = []
        for j in range(list2[0],list2[1]):
            list3.append(j)
        list1 = list1 + list3
    return(len(sorted(set(list1))))
    
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))
