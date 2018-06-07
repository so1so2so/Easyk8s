#__author:  zhangneng
#date:  2018/6/7
from django import template
from django.core.exceptions import FieldDoesNotExist
from django.utils.safestring import mark_safe
from django.utils.timezone import datetime,timedelta
register = template.Library()

@register.simple_tag
def get_labels(metadata_obj):
    return metadata_obj._labels