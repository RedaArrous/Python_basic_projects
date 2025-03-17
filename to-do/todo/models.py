from django.db import models

# Create your models here.


class Task(models.Model):
    task_name = models.CharField(max_length=80)
    category = models.CharField(max_length=30, null= True)
    importancy = models.CharField(max_length=12)
    date_added = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.task_name
