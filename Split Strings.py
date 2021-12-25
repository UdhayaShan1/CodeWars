def solution(s):
    list1 = list(s)
    if len(list1) % 2 != 0:
        list1.append("_")
    list2 = []
    b1 = False
    k1 =0
    while b1==False:
        if len(list1) == 0:
            return([])
            break
        if len(list1) == 1:
            return(list1)
            break
        list2.append(list1[k1]+list1[k1+1])
        k1+=2
        if k1==len(list1):
            break
    
    return list2
    
print(solution('X')) 
