from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Products
import json
@csrf_exempt
def products(request):
    if request.method == "GET":
        data=list(Products.objects.values())
        return JsonResponse(data,safe=False)
    if request.method == "POST":
        body=json.loads(request.body.decode('utf-8'))
        Products.objects.create(
            product_name=body['product_name'],
            price=body['price'],
            quantity=body['quantity']
        )
        return JsonResponse({'Message':"post executed"})
    if request.method == "PUT":
        body=json.loads(request.body.decode('utf-8'))
        product=Products.objects.get(id=body["id"])
        product.product_name=body["product_name"]
        product.price=body["price"]
        product.quantity=body["quantity"]
        product.save()
        return JsonResponse({'Message':"put executed"})
    if request.method == "DELETE":
        body=json.loads(request.body.decode('utf-8'))
        product=Products.objects.get(id=body["id"])
        product.delete()
        return JsonResponse({'Message':"delete executed"})
    return JsonResponse({'error':"not allowed"})

