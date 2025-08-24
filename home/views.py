from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from .models import MenuItem, RestaurantDetails
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
    query = request.GET.get('q')
    if query:
        menu_items = MenuItem.objects.filter(name__icontains=query)
    else:
        menu_items = MenuItem.objects.all()
    
    return render(request, 'home.html', {
        'menu_items': menu_items,
        'query': query
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

from .models import Restaurant

def home(request):
    # Assuming you have only one restaurant entry
    restaurant = Restaurant.objects.first()

    return render(request, "home.html", {
        "restaurant": restaurant
    })


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
    # Get cart from session, default to empty dict
    cart = request.session.get('cart', {})
    total_items = sum(cart.values())  # total number of items

    return render(request, 'homepage.html', {
        'total_items': total_items,
    })

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Construct email
            subject = f"New Contact Form Submission from {name}"
            full_message = f"From: {name} <{email}>\n\nMessage:\n{message}"

            # Send email (settings must be configured)
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ['restaurant@example.com'],  # replace with restaurant email
            )

            return redirect('contact_success')  # redirect after success
    else:
        form = ContactForm()

    return render(request, "contact_us.html", {"form": form})





