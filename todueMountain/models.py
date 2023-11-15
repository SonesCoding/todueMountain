from django.db import models
from django.contrib.auth.models import User
import calendar
#User is a table I can have django make for me
#documentation:
#https://docs.djangoproject.com/en/4.2/topics/auth/default/

SUN ="Sunday"
MON  = "Monday"
TUE = "Tuesday"
WED = "Wednesday"
THUR = "Thursday"
FRI = "Friday"
SAT = "Satuday"
dotwChoices = [(SUN,"Sunday"),
               (MON,"Monday"),
               (TUE,"Tuesday"),
               (WED,"Wednesday"),
               (THUR,"Thursday"),
               (FRI,"Friday"),
               (SAT,"Saturday")]


#model for individual tasks; a list of tasks is exclusive to a day
#days will be presented by the week with a toggle to move forwards or backwards in the month
#maybe will have a toggle to choose what month you want to toggle through weeks idk
#somethin like that
class tdTask(models.Model):
    user = models.ForeignKey(
            User, on_delete=models.CASCADE, 
            null=True, blank=True,) #I will allow "null" (empty) tasks because that might be an user's odd preogative, but it is theirs
    
    TaskTitle = models.CharField(max_length=200)
    TaskDescr = models.TextField(null=True, blank=True)
    #subtask = models.???
    checked = models.BooleanField(default=False) #if the task were completed and checked, the value would become true
    createdOn = models.DateField(auto_now_add=True) # will document time it is pub removing a field from the form and less work on user
    Taskdotf = models.CharField(max_length=9,choices=dotwChoices, null=False)
    def __str__(self) -> str:
        return self.TaskTitle
    
        class Meta:
            orderedby = ['checked'] 
        #completed tasks will (hopefully) be listed at the bottom of the list
        

#model for journal entries which can be multiple in a day

class journalEntry(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        null = True, blank = True   #MUST change only true for development
    )
    EntryTitle = models.CharField(max_length=200)
    mood = models.CharField(max_length=300)
    entryText = models.TextField(null = True, blank = True)
    enteredOn = models.DateTimeField(auto_now_add=True, null=False)
    Entrydotf = models.CharField(max_length=9, choices=dotwChoices)

    def __str__(self) -> str:
        return self.EntryTitle

    
