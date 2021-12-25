def find_next_square(sq):
    if sq**0.5 - int(sq**0.5) != 0:
        return(-1)
    sq1 = sq
    b1 = False
    while b1==False:
        sq1+=1
        if sq1**0.5 - int(sq1**0.5) == 0:
            break
    return(sq1)

print(find_next_square(12))
