from django.db import models
from django.utils.timezone import now, timedelta

def default_due_date():
    return now().date() + timedelta(days=2)

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    added_on = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(default=default_due_date, null=True, blank=True)

    def __str__(self):
        return self.title
