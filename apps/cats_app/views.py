# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Cat
from django.contrib import messages

def status(valid, request):
    if not valid:
        messages.error(request, "No hacking! Please log in first")
        return True

def index(request):
    if status(request.session['status'], request):
        return redirect('/')
    print Cat.objects.all()
    context = {
        "cats": Cat.objects.all()
    }
    return render(request, 'cats_app/index.html', context)

def add_home(request):
    if status(request.session['status'], request):
        return redirect('/')
    return render(request, 'cats_app/add.html')

def add(request):
    if status(request.session['status'], request):
        return redirect('/')
    results = Cat.objects.addCat(request.POST, request)
    if results['valid']:
        return redirect('/cats')
    else: 
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/cats/add_home')

def delete(request, id): 
    if status(request.session['status'], request):
        return redirect('/')
    Cat.objects.get(id = id).delete()
    return redirect('/cats')

def edit(request, id):
    if status(request.session['status'], request):
        return redirect('/')
    context = {
        "cat": Cat.objects.get(id = id)
    }
    return render(request, "cats_app/edit.html", context)

def edit_info(request, id):
    if status(request.session['status'], request):
        return redirect('/')
    Cat.objects.filter(id = id).update(name = request.POST['name'] , age = request.POST['age'])
    return redirect('/cats')

def show(request, id):
    if status(request.session['status'], request):
        return redirect('/')
    context = {
        "cat": Cat.objects.get(id = id)
    }
    return render(request, "cats_app/show.html", context)

def like(request, id):
    if status(request.session['status'], request):
        return redirect('/')
    Cat.objects.filter(id = id).update(likes = Cat.objects.get(id = id).likes + 1)
    return redirect('/cats')