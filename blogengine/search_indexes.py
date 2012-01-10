from haystack.indexes import *
from haystack import site
from models import BlogEntry
import datetime

class BlogEntryIndex(SearchIndex):
    text = CharField(document = True, use_template = True)
    author = CharField(model_attr = 'created_by')
    pub_date = DateTimeField(model_attr = 'created_on')
    
    def index_queryset(self):
        return BlogEntry.objects.filter(created_on__lte=datetime.datetime.now())
        
        
site.register(BlogEntry, BlogEntryIndex)
