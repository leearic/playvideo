from django.shortcuts import render

# Create your views here.



def index(request):

    return  render(request, template_name='webapps2/sports.html')



def video(request):

    return  render(request, template_name='webapps2/single.html')