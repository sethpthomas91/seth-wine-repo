from django.http import JsonResponse
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from wine_app.forms import WineForm
from wine_app.models import Wine
from wine_app.serializers import WineSerializer
import json

def wine_list(request):
    wines = Wine.objects.all()
    serialized_wines = WineSerializer().convert_all(wines)
    return JsonResponse(data=serialized_wines, status=200)

def wine_detail(request, wine_id):
    wine = Wine.objects.get(id=wine_id)
    serialized_wine = WineSerializer().convert_one(wine)
    return JsonResponse(data=serialized_wine, status=200)

@csrf_exempt
def create_wine(request):
    if request.method == "POST":
        data = json.load(request)
        form = WineForm(data)
        if form.is_valid():
            wine = form.save(commit=True)
            serialized_wine = WineSerializer().convert_one(wine)
            return JsonResponse(data=serialized_wine, status=200)
    return HttpResponse("404: Bad Request.")

@csrf_exempt
def edit_wine(request, wine_id):
    wine = Wine.objects.get(id=wine_id)
    if request.method == "PUT":
        data = json.load(request)
        form = WineForm(data, instance=wine)
        if form.is_valid():
            wine = form.save(commit=True)
            serialized_wine = WineSerializer().convert_one(wine)
            return JsonResponse(data=serialized_wine, status=200)
    return HttpResponse("404: Bad Request.")

@csrf_exempt
def delete_wine(request, wine_id):
    if request.method == "DELETE":
        wine = Wine.objects.get(id=wine_id)
        wine.delete()
    return JsonResponse(data={'status': 'Successfully deleted wine.'}, status=200)