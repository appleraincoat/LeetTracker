from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newentry", views.newentry, name="newentry"),
    path("myproblems", views.myproblems, name='myproblems'),
    path('problems/<int:problem_id>/', views.displayproblem, name='displayproblem'),
    path('selectbytopic', views.selectbytopic, name='selectbytopic'),
    path('selectbytopic/<int:topic_id>/', views.problemsbytopic, name='problemsbytopic'),
    path('problems/<int:problem_id>/delete/', views.deleteproblem, name='deleteproblem'),
    path('problems/<int:problem_id>/edit/', views.editproblem, name='editproblem'),
    path('random_problem', views.random_problem, name='random_problem'),
]