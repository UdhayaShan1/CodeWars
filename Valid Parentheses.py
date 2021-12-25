def valid_parentheses(string):
    if string == '':
        return True
    indices_open = [i for i , x in enumerate(string) if x=="("]
    indices_close = [i for i , x in enumerate(string) if x==")"]
    if len(indices_close) != len(indices_open):
        return False
    list1 = list(string)
    list2 = []
    for i in list1:
        if i.isalpha() == True:
            continue
        else:
            list2.append(str(i))
    b1 = False
    k1 = 0
    count = 0
    
    while b1==False:
        
        if len(list2) == 0:
            if count == len(indices_open):
                return True
            else:
                return False
        if list2[k1] != "(":
            return False
        c1 = False
        k2 = 1
        while c1==False:
            if list2[k2] == ")":
                count += 1
                list2.remove("(")
                list2.remove(")")
                
                break
            k2+=1
    return True
