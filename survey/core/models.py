from django.db import models

# Create your modelslass Student(models.Model):
class Survey(models.Model):
    name=models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    feedback = models.TextField()
    challenges = models.TextField()
    improvements = models.TextField()
    comments = models.TextField()

    def __str__(self):
        return self.name
