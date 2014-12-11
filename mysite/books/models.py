from django.db import models
from time import time

def get_upload_file_name(instance,filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'),filename)


# Create your models here.
  
class Article(models.Model):
    thumbnail = models.FileField(upload_to=get_upload_file_name)
    title = models.CharField(max_length=120)
    body = models.TextField()
    pub_date = models.DateTimeField('date published(YYYY-MM-DD)')
    likes = models.IntegerField(default=0)
    #unlikes = models.IntegerField( blank=True,null=True)
    def __unicode__(self):
        return self.title
    
    
#class Comment(models.Model):
   # body = models.TextField()
   # pub_date = models.DateTimeField('date published')
   # article = models.ForeignKey(Article)
    #blank=True,null=True
    
    
    
