from django import forms
from .models import Repository, GITHUB_QS

import requests

class RepositoryForm(forms.ModelForm):
  def clean(self,*args,**kwargs):
    cleaned_data = super(RepositoryForm,self).clean(*args,**kwargs)
    url = 'https://api.github.com/repos/{username}/{reponame}'.format(**cleaned_data)
    url += GITHUB_QS
    request = requests.head(url)
    try:
      request.raise_for_status()
    except Exception,e:
      raise forms.ValidationError(e)
    return cleaned_data
  class Meta:
    model = Repository
    fields = ('username','reponame')
