from django.shortcuts import render

# Create your views here.
def Header_view(request):
    return render(request,'HTMLFOLDER/index.html')

#
def Admission_view(request):
    my_dict = {'eng' : 'Engineering Addimmsion is started from 3rd March', 'type' : 'Admission'}

    return render(request,'HTMLFOLDER/News.html',my_dict)

def Sports_view(request):
    my_dict = {'eng' : 'Engineering Addimmsion is started from 3rd March','type': 'Sports'}
    return render(request,'HTMLFOLDER/News.html',my_dict)

def Placement_view(request):
    my_dict = {'eng' : 'Engineering Addimmsion is started from 3rd March','type': 'Placement'
}
    return render(request,'HTMLFOLDER/News.html',my_dict)
