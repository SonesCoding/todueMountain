
from django.urls import path 
#from .views import star_create, star_detail, checkout
from . import views
from .views import appLogin, appLogout, appRegister, planner, createTask, updateTask,deleteTask, task_detail, createEntry, entry_detail, deleteEntry,updateEntry

urlpatterns=[
    path('login/', appLogin.as_view(next_page = 'planner'), name='login'),
    path('logout/', appLogout.as_view(next_page = 'login'), name='logout'),
    path('register/', appRegister.as_view(), name= 'register'),
    path("", planner.as_view(), name='planner'),
    #tasks
    path('create_task', createTask.as_view(), name='create_task'),
    path("taskdetails/<int:pk>/", task_detail.as_view(), name = 'task_detail'),
    path("updatetask/<int:pk>/", updateTask.as_view(), name= 'update_task'), 
    path("deletetask/<int:pk>/", deleteTask.as_view(), name='delete_task'),
    #journal entries
    path('create_entry', createEntry.as_view(), name='create_entry'),
    path("entrydetails/<int:pk>/", entry_detail.as_view(), name = 'entry_detail'),
    path("updateentry/<int:pk>/", updateEntry.as_view(), name= 'update_entry'), 
    path("deleteentry/<int:pk>/", deleteEntry.as_view(), name='delete_entry')

]

