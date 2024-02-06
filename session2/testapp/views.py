from django.shortcuts import render
from testapp.forms import loginForm
# Create your views here.
def login_view(request):
    form = loginForm()
    return render(request, 'html/home.html', {'form': form})


def second_view(request):
    # name = request.GET['name']
    name = request.COOKIES.get('name')
    response =  render(request, 'html/second.html', {'name': name})
    response.set_cookie('name', name)
    return response

