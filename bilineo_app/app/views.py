from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Store, FoodItem, TrayItem
from .templates import *
from django.http import JsonResponse
import json, logging

# Create your views here.
logger = logging.getLogger(__name__)

def login_page(request):
   return render(request, "login_page.html", {'title': 'Login'})

def home_desktop_redirect(request):
   return redirect(home_desktop)

def home_desktop(request):
   return render(request, "home_desktop.html", {'title': 'Home'})

def messages_page(request):
   return render(request, "messages_page.html", {'title': 'Messages'})

def orders_page(request):
   return render(request, "orders_page.html", {'title': 'Orders'})

def profile_page(request):
   return render(request, "profile_page.html", {'title': 'Profile'})

def restaurant_detail_page(request):
   store_detail = FoodItem.objects.all()
   context = {
      'store_detail': store_detail,
      'title': 'Store Details',
   }
   return render(request, "restaurant_detail_page_desktop.html", context)

@csrf_exempt
def add_food(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            store_id = data.get('store_id')
            food_id = data.get('food_id')

            if store_id is None or food_id is None:
                logger.error(f"Missing store_id or food_id: store_id={store_id}, food_id={food_id}")
                return JsonResponse({'status': 'error', 'message': 'Missing store_id or food_id'}, status=400)

            try:
                tray_item = TrayItem.objects.get(store_id_id=store_id, food_id_id=food_id)
                tray_item.quantity += 1
                tray_item.save()
                return JsonResponse({'status': 'success', 'message': 'Quantity updated successfully'})
            except TrayItem.DoesNotExist:
                TrayItem.objects.create(quantity=1, food_id_id=food_id, store_id_id=store_id)
                return JsonResponse({'status': 'success', 'message': 'Food added successfully'})
        except json.JSONDecodeError:
            logger.error("Invalid JSON")
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            logger.exception("Unexpected error")
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid HTTP method'}, status=405)

def store_page(request):
   stores = Store.objects.all()
   context = {
      'stores': stores,
      'title': 'Stores',
   }
   return render(request, "store_page.html", context)

def tray_page(request):
   stores = Store.objects.all()
   trayItems = TrayItem.objects.all()
   foodItems = FoodItem.objects.all()
   context = {
      'stores': stores,
      'tratItems': trayItems,
      'foodItems': foodItems,
      'title': 'Tray',
   }
   return render(request, "tray_page.html", context)