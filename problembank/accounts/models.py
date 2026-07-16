from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('student', 'Student'),
        ('company', 'Company'),
    )

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPES,
        default='student'
    )

class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    college_name = models.CharField(max_length=150)
    location = models.CharField(max_length=100)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    skills = models.CharField(max_length=255,help_text="Separate multiple skills with commas.")
    bio = models.TextField(max_length=500,blank=True)
    resume = models.FileField(upload_to='resumes/',blank=True,null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
class CompanyProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150,unique=True)
    company_logo = models.ImageField(upload_to='company_logos/',blank=True,null=True)

    website = models.URLField(blank=True)

    industry = models.CharField(max_length=150)

    location = models.CharField(max_length=150)

    description = models.TextField(max_length=500,blank=True)

    verification_document = models.FileField(upload_to='verification_documents/')

    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
