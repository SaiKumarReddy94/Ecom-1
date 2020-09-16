from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *
# Create your views here.

class initial(View):
  def get(self,reuest):
    return render(reuest,"index.html")
    # return HttpResponse("<h1>Welcome</h1>")
def store(request):
  products=Product.objects.all()
  print(products)
  context={"Product":Product}
  return render(request,"store/store.html",{"Product":products})

def cart(request):
  context={}
  return render(request,"store/cart.html")

def checkout(request):
  context={}
  return render(request,"store/checkout.html")