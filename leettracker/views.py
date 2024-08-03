from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django import forms

from .models import User, LeetCodeProblem

# Create your views here.

def index(request):
    return render(request, "leettracker/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "leettracker/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "leettracker/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "leettracker/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "leettracker/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "leettracker/register.html")
    
class LeetCodeProblemForm(forms.Form):
    problem_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter Problem Name',
            'class': 'form-control'
        })
    )
    problem_number = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter Problem Number',
            'class': 'form-control'
        })
    )
    solution = forms.CharField(
        required=False,  # Make optional
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter Solution (optional)',
            'class': 'form-control'
        })
    )
    notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter Notes (optional)',
            'class': 'form-control'
        })
    )
    topic = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter Topic',
            'class': 'form-control'
        })
    )
    time_complexity = forms.CharField(
        required=False,  # Make optional
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter Time Complexity (optional)',
            'class': 'form-control'
        })
    )
    space_complexity = forms.CharField(
        required=False,  # Make optional
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter Space Complexity (optional)',
            'class': 'form-control'
        })
    )
    difficulty = forms.ChoiceField(
        choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')],
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    problem_link = forms.URLField(
        required=False,  # Make optional
        max_length=200,
        widget=forms.URLInput(attrs={
            'placeholder': 'Enter Problem Link (optional)',
            'class': 'form-control'
        })
    )
    status = forms.BooleanField(
        required=False,
        label="Problem Solved",
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )

def newentry(request):
    if request.method == "POST":
        form = LeetCodeProblemForm(request.POST)
        if form.is_valid():            
            new_problem = LeetCodeProblem(
                problem_name=form.cleaned_data['problem_name'],
                problem_number=form.cleaned_data['problem_number'],
                solution=form.cleaned_data.get('solution', ''),
                notes=form.cleaned_data.get('notes', ''),
                topic=form.cleaned_data['topic'],
                time_complexity=form.cleaned_data.get('time_complexity', ''),
                space_complexity=form.cleaned_data.get('space_complexity', ''),
                difficulty=form.cleaned_data['difficulty'],
                problem_link=form.cleaned_data['problem_link'],
                status=form.cleaned_data['status']
            )
            new_problem.save()
            return redirect('myproblems')  # Redirect to the listing page after saving
        else:
            print("Form is invalid. Errors:", form.errors)
            return render(request, 'leettracker/newentry.html', {'form': form})
    else:
        form = LeetCodeProblemForm()
        return render(request, 'leettracker/newentry.html', {'form': form})

def myproblems(request):
    # Fetch all problem instances from the database
    problems = LeetCodeProblem.objects.all()
    return render(request, 'leettracker/myproblems.html', {'problems': problems})

def displayproblem(request, problem_id):
    problem = get_object_or_404(LeetCodeProblem, pk=problem_id)
    return render(request, 'leettracker/displayproblem.html', {'problem': problem})

def topics(request):
    # Fetch distinct topics and order them alphabetically
    topics = LeetCodeProblem.objects.values_list('topic', flat=True).distinct().order_by('topic')
    return render(request, 'leettracker/topics.html', {'topics': topics})