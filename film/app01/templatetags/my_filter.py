from django import template

register = template.Library()

#Reference: https://docs.djangoproject.com/en/4.2/howto/custom-template-tags/
@register.filter
def is_user_digg(film, request):
    if str(request.user) == 'AnonymousUser':
        return ''
    if film in request.user.digg_film.all():
        return 'active'
    return ''


@register.filter
def is_not_user_digg(film, request):
    if str(request.user) == 'AnonymousUser':
        return 'active'
    if film in request.user.digg_film.all():
        return ''
    return 'active'


