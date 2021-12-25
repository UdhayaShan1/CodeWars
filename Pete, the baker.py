import math
def cakes(recipe, available):
    list_ingre = []
    list_values_each = []
    for i,j in recipe.items():
        list_ingre.append(i)
        list_values_each.append(j)
    min1 = 1000000000
    for i in list_ingre:
        if i not in available.keys():
            return 0
        else:
            check = math.floor(available[i] / recipe[i])
            if check < min1:
                min1 = check
    return min1
