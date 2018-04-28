from django import template

register = template.Library()

URL_PREFIX = '/media/'


@register.filter
def default_avatar(string):
    if not string:
        string = 'users_avatars/gravatar.png'

    new_string = f'{URL_PREFIX}{string}'
    return new_string
