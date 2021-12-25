def longest(a1, a2):
    str1 = list(a1 + a2)
    str1.sort()
    b1 = False
    k1 = 0
    while b1==False:
        if k1==len(str1)-1:
            break
        if str1[k1] == str1[k1+1]:
            str1.pop(k1+1)
            k1 = 0
        else:
            k1+=1
        
    return(''.join(str1))
    
print(longest("a","a"))
