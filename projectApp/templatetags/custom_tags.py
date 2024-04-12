from django import template
from projectApp.models import imageuser

register = template.Library()


@register.simple_tag
def get_image_user(user):
  try:
    return imageuser.objects.get(relation=user)
  except imageuser.DoesNotExist:
    return None
