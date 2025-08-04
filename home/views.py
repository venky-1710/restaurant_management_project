from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import response

class MenuAPIView(APIView):
    def gets(self, request):
        menu = [
            {
                "name" : "Pizza",
                "description" : "Classic delight with 100% real mozzarella cheese",
                "price" : 250
            },
            {
                "name": "Paneer",
                "description":"Chunks of paneer marinated in tandoori masala",
                "price":180
            }
        ]
        return Response(menu)

# Create your views here.

