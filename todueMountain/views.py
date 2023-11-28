from django.shortcuts import render
from django.views import View
from .models import tdTask, journalEntry
from .forms import TaskForm, EntryForm
from django.views.generic import (CreateView, DetailView,  
                                  UpdateView, DeleteView, FormView)
    
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

#         Login, Logout, registration, authentication :>

class appLogin(LoginView):
     template_name = 'todueMountain/login.html'
     fields = '_all_'
     redirect_authenticated_user = True
     success_url = '/'
     
class appLogout(LogoutView):
     template_name = 'todueMountain/login.html'
     fields = '_all_'
     redirect_authenticated_user = True
     success_url = '/'
     
class appRegister(FormView):
     template_name = 'todueMountain/register.html'
     form_class = UserCreationForm
     redirect_authenticated_user = True
     success_url = '/'
     
     def form_valid(self, form):
          user = form.save()
          if user is not None:
               login(self.request, user)
          return super(appRegister, self).form_valid(form)
     
     

#home <3
class planner(LoginRequiredMixin, View):
     
     def get(self, request):
          task_list = tdTask.objects.all()
          entry_list = journalEntry.objects.all()
          context ={
               'task_list' :  task_list.filter(user=self.request.user),
               'entry_list' : entry_list.filter(user=self.request.user),}
          return render(request, 'todueMountain/home.html', context)
    
        #Create, read, update delete TASKS       
        
class task_detail(LoginRequiredMixin,DetailView):
    model = tdTask
    template_name = 'todueMountain/task_detail.html'

class createTask(LoginRequiredMixin,CreateView):
     model = tdTask
     fields = ['TaskTitle', 'TaskDescr', 'Taskdotf', 'checked']
     template_name = 'todueMountain/create_task.html'
     success_url = '/'
     
     def form_valid(self, form):
         form.instance.user = self.request.user
         return super(createTask, self).form_valid(form)
     
     
               
class updateTask(LoginRequiredMixin,UpdateView):
     model = tdTask
     form_class = TaskForm
     template_name = 'todueMountain/update_task.html'
     success_url = '/'

class deleteTask(LoginRequiredMixin,DeleteView):
     model = tdTask
     template_name = 'todueMountain/delete_task.html'
     context_object_name = 'task'
     success_url = '/'
     
     #Create, read, update delete JOURNAL ENTRIES

class entry_detail(LoginRequiredMixin,DetailView):
    model = journalEntry
    template_name = 'todueMountain/entry_detail.html'

class createEntry(LoginRequiredMixin,CreateView):
     model = journalEntry
     fields = ['EntryTitle', 'mood', 'entryText', 'Entrydotf']
     template_name = 'todueMountain/create_entry.html'
     success_url = '/'
     
     def form_valid(self, form):
         form.instance.user = self.request.user
         return super(createEntry, self).form_valid(form)
               
class updateEntry(LoginRequiredMixin,UpdateView):
     model = journalEntry
     form_class = EntryForm
     template_name = 'todueMountain/update_entry.html'
     success_url = '/'

class deleteEntry(LoginRequiredMixin,DeleteView):
     model = journalEntry
     template_name = 'todueMountain/delete_entry.html'
     context_object_name = 'entry'
     success_url = '/'

