from django.shortcuts import render

# Create your views here.
def HomePage(request):
  return render(request, 'website/index.html')

def Contact(request):
  return render(request, 'website/contact.html')

def About(request):
  return render(request, 'website/aboutus.html')