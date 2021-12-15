from django.shortcuts import render,HttpResponse

# Create your views here.
def homePage(request):
    return render(request,'index.html')

def myth(request):
    return render(request,'myth.html')
    
def create(request):
    return render(request,'create.html')

def cricket(request):
    return render(request, 'cricket.html')