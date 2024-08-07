from django import template
from datetime import timezone

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

@register.simple_tag(takes_context=True)
def query_string(context, **kwargs):
    request = context["request"]
    updated = request.GET.copy()
    
    for key, value in kwargs.items():
        updated[key] = value

    return updated.urlencode()
  
@register.filter
def to_int(value):
  if not isinstance(value, timezone.datetime):
    return False
  
  now = timezone
  return value.date() == now.date()