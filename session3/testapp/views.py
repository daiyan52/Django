from django.shortcuts import render
from testapp.forms import addItemForm
# Create your views here.

def homeView(request):
    return render(request, 'pages/home.html')
def addItemForm_view(request):
    form = addItemForm()
    response =  render(request,'pages/addItemForm.html',{'form':form})

    if request.method == 'POST':
        form = addItemForm(request.POST)
        if form.is_valid():
            itemName = form.cleaned_data['itemName']
            quantity = form.cleaned_data['quantity']

            response.set_cookie(itemName, quantity)
    return response

def listItemView(request):
    return render(request,'pages/listItem.html')

