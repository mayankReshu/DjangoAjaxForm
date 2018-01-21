from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from testapp.models import User



# Create your views here.

def index(request):
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render())
    return render(request, 'index.html')


def create_user(request):
    print(request)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']

        User.objects.create(
            name=name,
            email=email
        )
        return HttpResponse()

