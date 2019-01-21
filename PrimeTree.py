totalNodes = int(input())
dictNodes = {}

for i in range(0, totalNodes - 1):
    childList = []
    parent, child = [int(x) for x in input().split(' ')]
    childList.append(child)

    if (parent in dictNodes):
        updatedChildList = list(dictNodes[parent])
        updatedChildList.append(child)
        dictNodes.update({parent: updatedChildList})
    else:
        dictNodes.update({parent: childList})


def countPrimeNode():
    count = 0
    for key in dictNodes:
        targetList = list(dictNodes[key])
        result = isPrime(sum(targetList))
        if result:
            count = count + 1
    print(count)


def isPrime(num):
    flag = True
    for i in range(2, num):
        if (num % i) == 0:
            flag = False
    return flag


countPrimeNode()
# print()
