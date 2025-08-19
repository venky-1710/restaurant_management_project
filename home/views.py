from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from .models import MenuItem
from datetime import datetime

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
    

from .models import Restaurant, MenuItem

def homepage(request):
    restaurant = Restaurant.objects.first()  # get first restaurant
    menu = MenuItem.objects.all()
    return render(request, 'homepage.html', {
        'restaurant': restaurant,
        'menu': menu
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

from .models import RestaurantInfo

from .models import Restaurant

def home_view(request):
    restaurant = Restaurant.objects.first()  # fetch the first (or only) restaurant
    return render(request, 'home.html', {'restaurant': restaurant})
def home(request):
    return render(request, "home.html", {
        "restaurant_name": settings.RESTAURANT_NAME,
        "restaurant_address": settings.RESTAURANT_ADDRESS,
        "current_year": datetime.now().year,
    })

from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_success')  # Redirect after saving
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})


from .forms import ContactForm

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save to database
            return redirect('home')  # Redirect after successful submission
    else:
        form = ContactForm()

    return render(request, 'home.html', {'form': form})

from .models import RestaurantInfo

def home(request):
    restaurant_name = RestaurantInfo.objects.first()  # get first entry
    return render(request, 'home.html', {'restaurant_name': restaurant_name})


def menu(request):
    # Fetch all menu items from database
    items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})


from .models import MenuItem

def menu_view(request):
    items = MenuItem.objects.all()
    return render(request, 'home/menu.html', {'items': items})

from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Store in DB
            return redirect('contact')  # Redirect to the same page (or a "thank you" page)
    else:
        form = ContactForm()

    return render(request, "contact_us.html", {"form": form})





from django.shortcuts import render
from .models import MenuItem, RestaurantDetails

def homepage(request):
    menu = MenuItem.objects.all()
    details = RestaurantDetails.objects.first()
    return render(
        request,
        "home.html",
        {
            "menu": menu,
            "details": details,
        }
    )





