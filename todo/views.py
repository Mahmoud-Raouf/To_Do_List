from django.shortcuts import render ,redirect ,get_object_or_404
from todo.models import *
from todo.forms import *
 

def todo_list(request):
    todoes = Todo.objects.all()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:todo')
    else:
        form = TodoForm()

    if request.method == 'POST':
        todo_id = request.POST['todo_id']
        todo = get_object_or_404(Todo , id=todo_id)
        print(todo)
        if todo.checked :
            todo.checked = False
            todo.save()
        else:
            todo.checked = True
            todo.save()

    return render(request , 'note/todo2.html' , {
        'todoes' : todoes ,
        'form' : form,
    })
    
def update_todo(request, pk):
    todo_id = Todo.objects.get(pk=pk)
    update_todo_form = TodoForm(instance=todo_id)
    if request.method == 'POST':
        update_todo_form = TodoForm(request.POST , instance=todo_id)
        if update_todo_form.is_valid():
            update_todo_form.save()
            return redirect('home:todo')
    else:
        update_todo_form = TodoForm( instance=todo_id)
    return render(request , 'note/update_todo.html' , {
        'update_todo_form' : update_todo_form,
})

def todo_delete(request , pk):
    todo_delete = Todo.objects.get(pk=pk)
    todo_delete.delete()
    return redirect('home:todo')