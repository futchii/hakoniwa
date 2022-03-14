import json
import random

from . import turn

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .models import Islands

#ターン関係の関数にはprocessingをつけるs

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

class CashingView(APIView):
    def get(self,request):
        user_island = Islands.objects.get(account=request.user)
        message = user_island.name
        return JsonResponse({'message':message})