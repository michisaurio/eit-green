allowed = []

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


not_allowed = [0, [4, 5, 6, 8, 9, 10, 13], [4, 6, 9, 12, 13, 14], [4, 16], [1, 2, 3, 7, 10, 13],
               [8, 9, 10, 12, 13, 14, 1], [8, 10, 13, 16, 1, 2], [8, 4], [5, 6, 7, 11, 14, 1],
               [12, 13, 14, 16, 1, 2, 5], [12, 14, 1, 4, 5, 6], [12, 8], [9, 10, 11, 15, 6, 5],
               [16, 1, 2, 4, 5, 6, 9], [16, 2, 5, 8, 9, 10], [16, 12], [13, 14, 15, 3, 6, 9]]

soft_allowed = [0, [4, 5, 6, 8, 9, 10, 13], [4, 6, 9, 12, 13, 14], [4, 16], [1, 2, 3, 7, 10, 13],
               [8, 9, 10, 12, 13, 14, 1], [8, 10, 13, 16, 1, 2], [8, 4], [5, 6, 7, 11, 14, 1],
               [12, 13, 14, 16, 1, 2, 5], [12, 14, 1, 4, 5, 6], [12, 8], [9, 10, 11, 15, 6, 5],
               [16, 1, 2, 4, 5, 6, 9], [16, 2, 5, 8, 9, 10], [16, 12], [13, 14, 15, 3, 6, 9]]

def loop(cur_list, unused, num):
    if num != 0:
        cur_list.append(num)
        for i in range(len(not_allowed[num])):
                if not_allowed[num][i] in unused: unused.remove(not_allowed[num][i])
    while len(unused)>0:
        a = unused[0]
        unused.remove(a)
        unused2 = unused.copy()
        cur_list2 = cur_list.copy()
        loop(cur_list2, unused2, a)
    if num != 0:
        allowed.append(cur_list)

loop([], list, 0)

#print(allowed)
#print(len(allowed))

def sublist(element, array):
    for i in array:
        if len(element)>= len(i):
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

#print(allowed)

no_sublists_list = []
for i in allowed:
    if not sublist(i, allowed):
        no_sublists_list.append(i)
print(no_sublists_list)
print(len(no_sublists_list))

print(allowed)