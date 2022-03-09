def swapPositions(list, pos1, pos2):
    first_ele = list.pop(pos1)
    second_ele = list.pop(pos2 - 1)
    list.insert(pos1, second_ele)
    list.insert(pos2, first_ele)
    return list
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print("\nbefore swapping:")
print(List)
print("\nafter swapping")
print(swapPositions(List, pos1 - 1, pos2 - 1))
