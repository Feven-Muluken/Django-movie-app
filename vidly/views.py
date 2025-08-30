from django.shortcuts import render

app_name = 'movies'
def home(request):
  return render(request, 'home.html')
