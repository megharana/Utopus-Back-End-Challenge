N = int(input())
# energy = []
energy = [int(x) for x in input().split(' ')]
# print(N, energy)
totalEnergy = sum(energy)
extraEnergy = []
for x in energy:
    extraEnergy.append(totalEnergy - x)
print(min(extraEnergy))
