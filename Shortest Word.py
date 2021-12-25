def find_short(s):
    list1 = s.split()
    min1 = len(list1[0])
    for i in list1:
        if len(i) < min1:
            min1 = len(i)
    
    return min1 # l: shortest word length
    
print(find_short("turns out random test cases are easier than writing out basic ones"))
