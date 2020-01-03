from django import forms
from ..models.school import School


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = [
            'school_name',
            'school_abbr',
            'region',
            'province',
            'color_primary',
            'color_secondary',
            'color_primary_alternate',
            'color_secondary_alternate',
            'president',
        ]
