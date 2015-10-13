from django import forms
from django.contrib import messages
from .models import Repository, GITHUB_QS

import requests

def test(repo):
  url = 'https://api.github.com/repos/{}'.format(repo)
  url += GITHUB_QS
  request = requests.head(url)
  try:
    request.raise_for_status()
  except Exception,e:
    e = str(e).replace(GITHUB_QS,'?SECRET_KEYS')
    raise forms.ValidationError(e)

class RepositoryForm(forms.Form):
  repo_1 = forms.CharField(max_length=128)
  repo_2 = forms.CharField(max_length=128)
  def clean(self,*args,**kwargs):
    cleaned_data = super(RepositoryForm,self).clean(*args,**kwargs)
    if 'repo_1' in cleaned_data:
      test(cleaned_data['repo_1'])
    if 'repo_2' in cleaned_data:
      test(cleaned_data['repo_2'])
    return cleaned_data
  def save(self,request):
    # not a traditional save method, takes in request for messages
    cleaned_data = self.cleaned_data
    repos = [cleaned_data['repo_1'],cleaned_data['repo_2']]
    out = []
    for repo_string in repos:
      username,reponame = repo_string.split('/')
      repo,new = Repository.objects.get_or_create(username=username,reponame=reponame)
      out.append(repo)
      if new:
        messages.success(request,"{} saved".format(repo))
    return out
