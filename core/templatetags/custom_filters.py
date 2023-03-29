from django import template
import datetime

register = template.Library()

@register.filter(name='calculate_age')
def calculate_age(dob):
    today = datetime.date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

# from datetime import date
# from django import template

# register = template.Library()

# @register.filter
# def calculate_age(dob):
#     today = date.today()
#     age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
#     return age
