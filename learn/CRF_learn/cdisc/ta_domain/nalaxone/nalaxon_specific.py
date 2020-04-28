from learn.CRF_learn.cdisc.ta_domain.nalaxone.expression_mapping import *

import re

def search_rule(data, rule):

    return data

def nalaxone_arm_spec_rule(data, protocol_values):
    """
    For conforming the predicted format
    """
    for expression, group_value in arm_attribute_rule.items():
        option = group_value[2]
        # print("options", option)

        if group_value[1] in protocol_values:
            protocol_values_data = protocol_values[group_value[1]]

        else:
            protocol_values_data = []

        if option == "search":
            search_object = re.search(expression, data, re.IGNORECASE)

            if search_object:
                rule = search_rule(search_object.group(group_value[0]), group_value[1])
                protocol_values_data.append(rule)

        elif option == "findall":
            search_object = re.findall(expression, data, re.IGNORECASE)
            # print("findall", search_object)

            if search_object:
                protocol_values_data.append(search_object)

        if protocol_values_data:
            protocol_values[group_value[1]] = protocol_values_data