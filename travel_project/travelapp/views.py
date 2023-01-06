from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team
# Create your views here.


def demo(request):
    obj = Place.objects.all()
    memb = Team.objects.all()
    return render(request, "index.html", {'result':obj,
                                          'team':memb})


# def about(request):
#     return render(request, "about.html")
#
#
# def contact(request):
#     return HttpResponse("Flying!!!")
#
#
# def add(request):
#     x = request.GET['num1']
#     y = request.GET['num2']
#     res = int(x) + int(y)
#     return render(request, 'result.html', {'result':res,
#                                            'num1':x,
#                                            'num2':y})