from django import template
register = template.Library()

@register.simple_tag
def define(val=None):
  #if(val=="5"):
  #  return "middle"
  print("==============================================\n")
  print(val)
  print("==============================================\n\n\n\n\n\n\n\n\n\n")
<<<<<<< HEAD
  return val
=======
  return val
>>>>>>> e5e84542e58e5d10423a34cacdc76d411df6bb4d
