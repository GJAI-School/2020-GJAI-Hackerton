from django.shortcuts import render
from firstapp import views

# Create your views here.
def main(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'login.html')

def signin(request):
    return render(request, 'signin.html')

def logout(request):
    return redirect('main.html')

def post(request):
    return render(request, 'post.html')

def write_page(request):
    return render(request, 'write_page.html')
