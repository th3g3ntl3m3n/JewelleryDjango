from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def cart(request):
    buyList = ItemPurchase.objects.all()
    length = len(buyList)
    return render(request, 'shop/cart.html', {'buyList':buyList, 'length':length, 'user':request.user})

def addToCart(request, product_id):
    buyPr = ItemPurchase()
    buyPr.user = request.user
    buyPr.product = Product.objects.get(pk = product_id)
    if buyPr.is_purchased:
        buyPr.is_purchased = False
    else:
        buyPr.is_purchased = True
    buyPr.quantity = 1
    buyPr.save()
    return HttpResponseRedirect('/jewellery')

def setQty(request, qty, buy_id):
    buyPr = ItemPurchase.objects.get(pk = buy_id)
    buyPr.quantity = int(qty)
    buyPr.save()
    return HttpResponseRedirect('/cart')

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'shop/login.html')
    else:
        products = Product.objects.all()
        corproducts = products[:4]
        context = {'products':products, 'user':request.user, 'corproducts':corproducts}
        return render(request, 'shop/index.html', context)

def register(request):
    form = UserForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/jewellery')
            else:
                return HttpResponseRedirect('/register')
        else:
            return render(request, 'shop/register.html', {'form':form})
    return render(request, 'shop/register.html',{'form':form})

def login_user(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/jewellery')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print user
        if user is not None:
            if user.is_active:
                login(request, user)
                # products = Product.objects.all()
                # return render(request, 'shop/index.html' ,{'products':products})
                print "logging in user"
                return HttpResponseRedirect('/jewellery/')
            else:
                return render(request, 'shop/login.html', {'error_message':"your account disabled"})
        else:
            return render(request, 'shop/login.html')
    return render(request, 'shop/login.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {'form':form}
    # return render(request, 'shop/login.html', context)
    return HttpResponseRedirect('/jewellery')

def detailproduct(request, product_id):
    product = Product.objects.get(pk = product_id)
    ctgs = Category.objects.all()
    revpr = ReviewProduct.objects.all()[::-1]
    if product:
        context = {'product':product, 'user':request.user, 'ctgs':ctgs, 'revpr':revpr}
        return render(request, 'shop/detail.html', context)

def saveReview(request, product_id):
    form = ReviewForm(request.POST)
    productRev = Product.objects.get(pk = product_id)
    if form.is_valid():
        reviews = form.save(commit=False)
        reviews.user = request.user
        reviews.product = productRev
        reviews.review = form.cleaned_data['review']
        reviews.rating = form.cleaned_data['rating']
        reviews.save()
        return HttpResponseRedirect('/detail/' + product_id)

def removeFromCart(request, buy_id):
    print buy_id
    buyPr = ItemPurchase.objects.get(pk = buy_id)
    buyPr.delete()
    return HttpResponseRedirect('/cart')

def checkout(request):
    buyItems = ItemPurchase.objects.all()
    form = ShoppingDetailForm(request.POST)
    # productRev = Product.objects.get(pk = product_id)
    print "hey in custormer detail"
    if form.is_valid():
        cstDetail = form.save(commit=False)
        cstDetail.full_name = form.cleaned_data['full_name']
        cstDetail.street = form.cleaned_data['street']
        cstDetail.town = form.cleaned_data['town']
        cstDetail.district = form.cleaned_data['district']
        cstDetail.state = form.cleaned_data['state']
        cstDetail.country = form.cleaned_data['country']
        cstDetail.pin = form.cleaned_data['pin']
        cstDetail.save()
        return HttpResponseRedirect('/thank/')
    return render(request, 'shop/checkout.html', {'form':form ,'buyItems':buyItems, 'user':request.user})
    # Class based Views

def showRings(request):
    rings = Products.category.objects.filter(cname = 'rings')

def about(request):
    return render(request, 'shop/about.html')

def thankYouPage(request):
    return render(request, 'shop/thank.html')
