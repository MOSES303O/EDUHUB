from django import forms
from django.core.exceptions import ValidationError

class SubjectSelectionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.subjects = kwargs.pop('subjects', [])
        self.grades = kwargs.pop('grades', [])
        super().__init__(*args, **kwargs)

        # Dynamically create fields for each subject
        for subject in self.subjects:
            self.fields[f'subject_{subject.id}'] = forms.BooleanField(
                required=False,
                label=subject.name
            )
            self.fields[f'grade_{subject.id}'] = forms.ChoiceField(
                choices=[(grade.id, grade.grade) for grade in self.grades],
                label='Select Grade',
                required=False
            )

    def clean(self):
        cleaned_data = super().clean()
        selected_subjects = []
        errors = []

        # Validate selected subjects and grades
        for subject in self.subjects:
            subj_key = f'subject_{subject.id}'
            grade_key = f'grade_{subject.id}'

            if cleaned_data.get(subj_key):
                grade = cleaned_data.get(grade_key)
                if not grade:
                    errors.append(ValidationError(f"Select a grade for {subject.name}"))
                else:
                    selected_subjects.append((subject.id, grade))

        # Validate subject count
        if len(selected_subjects) < 7 or len(selected_subjects) > 9:
            errors.append(ValidationError("Select 7-9 subjects"))

        if errors:
            raise ValidationError(errors)

        cleaned_data['selected_subjects'] = selected_subjects
        return cleaned_data