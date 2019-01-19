totalNodes = int(input())
dictNodes = {}

for i in range(0, totalNodes):
    childList = []
    parent, child = [int(x) for x in input().split(' ')]
    childList.append(child)

    if (parent in dictNodes):
        # print(dictNodes[parent])
        updatedChildList = list(dictNodes[parent])
        updatedChildList.append(child)
        print(updatedChildList)
        dictNodes.update({parent: updatedChildList})
    else:
        dictNodes.update({parent: childList})
print(dictNodes)
