import json
import random

from . import calculation

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .models import Islands

class TestView(APIView):
    def get(self,request):
        user_island = Islands.objects.get(account=request.user)
        message = user_island.name
        return JsonResponse({'message':message})

class IslandReadView(APIView):
    def get(self,request):
        user_island = Islands.objects.get(account=request.user)
        name = user_island.name
        turn = user_island.turn
        island = user_island.island
        money = user_island.money
        food = user_island.food
        people = user_island.people
        farm_worker = user_island.farm_worker
        factory_worker = user_island.factory_worker
        mine_worker = user_island.mine_worker
        return JsonResponse({'name':name,'turn':turn,'island':island,'money':money,'food':food,
        'people':people,'farm_worker':farm_worker,'factory_worker':factory_worker,'mine_worker':mine_worker})


class IslandCreateView(APIView):
    def post(self,request):
        try:
            data = json.loads(request.body)
            name = data['name']
        except:
            return JsonResponse({'message':'Post data injustice.'}, status=400)
        
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

        island = calculation.create_island(island)
        
        try:
            Islands.objects.create(
                account = request.user,
                name = name,
                island = island,
                money = 1000,
                food = 5000,
            )
        except:
            return JsonResponse({'message':'registration failure.'}, status=400)

        return JsonResponse({'message':'island success.'})


class CashingView(APIView):
    def get(self,request):
        user_island = Islands.objects.get(account=request.user)
        name = user_island.name
        turn = user_island.turn
        island = user_island.island
        money = user_island.money
        food = user_island.food
        people = user_island.people
        farm_worker = user_island.farm_worker
        factory_worker = user_island.factory_worker
        mine_worker = user_island.mine_worker

        if(turn<=0):
            return JsonResponse({'name':name,'turn':turn,'island':island,'money':money,'food':food,
            'people':people,'farm_worker':farm_worker,'factory_worker':factory_worker,'mine_worker':mine_worker})
        else:
            turn = turn - 1

        island = eval(island)

        start_tuple = calculation.start_process(island)

        people = start_tuple[0]
        farm_worker = start_tuple[1]
        factory_worker = start_tuple[2]
        mine_worker = start_tuple[3]
        sea_position = start_tuple[4]
        mountain_position = start_tuple[5]
        base_position = start_tuple[6]
        defense_position = start_tuple[7]
        haribote_position = start_tuple[8]
        farm_position = start_tuple[9]
        factory_position = start_tuple[10]
        mine_position = start_tuple[11]
        town_position = start_tuple[12]

        food = calculation.harvest_processing(farm_worker)
        money = calculation.income_processing(factory_worker,mine_worker) + money
        food = calculation.food_processing(food,people)

        money = calculation.cashing_processing(money)

        island = calculation.hex_processing(island)

        end_tuple = calculation.end_processing(island)

        people = end_tuple[0]
        farm_worker = end_tuple[1]
        factory_worker = end_tuple[2]
        mine_worker = end_tuple[3]

        island = str(island)

        try:
            user_island.name = name
            user_island.turn = turn
            user_island.island = island
            user_island.money = money
            user_island.food = food
            user_island.people = people
            user_island.farm_worker = farm_worker
            user_island.factory_worker = factory_worker
            user_island.mine_worker = mine_worker
            user_island.save()
        except:
            return JsonResponse({'message':'registration failure.'}, status=400)
        
        return JsonResponse({'name':name,'turn':turn,'island':island,'money':money,'food':food,
        'people':people,'farm_worker':farm_worker,'factory_worker':factory_worker,'mine_worker':mine_worker})

class DevelopmentView(APIView):
    def post(self,request):
        try:
            data = json.loads(request.body)
            pos1 = data['pos1']
            pos2 = data['pos2']
            dev_cmd = data['dev_cmd']
        except:
            return JsonResponse({'message':'Post data injustice.'}, status=400)

        user_island = Islands.objects.get(account=request.user)
        name = user_island.name
        turn = user_island.turn
        island = user_island.island
        money = user_island.money
        food = user_island.food
        people = user_island.people
        farm_worker = user_island.farm_worker
        factory_worker = user_island.factory_worker
        mine_worker = user_island.mine_worker
        
        if(turn <= 0 or money - 150 <= 0):
            return JsonResponse({'name':name,'turn':turn,'island':island,'money':money,'food':food,
            'people':people,'farm_worker':farm_worker,'factory_worker':factory_worker,'mine_worker':mine_worker})
        else:
            turn = turn - 1

        island = eval(island)

        start_tuple = calculation.start_process(island)

        people = start_tuple[0]
        farm_worker = start_tuple[1]
        factory_worker = start_tuple[2]
        mine_worker = start_tuple[3]
        sea_position = start_tuple[4]
        mountain_position = start_tuple[5]
        base_position = start_tuple[6]
        defense_position = start_tuple[7]
        haribote_position = start_tuple[8]
        farm_position = start_tuple[9]
        factory_position = start_tuple[10]
        mine_position = start_tuple[11]
        town_position = start_tuple[12]

        food = calculation.harvest_processing(farm_worker)
        money = calculation.income_processing(factory_worker,mine_worker) + money
        food = calculation.food_processing(food,people)

        position = [pos1,pos2]

        development_tuple = calculation.development_processing(island,money,position,calculation.dev_action(dev_cmd))

        island = development_tuple[0]
        money = development_tuple[1]

        island = calculation.hex_processing(island)

        end_tuple = calculation.end_processing(island)

        people = end_tuple[0]
        farm_worker = end_tuple[1]
        factory_worker = end_tuple[2]
        mine_worker = end_tuple[3]
        
        island = str(island)

        try:
            user_island.name = name
            user_island.turn = turn
            user_island.island = island
            user_island.money = money
            user_island.food = food
            user_island.people = people
            user_island.farm_worker = farm_worker
            user_island.factory_worker = factory_worker
            user_island.mine_worker = mine_worker
            user_island.save()
        except:
            return JsonResponse({'message':'registration failure.'}, status=400)
        
        return JsonResponse({'name':name,'turn':turn,'island':island,'money':money,'food':food,
        'people':people,'farm_worker':farm_worker,'factory_worker':factory_worker,'mine_worker':mine_worker})