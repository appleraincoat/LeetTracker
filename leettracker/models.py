from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass


class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str_(self):
        return self.name

class LeetCodeProblem(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    problem_name = models.CharField(max_length=255)
    problem_number = models.IntegerField()
    solution = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    topics = models.ManyToManyField(Topic, blank=True)
    time_complexity = models.CharField(max_length=100, blank=True, null=True)
    space_complexity = models.CharField(max_length=100, blank=True, null=True)
    difficulty = models.CharField(max_length=6, choices=DIFFICULTY_CHOICES)
    problem_link = models.URLField()
    status = models.BooleanField()

    def __str__(self):
        return self.problem_name