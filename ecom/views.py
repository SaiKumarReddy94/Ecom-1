from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


class initial(View):
    def get(self, reuest):
        return render(reuest, "index.html")
        # return HttpResponse("<h1>Welcome</h1>")

# class SignUpView(View):
#     def get(self, request, *args, **kwargs):
#         f = UserCreationForm()
#         return render(request, 'store/signup.html', context={'form': f})

#     def post(self, request, *args, **kwargs):
#         f = UserCreationForm(request.POST)
#         if f.is_valid():
#             User.objects.create_user(username=f.cleaned_data['username'], password=f.cleaned_data['password1'])
#             return redirect('/login/')
#         return render(request, 'store/signup.html', {'form': f})

# class LoginView(View):
#     def get(self, request, *args, **kwargs):
#         f = AuthenticationForm()
#         return render(request, 'store/login.html', context={'form': f})

#     def post(self, request, *args, **kwargs):
#         f = AuthenticationForm(data=request.POST)
#         if f.is_valid():
#             user = authenticate(username=f.cleaned_data['username'], password=f.cleaned_data['password'])
#             if user is not None:
#                 login(request, user)
#                 return redirect('/')
#             else:
#                 print("The username and password were incorrect.")
#         return render(request, 'login.html', {'form': f})


# class LogoutView(View):
#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return redirect('/')

def store(request):
    products = Product.objects.all()
    print(products)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0,"shipping":False}
        cartItems=order["get_cart_items"]
    context = {"Product": products,"cartItems":cartItems}
    return render(request, "store/store.html", context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0,"shipping":False}
        cartItems=order['get_cart_items']

    context = {"items": items, "order": order,"cartItems":cartItems}
    return render(request, "store/cart.html", context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        email= customer.email
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items = []
        email=""
        order = {"get_cart_total": 0, "get_cart_items": 0,"shipping":False,"email":""}
        cartItems=order['get_cart_items']
    context = {"items": items, "order": order,"cartItems":cartItems,"email":email}
    return render(request, "store/checkout.html", context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data["productID"]
    action = data["action"]
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    orderItem,created = OrderItem.objects.get_or_create(
        order=order, product=product)
    if action=="add":
        orderItem.quantity+=1
    elif action=="remove":
        orderItem.quantity-=1
    orderItem.save()
    if orderItem.quantity<=0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)
