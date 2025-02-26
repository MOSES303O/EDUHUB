import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

class Subject(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Subjects'

class Grade(models.Model):
    # Define a regex pattern for the allowed grade values
    GRADE_REGEX = r'^(A|A-|B\+|B|B-|C\+|C|C-|D\+|D|D-|E)$'
    
    grade = models.CharField(
        max_length=2,  # Adjust the max_length to fit the longest grade ('A-', 'B+')
        validators=[
            RegexValidator(
                regex=GRADE_REGEX,
                message='Grade must be one of the following: A, A-, B+, B, B-, C+, C, C-, D+, D, D-, E'
            )
        ]
    )
    
    points = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(12)
        ]
    )

    def __str__(self):
        return f"{self.grade} ({self.points} points)"
    
    class Meta:
        ordering = ['-points']

class TempSelection(models.Model):
    session_key = models.CharField(max_length=40)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
class UniversityList(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    detail = models.TextField()
    image_url = models.URLField(max_length=500)
    class Meta:
        ordering=['name']
        verbose_name_plural="universities"
class CourseDetail(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    university_established=models.PositiveIntegerField(default=0)
    details=models.TextField(default='tttt')
    class Meta:
        ordering=['name']
"""
class Courses(models.Model):
    id = models.UUIDField(editable=False,default=uuid.uuid4, primary_key=True)
    universityList=models.ForeignKey(UniversityList,on_delete=models.CASCADE,related_name='course')
    name = models.CharField(max_length=200)
    coursecode=models.PositiveIntegerField(default=0,unique=True)
    details=models.OneToOneField(CourseDetail,on_delete=models.SET_NULL,null=True,blank=True)
    class Meta:
        ordering=['name']    
        unique_together=('universityList','name')

class CourseRequirement(models.Model):
    course=models.ForeignKey(Courses,on_delete=models.CASCADE)
    subjects=models.TextField()
    cluster_wights21=models.DecimalField(max_digits=5,decimal_places=3)
    cluster_wights22=models.DecimalField(max_digits=5,decimal_places=3)
    #details=models.TextField(default='tttt') 

"""   