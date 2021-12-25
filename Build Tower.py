def tower_builder(n_floors):
    finalfloors = 1+(n_floors-1)*(2)
    n1 = 0
    n2 = 0
    list1 = []
    for i in range(n_floors):
        list1.append([])
        for j in range(n1):
            list1[i].append(" ")
        list1[i].append((finalfloors-n2) * "*")
        for j in range(n1):
            list1[i].append(" ")
        n1+=1
        n2+=2
    list1 = list1[::-1]
    
    finallist = []
    for i in list1:
        finallist.append(''.join(i))
        
        
    return finallist
print(tower_builder(3))
