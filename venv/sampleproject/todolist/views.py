from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import task
from . serializers import todoListSerializer
from django.utils import timezone


class todoList(APIView):
    def get(self, request):
        now = timezone.now()
        task1 = task.objects.all()
        searializer = todoListSerializer(task1, many = True)
        for e in task1:
            if not e.complete:
                if e.due<now:
                    e.overdue=True
                    e.save()
                else:
                    e.overdue=False
                    e.save()
        return(Response(searializer.data))

    def post(self, request):
        data = request.data
        task.objects.create(
            title=data['title'],
            complete=data['complete'],
            due=data['due'],
            overdue=data['overdue']
        )
        # if form.is_valid():
        #     text = form.cleaned_data['post']
        return(Response(request.data))

    def put(self, request):
        data = task.objects.get(id=request.data['id'])
        # data = request.data
        data.complete=request.data['complete']
        data.save()
        return(Response(request.data))
