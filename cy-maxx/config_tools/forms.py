from django import forms
from .models import ProjectInfo

class ProjectInfoForm(forms.ModelForm):
    class Meta:
        model = ProjectInfo
        fields = ['app_name', 'github_link', 'remark']