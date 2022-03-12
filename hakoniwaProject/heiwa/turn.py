import random

def start_process(island):
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

    worker = people

    if worker - farm >= 0:
        farm_worker = farm
        worker = worker - farm
    else:
        farm_worker = worker
        return (
            people,
            farm_worker,
            factory_worker,
            mine_worker,
            sea_position,
            mountain_position,
            base_position, 
            defense_position,
            haribote_position,
            farm_position,
            factory_position,
            mine_position,
            town_position)

    if worker - factory >= 0:
        factory_worker = factory
        worker = worker - factory
    else:
        factory_worker = worker
        return (
            people,
            farm_worker,
            factory_worker,
            mine_worker,
            sea_position,
            mountain_position,
            base_position, 
            defense_position,
            haribote_position,
            farm_position,
            factory_position,
            mine_position,
            town_position)
                
    if worker - mine >= 0:
        mine_worker = mine
        worker = worker - mine
    else:
        mine_worker = worker
        return (
            people,
            farm_worker,
            factory_worker,
            mine_worker,
            sea_position,
            mountain_position,
            base_position, 
            defense_position,
            haribote_position,
            farm_position,
            factory_position,
            mine_position,
            town_position)

    return (
        people,
        farm_worker,
        factory_worker,
        mine_worker,
        sea_position,
        mountain_position,
        base_position, 
        defense_position,
        haribote_position,
        farm_position,
        factory_position,
        mine_position,
        town_position)

def harvest_processing(farm_worker):
    return farm_worker

def income_processing(factory_worker,mine_worker):
    return (factory_worker + mine_worker) * 0.1

def food_processing(food,people):
    if food - people * 0.2 > 0:
        return food - people * 0.2
    else:
        return 0

