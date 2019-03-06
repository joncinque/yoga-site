from django.template import Variable, Node
from django.conf import settings

from mezzanine import template
from mezzanine.utils.sites import current_site_id

from theme.models import SiteConfiguration

from django_instagram.scraper import instagram_profile_obj
from django_instagram.templatetags.instagram_client import get_profile_media

register = template.Library()


@register.filter
def can_view_help(user):
    if settings.DEBUG or user.has_site_permission:
        return True
    return False


@register.as_tag
def get_site_conf():
    """
    Adds the `SiteConfiguration` to the context
    """
    return SiteConfiguration.objects.get_or_create(site_id=current_site_id())[0]


class InstagramUserRecentMediaNode(Node):
    def __init__(self, username):
        self.username = Variable(username)

    def render(self, context):
        actual_username = self.username.resolve(context)
        profile = instagram_profile_obj(username=actual_username)

        if profile:
            context['profile'] = profile
            context['recent_media'] = get_profile_media(profile)

        return ''


@register.tag
def instagram_user_recent_media_variable(parser, token):
    try:
        tagname, username = token.split_contents()
        return InstagramUserRecentMediaNode(username)
    except ValueError:
        raise template.TemplateSyntaxError('tag requires a single argument')
