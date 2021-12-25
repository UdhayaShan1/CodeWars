def score(dice):
    dice.sort()
    count = 0
    to_remove = []
    for i in range(len(dice)-2):
        if dice[i] == dice[i+1] and dice[i] == dice[i+2]:
            to_remove.append(dice[i])
            
    for i in to_remove:
        occur = len([k for k, x in enumerate(dice) if x == i])
        if occur >= 3:
            if i == 1:
                count+=1000
            else:
                count+= i*100
            for j in range(3):
                dice.remove(i)
        else:
            continue
            
    for i in dice:
        if i == 1:
            count+=100
        elif i == 5:
            count += 50
    return count
    
print(score([3, 3, 3, 2,2,2]))
