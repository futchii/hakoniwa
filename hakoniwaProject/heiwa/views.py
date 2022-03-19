import json
import random

from . import turn

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
        island = user_island.island
        money = user_island.money
        food = user_island.food
        people = user_island.people
        farm_worker = user_island.farm_worker
        factory_worker = user_island.factory_worker
        mine_worker = user_island.mine_worker
        return JsonResponse({'name':name,'island':island,'money':money,'food':food,
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

        island = turn.create_island(island)
        
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
        island = user_island.island
        money = user_island.money
        food = user_island.food
        people = user_island.people
        farm_worker = user_island.farm_worker
        factory_worker = user_island.factory_worker
        mine_worker = user_island.mine_worker

        (people,
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
        town_position) = turn.start_process(island)

        food = turn.harvest_processing(farm_worker)
        money = turn.income_processing(factory_worker,mine_worker)
        food = turn.food_processing(food,people)
        money = turn.cashing_processing(money)

        (people,
        farm_worker,
        factory_worker,
        mine_worker) = turn.end_processing

        try:
            user_island.name = name
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
        
        return JsonResponse({'name':name,'island':island,'money':money,'food':food,
        'people':people,'farm_worker':farm_worker,'factory_worker':factory_worker,'mine_worker':mine_worker})