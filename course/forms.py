from django import forms
from .models import Course, Lecture


class CourseForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'require-field'
    # describing other parts of the actual model form class
    class Meta:
        # declare model
        model = Course
        fields = ['name', 'desc',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_data = {
                "placeholder": f'Course {str(field)}',
                "class": 'form-control'
            }
            self.fields[str(field)].widget.attrs.update(**new_data)
        # self.fields['name'].widget.attrs.update({'class': 'form-control'})
        # self.fields['desc'].widget.attrs.update({'rows': 2})


class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['lname', 'program',
                  'sprites', 'plan', 'ppt',
                  'knowledge', 'game']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['knowledge'].widget.attrs.update({'rows': 2})