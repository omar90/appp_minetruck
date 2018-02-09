from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from webapp.models import Garage, Model_truck


def index(request):
    template=loader.get_template('webapp/home.html')
    context={"garages":Garage.objects.all()}
    return HttpResponse(template.render(context,request))

def contact(request):
    template = loader.get_template('webapp/basic.html')
    listingsa = Model_truck.objects.all()



    if request.GET.get('featured'):
        featured_filter = request.GET.get('lista')


        if featured_filter == "0":

            listings = Garage.objects.all()
        else:
            listings = Garage.objects.filter(model=featured_filter)

    else:
        listings = Garage.objects.all()

    context_dict = {'garages': listings,'models':listingsa}
    return HttpResponse(template.render(context_dict, request))
def contactIS(request):
    return render(request, 'webapp/basic.html',{'content':['If you would like to contact me, please email me.','hskinsley@gmail.com']})
# Create your views here.return render(request, 'webapp/home.html')
