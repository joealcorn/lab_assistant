import os
import json

from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

from lab_assistant.contrib.django.encoding import LaboratoryJSONEncoder


register = template.Library()


def render_as_str(value):
    return str(value)


def render_to_json(value):
    return json.dumps(value, indent=4, sort_keys=True)


@register.simple_tag
def render_value(value):
    renderer = {
        bool: render_to_json,
        dict: render_to_json,
        list: render_to_json,
        tuple: render_to_json,
        type(None): render_to_json,
    }.get(type(value), render_as_str)
    return renderer(value)


@register.simple_tag
def render_observation(observation):
    return mark_safe(json.dumps({
        'context': observation.context,
        'value': observation.value,
    }, cls=LaboratoryJSONEncoder))
