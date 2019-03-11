from django.shortcuts import render
# from django.template import loader
# from django.http import HttpResponse, HttpRequest
from todo_app.models import Task
import re

def list_all(request, taskn):

    tasks = Task.objects.all()
    if taskn:
        taskn = int(taskn)
        tskid = Task.objects.all().values_list('id', flat=True)
        if taskn in tskid:
            tasks = Task.objects.filter(id=taskn)
            addt = ''
        else:
            addt  = '  ~~~~ !!! Non existent ID !!! ~~~~'
            tasks = []
        paget = 'Tasks filtered by ID: ' + str(taskn) + addt
    else:
        paget = 'All My Tasks '

    template_file = 'todo_app/list.html'

    context = {
        'tasks': tasks,
        'page_title': paget
    }

    template_file = 'todo_app/list.html'

    return render(request, template_file, context)

# def list_part(request, year, month):
def list_part(request, year, month):
    alltasks = Task.objects.all()
    seltasks =  []
    # pagetitl = 'Filtered Tasks : ' + year + ' - ' + month
    pagetitl = 'Filtered Tasks by '
    
    if ( year and month ):
        pagetitl = pagetitl + 'year ' + year + ' and month  ' + month       
        for t in alltasks:
            if (t.due.year == int(year)) and (t.due.month == int(month)):
                seltasks.append(t.title)
                print(t.title)
    elif year:
        pagetitl = pagetitl + 'year ' + year
        for t in alltasks:
            if t.due.year == int(year):
                seltasks.append(t.title)
                print(t.title)
 
    template_file = 'todo_app/index.html'

    context = {
        'selected': seltasks,
        'page_title': pagetitl
    }

    return render(request, template_file, context)

def delete(request, **kwargs):

    taskn = kwargs['id']
    tasks = Task.objects.all()

    context = {
        'tasks': tasks,
        'taskn': taskn,
        'page_title': 'Todo App Index'
    }
   
    return render(request, 'todo_app/delete.html', context)

# delete({}, id=2)

# Create your views here.
# def index(request): 
#     tasks = Task.objects.all()
#     print(tasks)

#     template_file = 'todo_app/index.html'

#     context = {
#         'tasks': tasks,
#         'page_title': 'Todo App Index'
#     }


#     return render(request, template_file, context)

# http://127.0.0.1:8000/list
# def list(request, taskn):
#     import datetime
    
#     now = datetime.datetime.now()
    
#     template_file = 'todo_app/list.html'

#     # return HttpResponse('OK')

#     return render(request, template_file, {'taskn':taskn})

# def table(request):
#     latest_tasks = Task.objects.order_by('due')[:5]



#     context = {
#         'latest_tasks': latest_tasks
#     }

#     template_file = 'todo_app/table.html'


#     return render(request, template_file, context)

