from django.shortcuts import render
from django.http import HttpResponse
from .models import SanPham, Infomation

def index(request):
    return render(request, 'PyShop/index.html')
    # products = SanPham.objects.all()
    # return render(request, 'index.html', {'products': products})


# def information(request):
#     info = Infomation.objects.all()
#     return render(request, 'home.html', {'info': info})
#
# def navigate(request):
#     return render(request, 'navigate.html')
