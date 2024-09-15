
from django import forms

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)

    def clean_query(self):
        query = self.cleaned_data['query']
        # Add any additional input validation/sanitization here
        return query
    