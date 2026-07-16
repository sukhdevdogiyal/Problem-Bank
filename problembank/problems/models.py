from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Problem(models.Model):
    DIFFICULTY_CHOICES = (
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    )
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("open", "Open"),
        ("closed", "Closed"),
    )
    company = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to={"user_type": "company"}
    )

    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    category = models.CharField(max_length=150)

    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES
    )

    reward = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    deadline = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="draft"
    )

    problem_image = models.ImageField(
        upload_to="problem_images/",
        blank=True,
        null=True
    )

    required_skills = models.CharField(
        max_length=500,
        blank=True,
        help_text="Separate multiple skills with commas."
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Solution(models.Model):

    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("reviewing", "Reviewing"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
    )

    student = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to={"user_type": "student"},
        related_name="solutions"
    )

    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE,
        related_name="solutions"
    )

    submission_number = models.IntegerField()

    solution_text = models.TextField(
        max_length=1000,
        blank=True
    )

    github_url = models.URLField(blank=True)

    solution_file = models.FileField(
        upload_to="solutions/",
        blank=True,
        null=True
    )

    demo_url = models.URLField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    feedback = models.TextField(
        max_length=500,
        blank=True
    )

    score = models.IntegerField(
        blank=True,
        null=True
    )

    submitted_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.username} - {self.problem.title}"