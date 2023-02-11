from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField

import xml.etree.ElementTree
import re
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=300,null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default='/images/OIP.jpeg', null=True, blank=True)
    content = RichTextField()
    category = models.ForeignKey(Category,null=True,blank=True, on_delete=models.SET_NULL)
    slug = models.SlugField(blank=True, null=True)
    snippest = models.CharField(max_length=100,null=True, blank=True)
    published_now = models.BooleanField(default=False)
    like = models.ManyToManyField(User, related_name='likes', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True,verbose_name='Date Created')
    last_edited = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_created']


    def save(self, *args, **kwargs): 
        CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});') 

        def cleanhtml(raw_html):
            cleantext = re.sub(CLEANR, '', raw_html)
            return cleantext
            
        if self.slug is None:
            self.slug = slugify(self.title)
        else:
            self.slug = slugify(self.title)
        snippest = cleanhtml(self.content)[:100]
        self.snippest = snippest[:100]
        return super().save(*args, **kwargs)
        

    def __str__(self):        
        return self.author.username