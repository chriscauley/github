from django.http import HttpResponseRedirect
from django.contrib import messages
from django.template.response import TemplateResponse

from github.forms import RepositoryForm
from github.models import Repository

import json

def home(request):
  form = RepositoryForm(request.POST or None)
  if form.is_valid():
    repo = form.save()
    messages.success(request,"{} saved".format(repo))
    return HttpResponseRedirect('.')
  fields = ("username","reponame","stars","watchers","forks")
  values = {
    'form': form,
    'repositories': json.dumps(list(Repository.objects.all().values(*fields))),
  }
  return TemplateResponse(request,"index.html",values)

def direct_to_template(request,template,context={}):
  return TemplateResponse(request,template,context)

redirect = lambda request,url: HttpResponseRedirect(url)
