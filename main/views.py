from django.contrib import messages
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse

from github.forms import RepositoryForm
from github.models import Repository

import json

def home(request):
  form = RepositoryForm(request.GET or None)
  repos = []
  if form.is_valid():
    repos  = form.save(request)
  fields = ("username","reponame","stars","watchers","forks")
  values = {
    'form': form,
    'repositories': json.dumps(list(Repository.objects.all().values(*fields))),
    'current_repos': repos,
  }
  return TemplateResponse(request,"index.html",values)

def update_all(request):
  for repository in Repository.objects.all():
    repository.update()
    repository.save()
  messages.success(request,"Updated %s repos"%Repository.objects.count())
  return HttpResponseRedirect(request.GET['next']+"?"+request.GET['qs'])

def direct_to_template(request,template,context={}):
  return TemplateResponse(request,template,context)

redirect = lambda request,url: HttpResponseRedirect(url)
