from django.shortcuts import render, redirect
from django.views import View
from .models import Subject, Grade, TempSelection
from .forms import SubjectSelectionForm

class IndexView(View):
    def get(self,request):
        return render(request, 'eduapp/home.html')
    #success_url='/Welcome'
class SubjectSelectionView(View):
    def get(self, request):
        subjects = Subject.objects.filter(is_active=True)
        grades = Grade.objects.all()
        form = SubjectSelectionForm(subjects=subjects, grades=grades)
        return render(request, 'eduapp/form.html', {
            'form': form,
            'subjects': subjects,
            'grades': grades
        })

    def post(self, request):
        subjects = Subject.objects.filter(is_active=True)
        grades = Grade.objects.all()
        form = SubjectSelectionForm(request.POST, subjects=subjects, grades=grades)

        if form.is_valid():
            session_key = request.session.session_key
            TempSelection.objects.filter(session_key=session_key).delete()

            # Save selected subjects and grades
            for subject_id, grade_id in form.cleaned_data['selected_subjects']:
                TempSelection.objects.create(
                    session_key=session_key,
                    subject_id=subject_id,
                    grade_id=grade_id
                )
            return redirect('result_view')

        return render(request, 'eduapp/form.html', {
            'form': form,
            'subjects': subjects,
            'grades': grades
        })
        # Process selected subjects and grades

class ResultsView(View):
    def get(self, request):
        # Get the session key for the current user
        session_key = request.session.session_key
        
        # Fetch the selected subjects and grades for this session
        selections = TempSelection.objects.filter(session_key=session_key)
        
        # Prepare data for the results page
        results = []
        for selection in selections:
            results.append({
                'subject': selection.subject.name,
                'grade': selection.grade.grade
            })
        
        # Render the results template
        return render(request, 'eduapp/results.html', {
            'results': results
        })
"""
class RecommendedViews(View):
    def get(request):
        courses=Courses.objects.all()
        return render(request,'eduapp/courses.htnl')

#
def processing_view(request):
    session_key = request.session.session_key
    selections = TempSelection.objects.filter(session_key=session_key)
    
    # Add your cluster algorithm logic here
    # For now, we'll just pass the selections
    return render(request, "eduapp/results.html", {
        'selections': selections
    })
"""