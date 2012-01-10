from django.db import models


class Subscriber(models.Model):
    email = models.EmailField()
    status = models.BooleanField(default=True)
    
    def __unicode__(self):
        return u'%s' % self.email
        
