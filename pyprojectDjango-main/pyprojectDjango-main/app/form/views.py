from django.http import HttpResponseRedirect
from django.shortcuts import render

from .form import UploadFileForm
from .models import OriginalForm, FakeForm
import random

# Create your views here.


def index(request):
    if request.method == 'GET':
        originalForm = OriginalForm.objects.all()
        fakeForm = FakeForm.objects.all()
        return render(request, 'form/index.html', {'originalForm': originalForm, 'fakeForm': fakeForm})
    if request.method == 'POST':
        
        request.FILES['file']
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        nationality = request.POST.get('nationality')
        phoneNumber = request.POST.get('phone_number')
        date = request.POST.get('date')
        sex = request.POST.get('sex')
        region = request.POST.get('region')
        doctor = request.POST.get('doctor')
        maladies = request.POST.get('maladies')
        wordFile = request.FILES['file']
        originalForm = OriginalForm(firstName=firstName, lastName = lastName, nationality = nationality, phoneNumber = phoneNumber, date = date, sex = sex, region = region, doctor = doctor, maladies = maladies, wordFile = wordFile)
        originalForm.save()
        fakeForm = FakeForm(firstName=firstName[1:-1], lastName = lastName, nationality = nationality, phoneNumber = phoneNumber, date = date[0:4], sex = sex, region = region, doctor = doctor, maladies = maladies, wordFile = wordFile)
        fakeForm.save()

        return HttpResponseRedirect('/')


    return render(request, 'form/index.html')