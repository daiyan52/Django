from django.shortcuts import render
from testapp.models import Admin
from testapp.forms import AdminForm
# Create your views here.
def Home_view(request):
    return render(request, 'Home.html') 

def Add_Admin_view(request):
    form = AdminForm()
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'Home.html')
    return render(request, 'Admin_form.html', {'form': form})

def list_Admin_views(request):
    Admin_list = Admin.objects.all()
    return render(request, 'Admin_list.html', {'Admin_list': Admin_list})