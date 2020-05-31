from other.learn.CRF_learn.cdisc.ta_domain.nalaxone.nalaxon_specific import *
from other.learn.CRF_learn.cdisc.ta_domain.expression_mapping import *

"""prediction label mapping
call from arm.py
key: label value
item: function name (the argument should be, data, protocol_values"""
label_mapping = {
    "mark_3_na": "mg_portion_selector",
    "mark_4": "arm_part_discover",
    "part_2": "arm_part_2"
}


def update_protocol_value(data, protocol_values, expression, group_value, update_prediction_result=False):
    """Updating the matching sequence in protocol value document"""
    option = group_value[2] # search/findall
    protocol_values_data = []
    protocol_values_all_data = {}
    # print("options", option)

    if group_value[1] in protocol_values:
        protocol_values_all_data = protocol_values[group_value[1]]

        if "prediction" in protocol_values_all_data:
            protocol_values_data = protocol_values_all_data["prediction"]

    if option == "search":
        search_object = re.search(expression, data, re.IGNORECASE)

        if search_object:
            rule = search_rule(search_object.group(group_value[0]), group_value[1])

            if rule not in protocol_values_data:
                protocol_values_data.append(rule)

    elif option == "findall":
        search_object = re.findall(expression, data, re.IGNORECASE)
        # print("findall", search_object)

        if search_object:
            if search_object not in protocol_values_data:
                protocol_values_data.append(search_object)

    if protocol_values_data and update_prediction_result:
        if protocol_values_all_data:
            protocol_values_all_data["prediction"] = protocol_values_data

        else:
            protocol_values_all_data = {"prediction": protocol_values_data}

        protocol_values[group_value[1]] = protocol_values_all_data

    return protocol_values_data



def arm_part_2(data, protocol_values):
    """
    For conforming the predicted format
    """
    # update_protocol_value(data, protocol_values, arm_part_rule)

    duplicate_data = []

    for each_data in data:
        if each_data not in duplicate_data:
            duplicate_data.append(each_data)

            for expression, group_value in arm_part_rule_divided.items():
                update_value = update_protocol_value(each_data, protocol_values, expression, group_value)
                if update_value:
                    eval(group_value[3])(update_value, protocol_values)

def mg_portion_selector(data, protocol_values):
    # print("mg_portion_selector")
    # print(data)
    # nalaxone_arm_spec_rule(data[])

    for each_prediction in data:
        nalaxone_arm_spec_rule(each_prediction, protocol_values)

def arm_part_discover(data, protocol_values):
    # print("arm_part_discover")
    # print(data)

    for each_data in data:
        for pattern, function_name in arm_part_rule.items():
            pattern_match = re.search(pattern, each_data, re.IGNORECASE)

            if pattern_match:
                eval(function_name)(each_data, pattern, protocol_values)