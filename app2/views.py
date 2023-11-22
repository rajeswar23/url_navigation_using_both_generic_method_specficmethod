from django.shortcuts import render

# Create your views here.
def mom(request):
    return render(request,'mom.html')
def frnd(request):
    return render(request,'frnd.html')