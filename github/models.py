from django.conf import settings
from django.db import models

import requests,json

GITHUB_QS = "?client_id={}&client_secret={}".format(settings.GITHUB_KEY,settings.GITHUB_SECRET)

class Repository(models.Model):
  username = models.CharField(max_length=64)
  reponame = models.CharField(max_length=64)
  stars = models.IntegerField(default=0)
  watchers = models.IntegerField(default=0)
  forks = models.IntegerField(default=0)
  __unicode__ = lambda self: "%s/%s"%(self.username,self.reponame)
  def update(self):
    url = 'https://api.github.com/repos/{}'.format(unicode(self))
    url += GITHUB_QS
    request = requests.get(url)
    data = json.loads(request.text)
    self.stars = data['stargazers_count']
    self.watchers = data['watchers_count']
    self.forks = data['forks']
  def save(self,*args,**kwargs):
    if not self.pk:
      self.update()
    super(Repository,self).save(*args,**kwargs)
  class Meta:
    unique_together = ('username','reponame')
