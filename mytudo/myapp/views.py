from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404
from .models import Task
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            #save the new user from the form
            user = form.save()

            # login the user after registration
            login_user = authenticate(username=user.username, password=form.cleaned_data.get('password1'))
            if login_user:
                login(request, login_user)
                return redirect('home')

    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

@login_required
@require_POST
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('home')

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # put the logged-in user as the task owner
            task.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'myapp/add_task.html', {'form': form})

@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user).order_by('-date')
    return render(request, 'myapp/home.html', {'tasks': tasks})
