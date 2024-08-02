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
    path('topics', views.topics, name='topics'),
]