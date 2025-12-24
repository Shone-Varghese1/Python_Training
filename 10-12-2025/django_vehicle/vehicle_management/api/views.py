from django.shortcuts import render
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from .models import Vehicle
import json

@csrf_exempt
def vehicles(request):
    if request.method == 'GET':
        data = list(Vehicle.objects.values())
        return JsonResponse(data, safe=False)
    if request.method == 'POST':
        body = json.loads(request.body.decode("utf-8"))
        Vehicle.objects.create(
            number_plate=body['number_plate'],
            year=body['year'],
            manufacturer=body['manufacturer'],
            vehicle_type=body['vehicle_type'],
            )
        return  JsonResponse({"message": "Post Executed"})
    if request.method == 'PUT':
        body = json.loads(request.body.decode("utf-8"))
        veh=Vehicle.objects.get(id=body['id'])
        veh.number_plate=body['number_plate']
        veh.year=body['year']
        veh.manufacturer=body['manufacturer']
        veh.vehicle_type=body['vehicle_type']
        veh.save()
        return JsonResponse({"message": "Put Executed"})
    if request.method == 'DELETE':
        body = json.loads(request.body.decode("utf-8"))
        veh=Vehicle.objects.get(id=body['id'])
        veh.delete()
        return JsonResponse({"message": "Delete Executed"})
    return JsonResponse({"error": "Method Not Allowed"},status=405)

