from django import forms
from .models import Review


class WriteReview(forms.ModelForm):
    """WriteReview form to allow users to create their
    own reviews.
    """
    class Meta:
        model = Review
        fields = ('title', 'comments',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'comments': 'Write your review here',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:

            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].label = False
