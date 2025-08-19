from django.shortcuts import get_object_or_404, render
from car.forms import CarForm
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import generics,permissions
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
import requests
from django.conf import settings




# Create your views here.
class CarListCreateAPIView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [AllowAny]
    
    
class CarDetailView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
    
class CarUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
    
class CarDeleteView(generics.DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
    

API_BASE_URL = 'http://web:8000/carscreate/'

def car_list(request):
    cars = Car.objects.all()
    return render(request,'car_list.html',{'cars':cars})

def car_details(request,pk):
    car = get_object_or_404(Car,pk=pk)
    return render(request,'car_details.html',{'car':car})


def car_create(request):
    if request.method == 'POST':
        data = request.POST.dict()
        files = []
        
        try:
        
         response = requests.post(
            API_BASE_URL,
            data = data,
            files = files
         )
         if response.status_code == 201:
            messages.success(request,'Car Created Successfully!')
            return redirect('car_list')
         else:
            messages.error(request,f"Error Creating Car:{response.json()} ")
        except requests.exceptions.RequestException:
            messages.error(request,'Failed to connect to the API server')
    return render(request,'car_create.html',{'title':'create car'})


def car_update(request,pk):
    car = get_object_or_404(Car,pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST,request.FILES,instance = car)
        if form.is_valid():
            form.save()
            messages.success(request,'Car updated successfully')
            return redirect('car_details',pk=pk)
    else:
        form = CarForm(instance = car)
    return render(request,'car_form.html',{'form':form})


def car_delete(request,pk):
    car = get_object_or_404(Car,pk=pk)
    if request.method == 'POST':
        car.delete()
        messages.success(request,'Car delete successfully.')
        return redirect('car_list')
    return render(request,'car_confirm_delete.html',{'car':car})