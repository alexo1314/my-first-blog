from django import template
register = template.Library()

@register.simple_tag
def define(val=None):
  #if(val=="5"):
  #  return "middle"
  print("==============================================\n")
  print(val)
  print("==============================================\n\n\n\n\n\n\n\n\n\n")
  return val
