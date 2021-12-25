alphabet = "abcdefghijklmnopqrstuvwxyz"
def alphabet_position(text):
    list1 = []
    for i in text:
        index = [j for j, x in enumerate(alphabet) if x ==i.lower()]
        if len(index) == 0:
            continue
        list1.append(str(index[0]+1))
    return(' '.join(list1))
        
print(alphabet_position("The sunset sets at twelve o' clock."))
