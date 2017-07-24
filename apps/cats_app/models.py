# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login.models import User
# Create your models here.
class CatManager(models.Manager):
    def addCat(self, postData, request):
        results = {"valid": True, "errors": []}
        if not postData['cat_name']:
            results['valid'] = False
            results['errors'].append("Please give a name to your cat")
        if not postData['cat_age']:
            results['valid'] = False
            results['errors'].append("Please give an age for your cat")
        if results['valid']:
            Cat.objects.create(name = postData['cat_name'], user = User.objects.get(id = request.session['id']), age = postData['cat_age'])
        return results

class Cat(models.Model):
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    likes = models.IntegerField(default = 0)
    user = models.ForeignKey(User)
    date_added = models.DateTimeField(auto_now_add=True)
    objects = CatManager()
    def __str__(self):
        return self.name + " " + self.age + " " + self.user.first