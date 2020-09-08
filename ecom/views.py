from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

class initial(View):
  def get(self,reuest):
    return render(reuest,"index.html")
    # return HttpResponse("<h1>Welcome</h1>")
def store(request):
  context={}
  return render(request,"store/store.html")

def cart(request):
  context={}
  return render(request,"store/cart.html")

def checkout(request):
  context={}
  return render(request,"store/checkout.html")