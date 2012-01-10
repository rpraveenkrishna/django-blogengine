from django.db import models
from django.contrib.admin.models import User
from autoslug import AutoSlugField
from tinymce import models as tinymce_models

class BlogCategory(models.Model):
    name = models.CharField(max_length = 100)
    slug = AutoSlugField(populate_from = 'name')
    created_on = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(User, null = True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/blog/category/" + self.slug

    class Meta:
        verbose_name_plural = "Blog Categories"


class BlogEntry(models.Model):
    title = models.CharField(max_length = 200)
    slug = AutoSlugField(populate_from = 'title', null = True)
    text = tinymce_models.HTMLField()
    category = models.ForeignKey(BlogCategory)
    created_on = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(User, null = True)
    
    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/entry/" + self.slug

    class Meta:
        verbose_name_plural = "Blog Entries"

        
        