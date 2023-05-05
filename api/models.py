from django.db import models
import uuid


class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    # use Django's built-in hashing
    password = models.CharField(max_length=128)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    university_name = models.CharField(max_length=255)
    degree_name = models.CharField(max_length=255)
    graduation_year = models.IntegerField()
    major = models.CharField(max_length=255)
    gpa = models.DecimalField(max_digits=4, decimal_places=2)
    skills = models.TextField()
    profile_picture_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Employer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    # use Django's built-in hashing
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    website_url = models.URLField(null=True, blank=True)
    logo_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class JobPosting(models.Model):
    JOB_TYPE_CHOICES = (
        ('FT', 'Full-time'),
        ('PT', 'Part-time'),
        ('IN', 'Internship'),
        ('CO', 'Contract'),
    )

    id = models.AutoField(primary_key=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=2, choices=JOB_TYPE_CHOICES)
    required_skills = models.TextField()
    application_deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Collaboration(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(Student, related_name='collaborations')
    description = models.TextField()
    created_by = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='created_collaborations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Notification(models.Model):
    NOTIFICATION_TYPE_CHOICES = (
        ('AP', 'Application'),
        ('IN', 'Invitation'),
        ('CO', 'Collaboration'),
        ('OT', 'Other'),
    )

    id = models.AutoField(primary_key=True)
    recipient = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    type = models.CharField(max_length=2, choices=NOTIFICATION_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

import uuid
from django.db import models

# ... other models ...

class Internship(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    internship_type_choices = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('remote', 'Remote'),
    ]
    internship_type = models.CharField(max_length=20, choices=internship_type_choices)
    
    season_choices = [
        ('summer', 'Summer'),
        ('winter', 'Winter'),
    ]
    season = models.CharField(max_length=20, choices=season_choices)
    
    payment_status_choices = [
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
    ]
    payment_status = models.CharField(max_length=20, choices=payment_status_choices)
    
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.IntegerField(help_text="Duration in weeks")
    required_skills = models.TextField()
    responsibilities = models.TextField()
    application_deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
