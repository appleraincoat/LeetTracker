from django.contrib import admin
from .models import User, LeetCodeProblem, Topic

# Register your models here.
admin.site.register(User)
admin.site.register(Topic)
admin.site.register(LeetCodeProblem)