from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'),)
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
    


PROFESSIONAL_CHOICES = (('Psychologist', 'Psychologist'), ('Psychiatrist', 'Psychiatrist'), ('Therapist', 'Therapist'), ('Counsellor', 'Counsellor'), ('Clinical Social Worker', 'Clinical Social Worker'),)    
GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'),)
QUALIFICATION_CHOICES = (('M.D.', 'M.D.'), ('Psy.D', 'Psy.D'), ('PhD', 'PhD'), ('MSc in Counseling Psychology', 'MSc in Counseling Psychology'), ('MSc in Clinical Social Work', 'MSc in Clinical Social Work'),)    
class Professional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    pro_type = models.CharField(max_length=30, choices=PROFESSIONAL_CHOICES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    edu_type = models.CharField(max_length=30, choices=QUALIFICATION_CHOICES)
    license = models.CharField(max_length=100)
    nid_passport = models.CharField(max_length=100)


    def __str__(self):
        return self.first_name





# GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others'),)
# class Appointment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     full_name = models.CharField(max_length=100)
#     gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
#     age = models.IntegerField()
#     contact = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     appointment_Date = models.DateField(default=datetime.now, blank=True) 
#     symptoms = models.TextField(blank=True)
#     status = models.BooleanField(default=False)
    
#     def __str__(self):
#         return self.full_name
