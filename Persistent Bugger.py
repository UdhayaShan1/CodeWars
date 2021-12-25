def persistence(n):
    count = 0
    b1 = False
    while b1==False:
        if len(str(n)) == 1:
            return count
            break
        result = 1
        for i in str(n):
            result = result * int(i)
        n = result
        count += 1
    
print(persistence(4))
