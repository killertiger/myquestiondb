from django import template

register = template.Library()

@register.filter()
def int_to_str(value):
    return chr(96 + value)