def development_processing(island,money,action,position):
    if action == 0:#整地
        if (
            money - 5 >= 0 and
            island[position[0]][position[1]] != 0 and
            island[position[0]][position[1]] != 1 and
            island[position[0]][position[1]] != 12 and
            (island[position[0]][position[1]] < 30 or island[position[0]][position[1]] > 39 ) and
            (island[position[0]][position[1]] < 80 or island[position[0]][position[1]] > 89 )
        ):
            island[position[0]][position[1]] = 2
            money = money - 5 

    elif action == 1:#埋め立て
        pass

    elif action == 2:#掘削
        pass

    elif action == 3:#伐採
        if island[position[0]][position[1]] >= 70 and island[position[0]][position[1]] < 80:
            island[position[0]][position[1]] = 2
            if island[position[0]][position[1]] == 70:
                money = money + 200
            elif island[position[0]][position[1]] == 71:
                money = money + 400
            elif island[position[0]][position[1]] == 72:
                money = money + 600
            elif island[position[0]][position[1]] == 73:
                money = money + 800
            elif island[position[0]][position[1]] == 74:
                money = money + 1000
            else:
                money = money

    elif action == 4:#植林
        if money - 50 >= 0:
            money = money - 50
            if island[position[0]][position[1]] >= 70 and island[position[0]][position[1]] < 74:
                island[position[0]][position[1]] = island[position[0]][position[1]] + 1
            elif (
                island[position[0]][position[1]] != 0 and
                island[position[0]][position[1]] != 1 and
                island[position[0]][position[1]] != 12 and
                (island[position[0]][position[1]] < 30 or island[position[0]][position[1]] > 39 ) and
                (island[position[0]][position[1]] < 60 or island[position[0]][position[1]] > 79 ) and
                (island[position[0]][position[1]] < 80 or island[position[0]][position[1]] > 89 )
            ):
                island[position[0]][position[1]] = 70

    elif action == 5:#農場整備
        if  money - 20 >= 0:
            money = money - 20
            if island[position[0]][position[1]] >= 40 and island[position[0]][position[1]] < 44:
                island[position[0]][position[1]] = island[position[0]][position[1]] + 1
            elif (
                island[position[0]][position[1]] != 0 and
                island[position[0]][position[1]] != 1 and
                island[position[0]][position[1]] != 12 and
                (island[position[0]][position[1]] < 30 or island[position[0]][position[1]] > 39 ) and
                (island[position[0]][position[1]] < 60 or island[position[0]][position[1]] > 79 ) and
                (island[position[0]][position[1]] < 80 or island[position[0]][position[1]] > 89 )
            ):
                island[position[0]][position[1]] = 40
                
    elif action == 6:#工場建設
        if money - 100 >= 0:
            money = money - 100
            if island[position[0]][position[1]] >= 50 and island[position[0]][position[1]] < 54:
                island[position[0]][position[1]] = island[position[0]][position[1]] + 1
            elif (
                island[position[0]][position[1]] != 0 and
                island[position[0]][position[1]] != 1 and
                island[position[0]][position[1]] != 12 and
                (island[position[0]][position[1]] < 30 or island[position[0]][position[1]] > 39 ) and
                (island[position[0]][position[1]] < 60 or island[position[0]][position[1]] > 79 ) and
                (island[position[0]][position[1]] < 80 or island[position[0]][position[1]] > 89 )
            ):
                island[position[0]][position[1]] = 50
                
    elif action == 7:#採掘所整備
        if money - 300 >= 0:
            money = money - 300
            if island[position[0]][position[1]] == 4:
                island[position[0]][position[1]] = 60
            elif island[position[0]][position[1]] >= 60 and island[position[0]][position[1]] < 64:
                island[position[0]][position[1]] = island[position[0]][position[1]] + 1
                
    elif action == 8:#ミサイル基地建設
        if money - 300 >= 0:
            money = money - 300
            if island[position[0]][position[1]] >= 20 and island[position[0]][position[1]] < 24:
                island[position[0]][position[1]] = island[position[0]][position[1]] + 1
            elif (
                island[position[0]][position[1]] != 0 and
                island[position[0]][position[1]] != 1 and
                island[position[0]][position[1]] != 12 and
                (island[position[0]][position[1]] < 30 or island[position[0]][position[1]] > 39 ) and
                (island[position[0]][position[1]] < 60 or island[position[0]][position[1]] > 79 ) and
                (island[position[0]][position[1]] < 80 or island[position[0]][position[1]] > 89 )
            ):
                island[position[0]][position[1]] = 20

    elif action == 9:#海底基地建設
        if money - 6000 >= 0:
            money = money - 6000
            if island[position[0]][position[1]] == 0:
                island[position[0]][position[1]] = 30
            elif island[position[0]][position[1]] >= 30 and island[position[0]][position[1]] < 32:
                island[position[0]][position[1]] = island[position[0]][position[1]] + 1
    
    elif action == 10:#防衛施設建設
        if money - 500 >= 0:
            money = money - 500
            if (
                island[position[0]][position[1]] != 0 and
                island[position[0]][position[1]] != 1 and
                island[position[0]][position[1]] != 12 and
                (island[position[0]][position[1]] < 30 or island[position[0]][position[1]] > 39 ) and
                (island[position[0]][position[1]] < 60 or island[position[0]][position[1]] > 79 ) and
                (island[position[0]][position[1]] < 80 or island[position[0]][position[1]] > 89 )
            ):
                island[position[0]][position[1]] = 10
    
    elif action == 11:#ハリボテ設置
        if money - 1 >= 0:
            money = money - 1
            if (
                island[position[0]][position[1]] != 0 and
                island[position[0]][position[1]] != 1 and
                island[position[0]][position[1]] != 12 and
                (island[position[0]][position[1]] < 30 or island[position[0]][position[1]] > 39 ) and
                (island[position[0]][position[1]] < 60 or island[position[0]][position[1]] > 79 ) and
                (island[position[0]][position[1]] < 80 or island[position[0]][position[1]] > 89 )
            ):
                island[position[0]][position[1]] = 11

    elif action == 12:#記念碑建造
        if money - 9999 >= 0:
            money = money - 9999
            if (
                island[position[0]][position[1]] != 0 and
                island[position[0]][position[1]] != 1 and
                island[position[0]][position[1]] != 12 and
                (island[position[0]][position[1]] < 30 or island[position[0]][position[1]] > 39 ) and
                (island[position[0]][position[1]] < 60 or island[position[0]][position[1]] > 79 ) and
                (island[position[0]][position[1]] < 80 or island[position[0]][position[1]] > 89 )
            ):
                island[position[0]][position[1]] = 13

    elif action == 13:#記念碑建造
        if money - 9999 >= 0:
            money = money - 9999
            if (
                island[position[0]][position[1]] != 0 and
                island[position[0]][position[1]] != 1 and
                island[position[0]][position[1]] != 12 and
                (island[position[0]][position[1]] < 30 or island[position[0]][position[1]] > 39 ) and
                (island[position[0]][position[1]] < 60 or island[position[0]][position[1]] > 79 ) and
                (island[position[0]][position[1]] < 80 or island[position[0]][position[1]] > 89 )
            ):
                island[position[0]][position[1]] = 14

    elif action == 14:#記念碑建造
        if money - 9999 >= 0:
            money = money - 9999
            if (
                island[position[0]][position[1]] != 0 and
                island[position[0]][position[1]] != 1 and
                island[position[0]][position[1]] != 12 and
                (island[position[0]][position[1]] < 30 or island[position[0]][position[1]] > 39 ) and
                (island[position[0]][position[1]] < 60 or island[position[0]][position[1]] > 79 ) and
                (island[position[0]][position[1]] < 80 or island[position[0]][position[1]] > 89 )
            ):
                island[position[0]][position[1]] = 15
                

    return island,money

def cashing_processing(money):
    return money + 10

"""
def attract_processing():
    pass
"""

def export(money,food,amount):
    if food - amount < 0:
        amount = amount - (amount - food)
    food = food - amount
    money = money + food
    return money,food

def flattening(island,money,position):
    if (
        money - 100 > 0 and
        island[position[0]][position[1]] != 0 and
        island[position[0]][position[1]] != 1 and
        island[position[0]][position[1]] != 12 and
        (island[position[0]][position[1]] < 30 or island[position[0]][position[1]] > 39 ) and
        (island[position[0]][position[1]] < 80 or island[position[0]][position[1]] > 89 )
    ):
            island[position[0]][position[1]] = 2
            money = money - 100 
    return island,money

def hex_processing(island):

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
                if island[i1][i2] >= 70 and island[i1][i2] < 74:
                    island_imaginally[i1][i2] = island[i1][i2] + 1
                else:
                    island_imaginally[i1][i2] = island[i1][i2]

    return island_imaginally





def disaster_processing():
    pass
def log_processing():
    pass
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