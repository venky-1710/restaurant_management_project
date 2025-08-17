from django.conf import settings

def restaurant_name(request):
    return {
        'RESTAURANT_NAME': getattr(settings, 'RESTAURANT_NAME', 'Restaurant')
    }