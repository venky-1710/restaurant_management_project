from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class MenuAPIView(APIView):
    def get(self, request):
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
            },
            {
                "name": "Veg Biriyani",
                "description":"Aromatic basmati rice cooked with fresh vegetables and spices",
                "price": 220
            }
        ]
        return Response(menu)


import requests
from django.shortcuts import render

def menu_page(request):
    try:
        response = requests.get('http://localhost:8000/api/menu/')
        menu_data = response.json()
    except Exception as e:
        menu_data = []
        print("Error fetching menu:", e)

    return render(request, 'home/menu.html', {'menu': menu_data})

def about_page(request):
    return render(request, 'about.html')

def homepage(request):
    restaurant_name = "Gourmet Paradise"  # You can also fetch this from settings.py or the database
    return render(request, "homepage.html", {"restaurant_name": restaurant_name})