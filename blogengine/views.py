from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.sites.models import Site
from datetime import datetime
from django.views.decorators.gzip import gzip_page
from models import BlogEntry, BlogCategory
from haystack.query import SearchQuerySet



###############################################
###Homepage, Shows the top 1 entry in there
###############################################
@gzip_page
def home(request):
    html_template = 'blogengine/index.htm'
    blog_entries = BlogEntry.objects.all().order_by("-created_on")[:1]
    return render_to_response(html_template,
    {
        'blog_entries':         blog_entries,
        
    }, context_instance=RequestContext(request,))


###############################################
###Shows the search result
###############################################
@gzip_page
def search(request):
    search_term = None
    if request.method == 'GET':
        search_term = request.GET.get('q')
        results = SearchQuerySet().filter(content = search_term)
    html_template = 'blogengine/index.htm'
    return render_to_response(html_template,
    {
        'results': results,
        'search_term': search_term,
        
    }, context_instance=RequestContext(request,))


###############################################
###Shows the blog entry by slug
###############################################
@gzip_page
def blog_entry_by_slug(request, slug_field):
    html_template = 'blogengine/index.htm'
    blog_entry = BlogEntry.objects.filter(slug = slug_field)[0]
    return render_to_response(html_template,
    {
        'blog_entry': blog_entry,
        
    }, context_instance=RequestContext(request,))



###############################################
###Shows the category by slug
###############################################
@gzip_page
def category_by_slug(request, slug_field):
    html_template = 'blogengine/index.htm'
    blog_category = BlogCategory.objects.filter(slug = slug_field)
    blog_entries = BlogEntry.objects.filter(category = blog_category)
    return render_to_response(html_template,
    {
        'blog_entries': blog_entries,
        
    }, context_instance=RequestContext(request,))
