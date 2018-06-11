#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from django import template
from django.core.exceptions import FieldDoesNotExist
from django.utils.safestring import mark_safe
from django.utils.timezone import datetime, timedelta

register = template.Library()


@register.simple_tag
def get_labels(metadata_obj):
    return metadata_obj._labels


@register.simple_tag
def get_people_time(time_obj):
    if time_obj:
        return time_obj.strftime('%Y-%m-%d %H:%M:%S');
    else:
        return None


@register.simple_tag
def get_image_warehouse(image_obj):
    try:
        if image_obj[1].find("/") != -1:
            return image_obj[1].rsplit("/", maxsplit=1)[0]
        # return image_obj[0].split("@")[0]
        else:
            return "官方仓库"
    except:
        return "无仓库"


@register.simple_tag
def get_image_name(image_obj):
    try:
        return image_obj[1]
    except:
        return image_obj[0].split("@")[0]


@register.simple_tag
def get_image_sha256(image_obj):
    try:
        return image_obj[0].split("sha256:")[1]
    except:
        return image_obj[0].split("@")[0]


@register.simple_tag
def get_image_size_mb(image_obj_size_bytes):
    if image_obj_size_bytes < 0:
        raise ValueError("!!! number_of_bytes can't be smaller than 0 !!!")

    step_to_greater_unit = 1024.

    number_of_bytes = float(image_obj_size_bytes)
    unit = 'bytes'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'KB'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'MB'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'GB'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'TB'

    precision = 1
    number_of_bytes = round(number_of_bytes, precision)

    return str(number_of_bytes) + ' ' + unit
