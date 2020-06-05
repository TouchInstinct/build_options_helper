# -*- coding: utf-8 -*-

from __future__ import unicode_literals # python 2/3 support

from .raw_models import *

class Parameter(ParameterTuple):
    @staticmethod
    def from_dict(dict_obj):
        return Parameter(
            key=dict_obj["key"],
            values=dict_obj["values"],
            default_value=dict_obj.get("default_value")
        )

class Selector(SelectorTuple):
    @staticmethod
    def from_dict(dict_obj):
        return Selector(**dict_obj)

class Restriction(RestrictionTuple):
    @staticmethod
    def from_dict(dict_obj):
        return Restriction(
            when=list(map(Selector.from_dict, dict_obj["when"])),
            set=list(map(Parameter.from_dict, dict_obj["set"])),
        )

    def is_active_for_any_selector(self, selectors):
        for selector in selectors:
            if selector in self.when:
                return True

        return False

class BuildParameters(BuildParametersTuple):
    @staticmethod
    def from_dict(dict_obj):
        return BuildParameters(
            all_parameters=list(map(Parameter.from_dict, dict_obj["all_parameters"])),
            project_restrictions=list(map(Restriction.from_dict, dict_obj["project_restrictions"])),
            ci_parameters=list(map(Parameter.from_dict, dict_obj["ci_parameters"])),
            ios_parameters=list(map(Parameter.from_dict, dict_obj["ios_parameters"])),
            android_parameters=list(map(Parameter.from_dict, dict_obj["android_parameters"]))
        )

class ParametersSet(ParametersSetTuple):
    def filter_using_restrictions_and_selectors(self, restrictions, selectors):
        active_restrictions = filter(lambda r: r.is_active_for_any_selector(active_selectors), restrictions)

        parameters_from_restrictions = [parameter for restriction in active_restrictions for parameter in restriction.set]

        parameters_to_keep = self.__difference_for_parameters(parameters_from_restrictions)

        return ParametersSet(active_parameters=parameters_from_restrictions + parameters_to_keep)

    def update_parameters(self, parameters):
        parameters_to_keep = self.__difference_for_parameters(parameters)

        return ParametersSet(active_parameters=parameters_to_keep + parameters)

    def __difference_for_parameters(self, parameters):
        parameters_keys = list(map(lambda p: p.key, parameters))

        return list(filter(lambda p: p.key not in parameters_keys, self.active_parameters))

