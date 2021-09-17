from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import todoItem

# Create your views here.
def displayPage(request):
    all_todo_items = todoItem.objects.all()
    return render(request, 'todo.html',
    {'all_items' : all_todo_items})
    
def addTodo(request):
   todoItem(content = request.POST['content']).save()
   return HttpResponseRedirect('/todofront/')

def deleteTodo(request, todo_id):
    item_to_delete = todoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todofront/')