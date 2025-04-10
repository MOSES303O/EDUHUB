from django.contrib import admin
from .models import Subject, Grade, TempSelection,UniversityList,CourseDetail,Course

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_editable = ('is_active',)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('grade', 'points')

admin.site.register(TempSelection)
@admin.register(UniversityList)
class UniversityAdmin(admin.ModelAdmin):
    list_display=('name','detail','image_url')
    search_fields=('name','detail')
    #ordering='name'
    #  """
  
@admin.register(Course)
class CoursesAdmin(admin.ModelAdmin):
    list_display=('coursecode','name','university','coursecode')
    search_fields=('name','university','coursecode')
    #ordering=('name')

"""
@admin.register(CourseRequirement)
class courserequirements(admin.ModelAdmin):
    list_display=('course','subjects','cluster_wights21','cluster_wights22')
    search_fields=('course','sujects')
"""

@admin.register(CourseDetail)
class SchoolAdmin(admin.ModelAdmin):
    list_display=('name','university_established')
    search_fields=('id','name')
    #ordering=('name')
