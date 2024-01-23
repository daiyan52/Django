from django.shortcuts import render
import datetime
# Create your views here.
def wish(request):
    date = datetime.datetime.now();
    my_dict = {'x' : date}
    buddies_dict ={'b1': 'Daiyan','b2':'Raju','b3':'Anish'}
    context = {**my_dict, **buddies_dict}
    return render(request,'html/wish.html',context=context)
