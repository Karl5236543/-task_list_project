from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from to_do_list.models import Task

def task_list(request, mode):
    tasks = Task.objects.all()
    print(mode)
    return render(request, 'to_do_list/task_list.html', context={'tasks': tasks, 'mode': mode})


def add_task(request):
    text = request.POST['text']
    details = request.POST['details']
    deadline = request.POST['deadline']
    Task.objects.create(text=text, details=details, deadline=deadline).save()
    return HttpResponsePermanentRedirect('/to_do_list/view')


def delete_task(request, task_id):
    Task.objects.get(id__iexact=task_id).delete()
    return HttpResponsePermanentRedirect('/to_do_list/delete')


def edit_task(request, task_id):
    task = Task.objects.get(id__iexact=task_id)
    task.text = request.POST['text']
    task.deadline = request.POST['deadline']
    task.details = request.POST['details']
    task.save()
    return HttpResponsePermanentRedirect('/to_do_list/edit')


def change_task_status(request, task_id):
    task = Task.objects.get(id__iexact=task_id)
    task.is_done = not task.is_done
    print(task.is_done)
    task.save()
    return HttpResponsePermanentRedirect('/to_do_list/view')