# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Reg
from django.shortcuts import render, redirect
from django.contrib import messages
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# apps.secret_key = "keepitasecretbozo"

def index(request):
    print ("***** view.py file index function ****")

    return render(request, "loginreg_set/index.html")

def register(request):
    print ('*************** error function ************')
    result = Reg.objects.Reg_validator(request.POST)
    if type(result) == list:
        for err in result:
                messages.error(request, err)
        return redirect('/')
    request.session['Reg_id'] = result.id
    messages.success(request, "Successfully registered!")
    return redirect('/success')


    # return redirect('/'+id)

def login(request):
    print ("*********** login page   ***********")
    result = Reg.objects.login_validator(request.POST)
    if type(result) == list:
        for item in result:
            messages.error(request, item)
        return redirect('/')
    request.session['Reg_id'] = result.id
    messages.success(request, "Welcom Back, Successfully logged in!")
    return redirect('/success')

def success(request):
    try:
        request.session['Reg_id']
    except KeyError:
        return redirect('/')
    context = {
        'Reg': Reg.objects.get(id=request.session['Reg_id'])

    }
    print ("***************** regobj ***********",Reg.objects)
    return render(request, 'loginsuccess_set/success.html', context)
