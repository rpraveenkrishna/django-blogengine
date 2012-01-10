from django.db import models

class UserInfo(models.Model):
    website_name = models.CharField(500)
    website_url = models.URLField()
    hit_count = models.BigIntegerField()
    
    def __unicode__(self):
        return self.website_name
