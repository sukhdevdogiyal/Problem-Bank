from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_problem, name="create_problem"),
    path("my-problems/",views.my_problems,name="my_problems"),
    path("edit/<int:id>/",views.edit_problem,name="edit_problem"),
    path("delete/<int:id>/",views.delete_problem,name="delete_problem"),
    path("all/",views.all_problems,name="all_problems"),
    path("detail/<int:id>/",views.problem_detail,name="problem_detail"),
    path("submit-solution/<int:id>/",views.submit_solution,name="submit_solution"),
    path("my-submissions/", views.my_submissions, name="my_submissions"),
    path("submission/<int:id>/", views.submission_detail, name="submission_detail"),
    path("submissions/<int:id>/", views.company_submissions, name="company_submissions"),
    path("submission-review/<int:id>/",views.company_submission_detail,name="company_submission_detail"),
    
]