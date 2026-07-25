from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Problem,Solution
from django.contrib import messages
from django.shortcuts import get_object_or_404 
# Create your views here.

@login_required(login_url="login")
def create_problem(request):

    if request.user.user_type != "company":
        return redirect("student_dashboard")

    if request.method == "POST":

        title = request.POST.get("title")
        if title == "":
            messages.error(request, "Title is required")
            return render(request, "problems/create_problem.html")
        description = request.POST.get("description")
        category = request.POST.get("category")
        difficulty = request.POST.get("difficulty")
        reward = request.POST.get("reward")
        deadline = request.POST.get("deadline")
        required_skills = request.POST.get("required_skills")
        problem_image = request.FILES.get("problem_image")

        problem = Problem(
            company=request.user,
            title=title,
            description=description,
            category=category,
            difficulty=difficulty,
            reward=reward,
            deadline=deadline,
            required_skills=required_skills,
            problem_image=problem_image,
        )

        problem.save()

        messages.success(request, "Problem Created Successfully")

        return redirect("company_dashboard")

    return render(request, "problems/create_problem.html")


@login_required(login_url="login")
def my_problems(request):

    if request.user.user_type != "company":
        return redirect("student_dashboard")

    problems = Problem.objects.filter(company=request.user).order_by("-created_at")

    context = {"problems": problems}

    return render(request,"problems/my_problems.html",context)


@login_required(login_url="login")
def edit_problem(request, id):

    if request.user.user_type != "company":
        return redirect("student_dashboard")

    problem = get_object_or_404(Problem,id=id,
                                company=request.user)

    if request.method == "POST":
        problem.title = request.POST.get("title")
        problem.description = request.POST.get("description")
        problem.category = request.POST.get("category")
        problem.difficulty = request.POST.get("difficulty")
        problem.reward = request.POST.get("reward")
        problem.deadline = request.POST.get("deadline")
        problem.required_skills = request.POST.get("required_skills")
        if request.FILES.get("problem_image"):
            problem.problem_image = request.FILES.get("problem_image")
        problem.save()
        messages.success(request,"Problem Updated Successfully")
        return redirect("my_problems")
    context = {
        "problem": problem
    }
    return render(request,
                  "problems/edit_problem.html",context)


@login_required(login_url="login")
def delete_problem(request, id):

    if request.user.user_type != "company":
        return redirect("student_dashboard")

    problem = get_object_or_404(Problem,id=id,
                                company=request.user)
    problem.delete()
    messages.success(request,"Problem Deleted Successfully.")
    return redirect("my_problems")


@login_required(login_url="login")
def all_problems(request):

    if request.user.user_type=='company': 
        return redirect("company_dashboard")

    problems = Problem.objects.filter(status='open').order_by("-created_at") 
    context = {"problems": problems}
    return render(request,"problems/problem_list.html",context)

@login_required(login_url="login")
def problem_detail(request, id):

    # Student
    if request.user.user_type == "student":

        problem = get_object_or_404(
            Problem,
            id=id,
            status="open"
        )

    # Company
    elif request.user.user_type == "company":

        problem = get_object_or_404(
            Problem,
            id=id,
            company=request.user
        )

    else:

        return redirect("login")

    context = {

        "problem": problem

    }

    return render(
        request,
        "problems/problem_detail.html",
        context
    )

@login_required(login_url="login")
def submit_solution(request, id):

    # Only students can submit solutions
    if request.user.user_type != "student":
        return redirect("company_dashboard")

    # Get only open problem
    problem = get_object_or_404(Problem,id=id,status="open")

    if request.method == "POST":

        # Get form data
        solution_text = request.POST.get("solution_text")
        github_url = request.POST.get("github_url")
        demo_url = request.POST.get("demo_url")

        # Get uploaded file
        solution_file = request.FILES.get("solution_file")

        # Generate submission number
        submission_number = (
            Solution.objects.filter(
                student=request.user,
                problem=problem).count() + 1)
        
        # Validation
        if (not solution_text.strip() and not github_url.strip()
            and not demo_url.strip() and not solution_file):
            messages.error(request,"Please provide at least one solution.")
            return redirect("submit_solution", id=problem.id)
        
        # Save solution
        Solution.objects.create(student=request.user,
                                problem=problem,
                                submission_number=submission_number,
                                solution_text=solution_text,
                                github_url=github_url,
                                solution_file=solution_file,
                                demo_url=demo_url
                                # status = "pendin" # No need because default="pending"
        )
        messages.success(request,"Solution submitted successfully.")

        return redirect("problem_detail",id=problem.id)
    context = {"problem": problem}

    return render(request,
                  "problems/submit_solution.html",context)


@login_required(login_url="login")
def my_submissions(request):

    # Only students
    if request.user.user_type != "student":
        return redirect("company_dashboard")

    submissions = Solution.objects.filter(student=request.user)

    context = {"submissions": submissions}
    return render(request,
                  "problems/my_submissions.html",context)


@login_required(login_url="login")
def submission_detail(request, id):

    if request.user.user_type != "student":
        return redirect("company_dashboard")

    submission = get_object_or_404(
        Solution,
        id=id,
        student=request.user
    )

    context = {
        "submission": submission
    }
    return render(
        request,
        "problems/submission_detail.html",
        context
    )

@login_required(login_url="login")
def company_submissions(request, id):

    # Company check
    if request.user.user_type != 'company':
        return redirect("student_dashboard")
    # Problem get
    problem = get_object_or_404(Problem,id=id,company = request.user)

    # Submissions get
    submissions = Solution.objects.filter(problem=problem)

    # Context
    context = {
        "problem": problem,
        "submissions":submissions}

    # Render
    return render(request,
                  "problems/company_submissions.html",context)


@login_required(login_url="login")
def company_submission_detail(request, id):

    # company check
    if request.user.user_type != "company":
            return redirect("student_dashboard")
    
    # submission get
    submission = get_object_or_404(
            Solution,
            id=id,
            problem__company=request.user
        )

    if request.method == "POST":

        # status
        status = request.POST.get("status")
        if status in ["accepted","rejected","reviewing"]:
            submission.status = status
        # feedback
        submission.feedback = request.POST.get("feedback")
        # score
        score = request.POST.get("score")
        if score:
            submission.score = score

        # save
        submission.save()
        # success message
        messages.success(request,"Submission reviewed successfully.")
        # redirect
        return redirect("company_submissions",id=submission.problem.id)

    context = {

        "submission": submission

    }

    return render(
        request,
        "problems/company_submission_detail.html",
        context
    )