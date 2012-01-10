from django.template import Library, Node, TemplateSyntaxError
from django.db.models import get_model
from django.contrib.sites.models import Site
from settings import SITE_ID

register = Library()


class LatestContentNode(Node):
    def __init__(self, model, num, varname):
        self.num, self.varname = num, varname
        self.model = get_model(*model.split('.'))

    def render(self, context):
        context[self.varname] = self.model._default_manager.all()[:self.num]
        return ''


def get_latest(parser, token):
    bits = token.contents.split()
    if len(bits) != 5:
        raise TemplateSyntaxError,\
        "get_latest tag takes exactly four arguments"
    if bits[3] != 'as':
        raise TemplateSyntaxError,\
        "third argument to get_latest tag must be 'as'"
    return LatestContentNode(bits[1], bits[2], bits[4])


class SiteNameNode(Node):
    def __init__(self, varname):
        self.varname = varname

    def render(self, context):
        context[self.varname] = Site.objects.get_current().name
        return ''


def get_site_name(parser, token):
    bits = token.contents.split()
    if len(bits) != 3:
        raise TemplateSyntaxError,\
        "get_site_name tag takes exactly two arguments (" + str(len(bits)) +\
        " given )"
    if bits[1] != 'as':
        raise TemplateSyntaxError,\
        "first argument to get_site_name tag must be 'as'"
    return SiteNameNode(bits[2])


get_latest = register.tag(get_latest)
get_site_name = register.tag(get_site_name)
