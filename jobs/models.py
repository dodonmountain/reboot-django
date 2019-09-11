from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=30)
    job = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.job}'