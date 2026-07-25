from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from problems.models import Problem,Solution

# Create your views here.

def register(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        user_type = request.POST.get("user_type")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, "accounts/register.html")

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, "accounts/register.html")

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, "accounts/register.html")

        CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            user_type=user_type
        )

        messages.success(request, "Registration successful. Please login.")
        return redirect("login")

    return render(request, "accounts/register.html")

def login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            auth_login(request, user)

            if user.user_type == "student":
                return redirect("student_dashboard")

            elif user.user_type == "company":
                return redirect("company_dashboard")

        else:

            messages.error(
                request,
                "Invalid username or password."
            )

            return render(
                request,
                "accounts/login.html"
            )

    return render(
        request,
        "accounts/login.html"
    )


@login_required(login_url="login")
def student_dashboard(request):

    if request.user.user_type != "student":
        return redirect("company_dashboard")

    total_problems = Problem.objects.filter(status="open").count()

    submitted_count = Solution.objects.filter(
        student=request.user
    ).count()

    accepted_count = Solution.objects.filter(
        student=request.user,
        status="accepted"
    ).count()

    recent_problems = Problem.objects.filter(
        status="open"
    ).order_by("-created_at")[:5]

    context = {
        "student": request.user,
        "total_problems": total_problems,
        "submitted_count": submitted_count,
        "accepted_count": accepted_count,
        "recent_problems": recent_problems,
    }

    return render(
        request,
        "accounts/student_dashboard.html",
        context
    )

@login_required(login_url="login")
def company_dashboard(request):

    # Company check
    if request.user.user_type != "company":
        return redirect("student_dashboard")

    # Statistics
    total_problems = Problem.objects.filter(
        company=request.user
    ).count()

    open_problems = Problem.objects.filter(
        company=request.user,
        status="open"
    ).count()

    closed_problems = Problem.objects.filter(
        company=request.user,
        status="close"
    ).count()

    total_submissions = Solution.objects.filter(
        problem__company=request.user
    ).count()

    # Recent Problems
    recent_problems = Problem.objects.filter(
        company=request.user
    ).order_by("-created_at")[:5]

    # Context
    context = {
        "company": request.user,
        "total_problems": total_problems,
        "open_problems": open_problems,
        "closed_problems": closed_problems,
        "total_submissions": total_submissions,
        "recent_problems": recent_problems,
    }

    return render(
        request,
        "accounts/company_dashboard.html",
        context
    )

def logout(request):
    auth_logout(request)
    return redirect("login")