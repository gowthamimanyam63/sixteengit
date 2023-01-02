from django.shortcuts import render

# Create your views here.
def operations3(request):
    d={'a':60,'b':80,'c':40}
    return render(request,'operations3.html',d)

