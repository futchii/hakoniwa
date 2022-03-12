import random

island = [
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [2,0,0,0,0,0,0,0,0,0,0,0],
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
    

def create_island(island):
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

    return island

def start_processing(island):
    people = 0
    farm = 0
    factory =0
    mine= 0
    worker = 0
    farm_worker = 0
    factory_worker =0
    mine_worker = 0

    
    sea_position = list()
    mountain_position = list()
    defense_position = list()
    haribote_position = list()
    base_position = list() 
    farm_position = list()
    factory_position = list()
    mine_position = list()
    town_position = list()
    
    for i1 in range(0,12):
        for i2 in range(0,12):
            if island[i1][i2] == 0 or island[i1][i2] == 1:
                sea_position.append([i1,i2])
            elif island[i1][i2] == 4:
                mountain_position.append([i1,i2])
            elif island[i1][i2] == 10:
                defense_position.append([i1,i2])
            elif island[i1][i2] == 11:
                haribote_position.append([i1,i2])
            elif island[i1][i2] >= 20 and island[i1][i2] < 30:
                base_position.append([i1,i2])
            elif island[i1][i2] >= 40 and island[i1][i2] < 50:
                farm_position.append([i1,i2])
                if island[i1][i2] == 40:
                    farm = farm + 200
                elif island[i1][i2] == 41:
                    farm = farm + 400
                elif island[i1][i2] == 42:
                    farm = farm + 600
                elif island[i1][i2] == 43:
                    farm = farm + 800
                elif island[i1][i2] == 44:
                    farm = farm + 1000
                else:
                    farm = farm                     
            elif island[i1][i2] >= 50 and island[i1][i2] < 60:
                factory_position.append([i1,i2])
                if island[i1][i2] == 50:
                    factory = factory + 200
                elif island[i1][i2] == 51:
                    factory = factory + 400
                elif island[i1][i2] == 52:
                    factory = factory + 600
                elif island[i1][i2] == 53:
                    factory = factory + 800
                elif island[i1][i2] == 54:
                    factory = factory + 1000
                else:
                    factory = factory  
            elif island[i1][i2] >= 60 and island[i1][i2] < 70:
                mine_position.append([i1,i2])
                if island[i1][i2] == 60:
                    mine = mine + 200
                elif island[i1][i2] == 61:
                    mine = mine + 400
                elif island[i1][i2] == 62:
                    mine = mine + 600
                elif island[i1][i2] == 63:
                    mine = mine + 800
                elif island[i1][i2] == 64:
                    mine = mine + 1000
                else:
                    mine = mine
            elif island[i1][i2] > 100:
                if island[i1][i2] > 150:
                    town_position.append([i1,i2])
                people = people + island[i1][i2] - 100

    print(farm,factory,mine)
    worker = people

    if worker - farm >= 0:
        farm_worker = farm
        worker = worker - farm
    else:
        farm_worker = worker
        return people,farm_worker,factory_worker,mine_worker

    if worker - factory >= 0:
        factory_worker = factory
        worker = worker - factory
    else:
        factory_worker = worker
        return people,farm_worker,factory_worker,mine_worker
                
    if worker - mine >= 0:
        mine_worker = mine
        worker = worker - mine
    else:
        mine_worker = worker
        return people,farm_worker,factory_worker,mine_worker

    return (
        people,
        farm_worker,
        factory_worker,
        mine_worker,sea_position,
        mountain_position,
        base_position, 
        defense_position,
        haribote_position,
        farm_position,
        factory_position,
        mine_position,
        town_position)

def end_processing(island):
    people = 0
    farm = 0
    factory =0
    mine= 0
    worker = 0
    farm_worker = 0
    factory_worker =0
    mine_worker = 0
    
    for i1 in range(0,12):
        for i2 in range(0,12):
            if island[i1][i2] >= 40 and island[i1][i2] < 50:
                if island[i1][i2] == 40:
                    farm = farm + 200
                elif island[i1][i2] == 41:
                    farm = farm + 400
                elif island[i1][i2] == 42:
                    farm = farm + 600
                elif island[i1][i2] == 43:
                    farm = farm + 800
                elif island[i1][i2] == 44:
                    farm = farm + 1000
                else:
                    farm = farm                     
            elif island[i1][i2] >= 50 and island[i1][i2] < 60:
                if island[i1][i2] == 50:
                    factory = factory + 200
                elif island[i1][i2] == 51:
                    factory = factory + 400
                elif island[i1][i2] == 52:
                    factory = factory + 600
                elif island[i1][i2] == 53:
                    factory = factory + 800
                elif island[i1][i2] == 54:
                    factory = factory + 1000
                else:
                    factory = factory  
            elif island[i1][i2] >= 60 and island[i1][i2] < 70:
                if island[i1][i2] == 60:
                    mine = mine + 200
                elif island[i1][i2] == 61:
                    mine = mine + 400
                elif island[i1][i2] == 62:
                    mine = mine + 600
                elif island[i1][i2] == 63:
                    mine = mine + 800
                elif island[i1][i2] == 64:
                    mine = mine + 1000
                else:
                    mine = mine
            elif island[i1][i2] > 100:
                people = people + island[i1][i2] - 100

    print(farm,factory,mine)
    worker = people

    if worker - farm >= 0:
        farm_worker = farm
        worker = worker - farm
    else:
        farm_worker = worker
        return people,farm_worker,factory_worker,mine_worker

    if worker - factory >= 0:
        factory_worker = factory
        worker = worker - factory
    else:
        factory_worker = worker
        return people,farm_worker,factory_worker,mine_worker
                
    if worker - mine >= 0:
        mine_worker = mine
        worker = worker - mine
    else:
        mine_worker = worker
        return people,farm_worker,factory_worker,mine_worker

    return people,farm_worker,factory_worker,mine_worker

def growth_city(island):
    def expanding_city():
        if i1 == 0 and i2 == 0:
            if island[i1+1][i2] == 2:
                island_imaginally[i1+1][i2] = random.randint(101,120)
            if island[i1][i2+1] == 2:
                island_imaginally[i1][i2+1] = random.randint(101,120)
        elif i1 == 0 and i2 == 11:
            if island[i1+1][i2] == 2:
                island_imaginally[i1+1][i2] = random.randint(101,120)
            if island[i1][i2-1] == 2:
                island_imaginally[i1][i2-1] = random.randint(101,120)
        elif i1 == 11 and i2 == 0:
            if island[i1-1][i2] == 2:
                island_imaginally[i1-1][i2] = random.randint(101,120)
            if island[i1][i2+1] == 2:
                island_imaginally[i1][i2+1] = random.randint(101,120)
        elif i1 == 11 and i2 == 11:
            if island[i1-1][i2] == 2:
                island_imaginally[i1-1][i2] = random.randint(101,120)
            if island[i1][i2-1] == 2:
                island_imaginally[i1][i2-1] = random.randint(101,120)
        elif i1 == 0:
            if island[i1+1][i2] == 2:
                island_imaginally[i1+1][i2] = random.randint(101,120)
            if island[i1][i2+1] == 2:
                island_imaginally[i1][i2+1] = random.randint(101,120)
            if island[i1][i2-1] == 2:
                island_imaginally[i1][i2-1] = random.randint(101,120)
        elif i1 == 11:
            if island[i1-1][i2] == 2:
                island_imaginally[i1-1][i2] = random.randint(101,120)
            if island[i1][i2+1] == 2:
                island_imaginally[i1][i2+1] = random.randint(101,120)
            if island[i1][i2-1] == 2:
                island_imaginally[i1][i2-1] = random.randint(101,120)
        elif i2 == 0:
            if island[i1+1][i2] == 2:
                island_imaginally[i1+1][i2] = random.randint(101,120)
            if island[i1-1][i2] == 2:
                island_imaginally[i1-1][i2] = random.randint(101,120)
            if island[i1][i2+1] == 2:
                island_imaginally[i1][i2+1] = random.randint(101,120)
        elif i2 == 11:
            if island[i1+1][i2] == 2:
                island_imaginally[i1+1][i2] = random.randint(101,120)
            if island[i1-1][i2] == 2:
                island_imaginally[i1-1][i2] = random.randint(101,120)
            if island[i1][i2-1] == 2:
                island_imaginally[i1][i2-1] = random.randint(101,120)
        else:
            if island[i1+1][i2] == 2:
                island_imaginally[i1+1][i2] = random.randint(101,120)
            if island[i1-1][i2] == 2:
                island_imaginally[i1-1][i2] = random.randint(101,120)
            if island[i1][i2+1] == 2:
                island_imaginally[i1][i2+1] = random.randint(101,120)
            if island[i1][i2-1] == 2:
                island_imaginally[i1][i2-1] = random.randint(101,120)
    

    island_imaginally = [
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
                coin = random.random()
                if island[i1][i2] > 100 and island[i1][i2] < 200 :
                    island_imaginally[i1][i2] = island[i1][i2] + random.randint(0,20)
                    if island_imaginally[i1][i2] > 200:
                        island_imaginally[i1][i2] = 200
                    if coin < 0.2:
                        expanding_city()
                elif island[i1][i2] >= 40 and island[i1][i2] < 50:
                    island_imaginally[i1][i2] = island[i1][i2]
                    if coin < 0.2:
                        expanding_city()
                else:
                    if island_imaginally[i1][i2] < 100 or island_imaginally[i1][i2] > 200:
                        island_imaginally[i1][i2] = island[i1][i2]

    return island_imaginally

def disaster(
        island,
        sea_position,
        mountain_position,
        base_position, 
        defense_position,
        haribote_position,
        farm_position,
        factory_position,
        mine_position,
        town_position):
    
    def condition_check(island,target,condition_min,condition_max):
        if target[0] == 0 and target[1] == 0:
            if island[target[0]+1][target[1]] >= condition_min and island[target[0]+1][target[1]] <= condition_max:
                return True
            elif island[target[0]][target[1]+1] >= condition_min and island[target[0]][target[1]+1] <= condition_max:
                return True
            return False
        elif target[0] == 0 and target[1] == 11:
            if island[target[0]+1][target[1]] >= condition_min and island[target[0]+1][target[1]] <= condition_max:
                return True
            elif island[target[0]][target[1]-1] >= condition_min and island[target[0]][target[1]-1] <= condition_max:
                return True
            return False
        elif target[0] == 11 and target[1] == 0:
            if island[target[0]-1][target[1]] >= condition_min and island[target[0]-1][target[1]] <= condition_max:
                return True
            elif island[target[0]][target[1]+1] >= condition_min and island[target[0]][target[1]+1] <= condition_max:
                return True
            return False
        elif target[0] == 11 and target[1] == 11:
            if island[target[0]-1][target[1]] >= condition_min and island[target[0]-1][target[1]] <= condition_max:
                return True
            elif island[target[0]][target[1]-1] >= condition_min and island[target[0]][target[1]-1] <= condition_max:
                return True
            return False
        elif target[0] == 0:
            if island[target[0]+1][target[1]] >= condition_min and island[target[0]+1][target[1]] <= condition_max:
                return True
            elif island[target[0]][target[1]+1] >= condition_min and island[target[0]][target[1]+1] <= condition_max:
                return True
            elif island[target[0]][target[1]-1] >= condition_min and island[target[0]][target[1]-1] <= condition_max:
                return True
            return False
        elif target[0] == 11:
            if island[target[0]-1][target[1]] >= condition_min and island[target[0]-1][target[1]] <= condition_max:
                return True
            elif island[target[0]][target[1]+1] >= condition_min and island[target[0]][target[1]+1] <= condition_max:
                return True
            elif island[target[0]][target[1]-1] >= condition_min and island[target[0]][target[1]-1] <= condition_max:
                return True
            return False
        elif target[1] == 0:
            if island[target[0]+1][target[1]] >= condition_min and island[target[0]+1][target[1]] <= condition_max:
                return True
            elif island[target[0]-1][target[1]] >= condition_min and island[target[0]-1][target[1]] <= condition_max:
                return True
            elif island[target[0]][target[1]+1] >= condition_min and island[target[0]][target[1]+1] <= condition_max:
                return True
            return False
        elif target[1] == 11:
            if island[target[0]+1][target[1]] >= condition_min and island[target[0]+1][target[1]] <= condition_max:
                return True
            elif island[target[0]-1][target[1]] >= condition_min and island[target[0]-1][target[1]] <= condition_max:
                return True
            elif island[target[0]][target[1]-1] >= condition_min and island[target[0]][target[1]-1] <= condition_max:
                return True
            return False
        else:
            if island[target[0]+1][target[1]] >= condition_min and island[target[0]+1][target[1]] <= condition_max:
                return True
            elif island[target[0]-1][target[1]] >= condition_min and island[target[0]-1][target[1]] <= condition_max:
                return True
            elif island[target[0]][target[1]+1] >= condition_min and island[target[0]][target[1]+1] <= condition_max:
                return True
            elif island[target[0]][target[1]-1] >= condition_min and island[target[0]][target[1]-1] <= condition_max:
                return True
            return False


    fire_log = list()
    typhoon_log = list()

    while True:
        coin = random.random()
        if coin < 0.01:#火災
            candidate_disaster = haribote_position + factory_position + town_position
            disaster = random.choice(candidate_disaster)
            if (island[disaster[0]][disaster[1]] == 11 or 
            (island[disaster[0]][disaster[1]] >= 50 and island[disaster[0]][disaster[1]] < 60) or 
            island[disaster[0]][disaster[1]] > 150):
                if condition_check(island,disaster,70,79) == False:
                    if condition_check(island,disaster,13,15) == False:
                        fire_log = fire_log + disaster
                        island[disaster[0]][disaster[1]] = 3
            continue
        if coin > 0.01 and coin < 0.03:#台風
            candidate_disaster = haribote_position + farm_position
            disaster = random.choice(candidate_disaster)
            if (island[disaster[0]][disaster[1]] == 11 or 
            (island[disaster[0]][disaster[1]] >= 40 and island[disaster[0]][disaster[1]] < 50)):
                if condition_check(island,disaster,70,79) == False:
                    if condition_check(island,disaster,13,15) == False:
                        typhoon_log = typhoon_log + disaster
                        island[disaster[0]][disaster[1]] = 2
            continue
        if coin > 0.03 and coin < 0.45:#津波
            candidate_disaster = sea_position
            disaster = random.choice(candidate_disaster)


        break
        
    return island,
        
                

island = create_island(island)

for a in island:
    print(*a)

print("---")

island = growth_city(island)

for a in island:
    print(*a)

print("---")

island = growth_city(island)

for a in island:
    print(*a)

print("---")

island = growth_city(island)

for a in island:
    print(*a)

print(start_processing(island))