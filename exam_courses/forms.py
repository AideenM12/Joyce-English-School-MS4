from django import forms
from .models import ExamCourse


class ExamCourseForm(forms.ModelForm):

    class Meta:
        model = ExamCourse
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
     
       
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'