def pig_it(text):
    list1 = text.split()
    list2 = []
    
    for i in list1:
        if i.isalpha() == True:
            temp_str = i[1:]
            temp_first = i[0]
            temp_str += temp_first
            temp_str += "ay"
            list2.append(temp_str)
        else:
            list2.append(i)
        
    return(' '.join(list2))
    
print(pig_it('Pig latin is cool ?'))
