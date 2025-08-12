from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from .models import MenuItem
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
    return render(request, 'homepage.html', {
        'restaurant_name': 'My Awesome Restaurant',
        'phone_number': settings.RESTAURANT_PHONE_NUMBER
    })

def contact_us(request):
    context = {
        "restaurant_name": "My Awesome Restaurant",
        "phone_number": "+1 (555) 123-4567",
        "email": "contact@myrestaurant.com",
        "address": "123 Main Street, Springfield, USA"
    }
    return render(request, "contact_us.html", context)

def reservations_page(request):
    return render(request, 'reservations.html')

def home_view(request):
    try:
        menu_items = MenuItem.objects.all()  # Database query
        return render(request, 'home.html', {'menu_items': menu_items})
    except Exception as e:
        # Log the error (optional)
        print(f"Error loading homepage: {e}")
        # Show a user-friendly message
        return HttpResponse("Sorry, something went wrong. Please try again later.", status=500)















