# -*- coding: utf-8 -*-

from __future__ import unicode_literals # python 2/3 support

from collections import namedtuple

ParameterTuple = namedtuple('ParameterTuple', [
    'key',
    'values',
    'default_value',
])

SelectorTuple = namedtuple('SelectorTuple', [
    'key',
    'value',
])

RestrictionTuple = namedtuple('RestrictionTuple', [
    'when',
    'set',
])

BuildParametersTuple = namedtuple('BuildParametersTuple', [
    'all_parameters',
    'project_restrictions',
    'ci_parameters',
    'ios_parameters',
    'android_parameters',
])

ParametersSetTuple = namedtuple('ParametersSetTuple', [
    'active_parameters',
])