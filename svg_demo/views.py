from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'svg_demo/index.html')


def roti(request):
    return render(request, 'svg_demo/replacementOfTwoImages.html')