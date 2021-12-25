def accum(s):
    list1 = []
    str1 = ''
    count = 0
    for i in s:
        count += 1
        str1 = str1 + i.upper()
        str1 = str1 + (count-1)*(i.lower())
        str1 = str1 + "-"
    str1 = list(str1)
    str1.pop(-1)
    return(''.join(str1))

print(accum("RqaEzty"))
