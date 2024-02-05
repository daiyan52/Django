from django.shortcuts import render
from testapp.forms import studentForm

def student_view(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            captcha_response = form.cleaned_data['captcha']

            # Verify captcha
            if request.session.get('django_simple_captcha_passed') == captcha_response:
                return render(request, 'htmlfolder/student.html', {'name': name})
            else:
                return render(request, 'htmlfolder/student.html', {'error': 'Invalid captcha'})
    else:
        form = studentForm()

    return render(request, 'htmlfolder/student.html', {'form': form})
