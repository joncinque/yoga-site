
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import register_setting

from django.conf import settings


register_setting(
    name="GOOGLE_RECAPTCHA_KEY",
    label=_("Google reCAPTCHA key"),
    description=_("Site ID key to use for form validation, preventing spam bots"),
    editable=True,
    default=settings.GOOGLE_RECAPTCHA_KEY,
)

register_setting(
    name="SOCIAL_LINK_FACEBOOK",
    label=_("Facebook link"),
    description=_("If present a Facebook icon linking here will be in the header."),
    editable=True,
    default="https://facebook.com/mezzatheme",
)

register_setting(
    name="SOCIAL_LINK_TWITTER",
    label=_("Twitter link"),
    description=_("If present a Twitter icon linking here will be in the header."),
    editable=True,
    default="https://twitter.com/mezzatheme",
)

register_setting(
    name="SOCIAL_LINK_INSTAGRAM",
    label=_("Instagram link"),
    description=_("If present an Instagram icon linking here will be in the header."),
    editable=True,
    default="https://instagram.com/joncyoga",
)

register_setting(
    name="SOCIAL_LINK_GOOGLE",
    label=_("Google Plus link"),
    description=_("If present a Google Plus icon linking here will be in the header."),
    editable=True,
    default="https://plus.google.com/b/118069550927850290401/118069550927850290401/",
)

register_setting(
    name="SOCIAL_LINK_LINKEDIN",
    label=_("LinkedIn link"),
    description=_("If present a LinkedIn icon linking here will be in the header."),
    editable=True,
    default="",
)

register_setting(
    name="SOCIAL_LINK_PINTEREST",
    label=_("Pinterest link"),
    description=_("If present a Pinterest icon linking here will be in the header."),
    editable=True,
    default="",
)

register_setting(
    name="SOCIAL_LINK_DRIBBBLE",
    label=_("Dribbble link"),
    description=_("If present a Dribbble icon linking here will be in the footer."),
    editable=True,
    default="http://dribbble.com/joshcartme",
)

register_setting(
    name="SOCIAL_PHONE",
    label=_("Phone"),
    description=_("If present this phone number will show in the header."),
    editable=True,
    default="123-456-7890",
)

register_setting(
    name="SOCIAL_EMAIL",
    label=_("Email"),
    description=_("If present this email address will show in the header."),
    editable=True,
    default="contact@mezzathe.me",
)

register_setting(
    name="INSTAGRAM_USER",
    label=_("Instagram user"),
    description=_("If present the last few posts from the user will be shown in the footer."),
    editable=True,
    default="joncyoga",
)

register_setting(
    name="INSTAGRAM_POSTS",
    label=_("Instagram posts"),
    description=_("If INSTAGRAM_USER is present, decides how many old posts will show in the footer."),
    editable=True,
    default="5",
)

RIGHT = 'RI'
LEFT = 'LE'
SIDEBAR_ALIGNMENTS = (
    (LEFT, _('Left')),
    (RIGHT, _('Right')),
)

register_setting(
    name="THEME_SIDEBAR_ALIGNMENT",
    label="Sidebar alignment",
    description=_("For pages that have a sidebar, determines if it is on the "
                  "left or right"),
    editable=True,
    choices=SIDEBAR_ALIGNMENTS,
    default=RIGHT
)

ONE = 1
TWO = 2
BLOG_LAYOUTS = (
    (ONE, _('One')),
    (TWO, _('Two')),
)

register_setting(
    name="THEME_BLOG_LIST_LAYOUT",
    label="Blog list layout",
    description=_("Determines how many blog posts are shown per row in the "
                  "blog list view"),
    editable=True,
    choices=BLOG_LAYOUTS,
    default=TWO
)

register_setting(
    name="THEME_COLOR_SCHEME",
    label="Color scheme",
    description=_("Use the cog icon in the front end to try out color "
                  "schemes. Enter the number of the chosen color scheme here "
                  "to make it permanent."),
    editable=True,
    default="1",
)

register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    append=True,
    default=("SOCIAL_LINK_FACEBOOK",
             "SOCIAL_LINK_INSTAGRAM",
             "SOCIAL_LINK_TWITTER",
             "SOCIAL_LINK_GOOGLE",
             "SOCIAL_LINK_LINKEDIN",
             "SOCIAL_LINK_PINTEREST",
             "SOCIAL_LINK_DRIBBBLE",
             "SOCIAL_PHONE",
             "SOCIAL_EMAIL",
             "INSTAGRAM_USER",
             "THEME_SIDEBAR_ALIGNMENT",
             "THEME_BLOG_LIST_LAYOUT",
             "THEME_COLOR_SCHEME",
             "GOOGLE_RECAPTCHA_KEY"),
)
