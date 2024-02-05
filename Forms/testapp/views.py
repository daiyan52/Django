from django.shortcuts import render
from testapp.forms import EmployeeForm
# Create your views here.

def EmployeeForm_view(request):
    submitted = False
    fname = ''
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data['name'])
            # print(form.cleaned_data['marks'])
            fname = form.cleaned_data['First_Name']
            submitted = True
    form = EmployeeForm()
    my_dict = {'form': form,'fname': fname,'submitted': submitted}
    return render(request, 'HtmlFolder/form.html', my_dict)
