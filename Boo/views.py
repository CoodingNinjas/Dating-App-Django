from django.shortcuts import render

# Create your views here.

def product(request):
    return render(request, 'product.html')

def learn(request):
    return render(request, 'learn.html')

def policy(request):
    return render(request, 'policy.html')

def security(request):
    return render(request, 'security.html')

def guildline(request):
    return render(request, 'guildline.html')

def register(request):
    return render(request, 'register.html')

def signin(request):
    return render(request, 'signin.html')


