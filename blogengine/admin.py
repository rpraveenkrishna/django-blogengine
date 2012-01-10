from models import BlogEntry, BlogCategory
from django.contrib import admin
from forms import BlogEntryModelForm


class BlogCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_by', 'created_on', 'slug', )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.save()


class BlogEntryAdmin(admin.ModelAdmin):
    form = BlogEntryModelForm
    list_display = ('title', 'created_on')
    readonly_fields = ('created_by', 'created_on', 'slug', )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.save()

    class Media: 
        js = ('/media/js/jquery.min14.js',) 

admin.site.register(BlogEntry, BlogEntryAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
