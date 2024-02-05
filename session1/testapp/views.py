from django.shortcuts import render

# Create your views here.
def count_view(request):
    count = request.COOKIES.get('count',0)
    count = int(count)
    count += 1
    response =  render(request, 'html/home.html', {'count':count})
    response.set_cookie('count',count)
    return response
