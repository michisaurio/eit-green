allowed = []

initList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


notAllowed = [0, [4, 5, 6, 8, 9, 10, 13], [4, 6, 9, 12, 13, 14], [4, 16], [1, 2, 3, 7, 10, 13],
              [8, 9, 10, 12, 13, 14, 1], [8, 10, 13, 16, 1, 2], [8, 4], [5, 6, 7, 11, 14, 1],
              [12, 13, 14, 16, 1, 2, 5], [12, 14, 1, 4, 5, 6], [12, 8], [9, 10, 11, 15, 6, 5],
              [16, 1, 2, 4, 5, 6, 9], [16, 2, 5, 8, 9, 10], [16, 12], [13, 14, 15, 3, 6, 9]]

softAllowed = [0, [4, 5, 6, 8, 9, 10, 11, 13, 14], [4, 5, 6, 9, 12, 13, 14, 15], [4, 6, 9, 16], [1, 2, 3, 7, 10, 13],
               [2, 8, 9, 10, 12, 13, 14, 15, 1], [3, 8, 9, 10, 13, 16, 1, 2], [8, 4, 10, 13], [5, 6, 7, 11, 14, 1],
               [3, 6, 12, 13, 14, 16, 1, 2, 5], [12, 14, 1, 4, 5, 6, 7, 13], [1, 12, 8, 14], [9, 10, 11, 15, 6, 5],
               [16, 1, 2, 4, 5, 6, 9, 7, 10], [16, 2, 5, 8, 9, 10, 1, 11], [2, 5, 16, 12], [13, 14, 15, 3, 6, 9]]


def merge(mergeList, allowedList):
    for i in range(len(mergeList)):
        for j in range(len(mergeList[i])):
            allowedList[mergeList[i][0]] = list(set().union(allowedList[mergeList[i][0]], allowedList[mergeList[i][j]]))
            for k in range(1, len(allowedList)):
                if mergeList[i][j] in allowedList[k]:
                    allowedList[k] = list(set().union(allowedList[k], mergeList[i]))
        for j in range(1, len(mergeList[i])):
            allowedList[mergeList[i][j]] = allowedList[mergeList[i][0]]


def loop(curList, unused, num, allowedList):
    if num != 0:
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


def sublist(element, array):
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


def main(mergeList=[], allowedList=notAllowed, deleteList=[]):
    merge(mergeList, allowedList)
    for i in deleteList:
        allowedList.remove(i)
    loop([], initList, 0, allowedList)
    noSublistList = []
    for i in allowed:
        if not sublist(i, allowed):
            noSublistList.append(i)
    #print(noSublistList)
    #print(len(noSublistList))
    return noSublistList


if __name__ == "__main__":
    main(allowedList=softAllowed)
