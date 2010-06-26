from django import template

register = template.Library()


@register.simple_tag
def required_field(field):
    if field.field.required:
        return '<span class="required">*</span>'
    else:
        return ''
