#coding: utf-8

from django import template
import ttag


register = template.Library()


@register.filter
def split(str, char):
    return str.split(char)
