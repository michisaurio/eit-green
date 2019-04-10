allowed = []

initList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


notAllowed = [[3, 4, 5, 7, 8, 9, 12], [3, 5, 8, 11, 12, 13], [3, 15], [0, 1, 2, 6, 9, 12],
              [7, 8, 9, 11, 12, 13, 0], [7, 9, 12, 15, 0, 1], [7, 3], [4, 5, 6, 10, 13, 0],
              [11, 12, 13, 15, 0, 1, 4], [11, 13, 0, 3, 4, 5], [11, 7], [8, 9, 10, 14, 1, 4],
              [15, 0, 1, 3, 4, 5, 8], [15, 1, 4, 7, 8, 9], [15, 11], [12, 13, 14, 2, 5, 8]]

softAllowed = [[3, 4, 5, 7, 8, 9, 10, 12, 13], [3, 4, 5, 8, 11, 12, 13, 14], [3, 5, 8, 15], [0, 1, 2, 6, 9, 12],
               [1, 7, 8, 9, 11, 12, 13, 14, 0], [2, 7, 8, 9, 12, 15, 0, 1], [7, 3, 9, 12], [4, 5, 6, 10, 13, 0],
               [2, 5, 11, 12, 13, 15, 0, 1, 4], [11, 13, 0, 3, 4, 5, 6, 12], [0, 11, 7, 13], [8, 9, 10, 14, 1, 4],
               [15, 0, 1, 3, 4, 5, 8, 6, 9], [15, 1, 4, 7, 8, 9, 0, 10], [1, 4, 15, 11], [12, 13, 14, 2, 5, 8]]


# Modifies the restriction list (allowedList) by merging certain nodes such that for instance the light for moving
# straight forward and taking a turn to the right must be green at the same time (typically because the cars in these
# two directions start in the same lane).
def merge(mergeList, allowedList):
    for i in range(len(mergeList)):
        for j in range(len(mergeList[i])):
            allowedList[mergeList[i][0]] = list(set().union(allowedList[mergeList[i][0]], allowedList[mergeList[i][j]]))
            for k in range(0, len(allowedList)):
                if mergeList[i][j] in allowedList[k]:
                    allowedList[k] = list(set().union(allowedList[k], mergeList[i]))
        for j in range(1, len(mergeList[i])):
            allowedList[mergeList[i][j]] = allowedList[mergeList[i][0]]


# Uses recursion to generate a list of all possible configurations given the restrictions.
# The current possible restrictions are notAllowed and softAllowed, where notAllowed allows every configuration where
# cars don't crash into each other, and softAllowed allows all configurations that don't crash into each other and
# additionally requires that cars can't exit the intersection through the same direction from two different direction.
def loop(curList, unused, num, allowedList):
    if num != -1:
        curList.append(num)
        for i in range(len(allowedList[num])):
                if allowedList[num][i] in unused: unused.remove(allowedList[num][i])
    while len(unused) > 0:
        a = unused[0]
        unused.remove(a)
        unused2 = unused.copy()
        curList2 = curList.copy()
        loop(curList2, unused2, a, allowedList)
    if num != 0:
        allowed.append(curList)


# Removes configurations that are a subset of some other configuration.
def sublist(element, array):
    if element == []:
        return True
    for i in array:
        if len(element) >= len(i):
            continue
        else:
            currentIndex = 0
            for index in range(len(element)):
                currentIndex = index
                if element[index] not in i:
                    currentIndex = 0
                    break
            if currentIndex == len(element)-1:
                return True
    return False


# Primary loop.
def main(mergeList=[], allowedList=notAllowed, deleteList=[], footGanger=False):
    merge(mergeList, allowedList)
    for i in deleteList:
        allowedList.remove(i)
    loop([], initList, -1, allowedList)
    noSublistList = []
    if footGanger == False:
        for i in range(len(allowed)):
            removelist = []
            for j in range(len(allowed[i])):
                if allowed[i][j] % 4 == 3:
                    removelist.append(allowed[i][j])
            for j in removelist:
                allowed[i].remove(j)
    for i in allowed:
        if not sublist(i, allowed):
            noSublistList.append(i)
    print(noSublistList)
    return noSublistList


if __name__ == "__main__":
    liste = main(mergeList=[[0, 1, 2], [4, 5, 6], [8, 9, 10], [12, 13, 14]])
    print(liste)
