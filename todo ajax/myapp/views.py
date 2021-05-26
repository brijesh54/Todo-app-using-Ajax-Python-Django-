from django.shortcuts import render
from django.urls import reverse_lazy
from .models import CrudUser
from django.views.generic import TemplateView, View, DeleteView
from django.views.generic import ListView
from django.core import serializers
from django.http import JsonResponse


class CrudView(ListView):
    model = CrudUser
    template_name = 'crud.html'
    context_object_name = 'users'


class CreateCrudUser(View):
    def  get(self, request):
        name1 = request.GET.get('name', None)
        title1 = request.GET.get('title', None)
        status1 = request.GET.get('status', None)
        priority1 = request.GET.get('priority', None)

        obj = CrudUser.objects.create(
            name = name1,
            title = title1,
            status = status1,
            priority = priority1
        )

        user = {'id':obj.id,'name':obj.name,'title':obj.title,'status':obj.status,'priority':obj.priority}

        data = {
            'user': user
        }
        return JsonResponse(data)

class DeleteCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        CrudUser.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class UpdateCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        title1 = request.GET.get('title', None)
        status1 = request.GET.get('status', None)
        priority1 = request.GET.get('priority', None)

        obj = CrudUser.objects.get(id=id1)
        obj.name = name1
        obj.title = title1
        obj.status = status1
        obj.priority = priority1
        obj.save()

        user = {'id':obj.id,'name':obj.name,'title':obj.title,'status':obj.status,'priority':obj.priority}

        data = {
            'user': user
        }
        return JsonResponse(data)