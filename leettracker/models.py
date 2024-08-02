from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass


class LeetCodeProblem(models.Model):
    DIFFICULTY_CHOICES = [
        ('E', 'Easy'),
        ('M', 'Medium'),
        ('H', 'Hard'),
    ]

    problem_name = models.CharField(max_length=255)
    problem_number = models.IntegerField()
    solution = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    topic = models.CharField(max_length=100)
    time_complexity = models.CharField(max_length=100, blank=True, null=True)
    space_complexity = models.CharField(max_length=100, blank=True, null=True)
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY_CHOICES)
    problem_link = models.URLField(max_length=200, default='https://default.url')
    status = models.BooleanField()

    def __str__(self):
        return f"{self.problem_number}: {self.problem_name}"