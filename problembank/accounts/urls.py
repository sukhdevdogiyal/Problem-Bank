from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout/', views.logout, name="logout"),
    path('student-dashboard/',views.student_dashboard,name="student_dashboard"),
    path("company-dashboard/",views.company_dashboard,name="company_dashboard"),

]