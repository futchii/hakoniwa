import random

island = [
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0]
    ]

asase = 0 #目標値5
yama = 0 #目標値1
heichi_position = list()
mura_position = list()

for i1 in range(3,9):
    for i2 in range(3,9):
        if yama == 0 and asase < 5:
            island[i1][i2] = random.randint(1,4)
            if island[i1][i2] == 1:
                asase = asase + 1
            if island[i1][i2] == 4:
                yama = yama + 1
            if island[i1][i2] == 2:
                heichi_position.append([i1,i2])
        elif yama == 0:
            island[i1][i2] = random.randint(2,4)
            if island[i1][i2] == 4:
                yama = yama + 1
            if island[i1][i2] == 2:
                heichi_position.append([i1,i2])
        elif asase < 5:
            island[i1][i2] = random.randint(1,3)
            if island[i1][i2] == 1:
                asase = asase + 1
            if island[i1][i2] == 2:
                heichi_position.append([i1,i2])
        else:
            island[i1][i2] = random.randint(2,3)
            if island[i1][i2] == 2:
                heichi_position.append([i1,i2])

for i in range(0,3):
    mura_position = random.choice(heichi_position)
    island[mura_position[0]][mura_position[1]] = random.randint(101,120)

for a in island:
    print(*a)

#print(island)
print(heichi_position)

map = [
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0]
    ]

for i1 in range(0,12):
    for i2 in range(0,12):
        if island[i1][i2] == 0:
            map[i1][i2] = "海"
        elif island[i1][i2] == 1:
            map[i1][i2] = "浅"
        elif island[i1][i2] == 2:
            map[i1][i2] = "平"
        elif island[i1][i2] == 3:
            map[i1][i2] = "荒"
        elif island[i1][i2] == 4:
            map[i1][i2] = "山"

for a in map:
    print(*a)

def calculation_population(map):
    people = 0
    for i1 in range(0,12):
        for i2 in range(0,12):
            if map[i1][i2] > 100:
                people = people + map[i1][i2] - 100
    
    return people

population = calculation_population(island)
print(population)