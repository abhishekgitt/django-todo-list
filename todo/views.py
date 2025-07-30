from django.shortcuts import render ,redirect
from .forms import TodoForm
from .models import Todo

def home(request):
    if(request.method == 'POST'):
        form = TodoForm(request.POST) # filled submited  form , created in forms.py's TodoForm Meta sub class
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoForm() #blank submmited form , created in forms.py's TododForm Meta sub class

        """ '-created_at : is new list item first ,  
            'created_at :  is old list item first"""
        
        tasks = Todo.objects.all().order_by('-created_at') 
        return render(request,'todo/home.html',{'form':form,'tasks':tasks})