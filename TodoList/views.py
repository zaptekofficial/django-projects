from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Task
from django.views.generic import ListView, CreateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
# Create your views here.


class HomeView(LoginView):
    template_name = 'TodoList/home.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            username = str(self.request.user.username)
            return HttpResponseRedirect(reverse('todolist-main', args=(username,)))

        return super(HomeView, self).get(request, *args, **kwargs)


def mark_complete(request, username, task_id):
    task = Task.objects.get(id=task_id)
    task.status = True
    task.save()
    return HttpResponseRedirect(reverse('todolist-main', args=(username,)))


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'TodoList/todolist_main.html'
    paginate_by = 5

    def get_queryset(self):
        return Task.objects.filter(creator=self.request.user).order_by('-deadline')


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'description', 'deadline']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TaskCreateView, self).form_valid(form)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'TodoList/register.html', {'form': form})

