from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from ..lognreg_set.models import Reg
from django.shortcuts import render, redirect
from django.contrib import messages

# def index(request):
#     print ("***** view.py file app2 ****")
#     return redirect('/')
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


# Create your views here.
