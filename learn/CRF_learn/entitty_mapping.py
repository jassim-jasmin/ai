import re

mg_values = 'mg_values'
combination = 'combination'

"""prediction label mapping"""
logic_mapping = {
    "mark_3_na": "nalaxone_format_1",
    "mark_4": "arm_part_discover"
}

"""data identification"""
arm_attribute_rule = {
    "(\d+)\s+in\s+dose": (1, "combination", "search"),
    "([\d/.]+\s*mg)": (0, mg_values, "findall")
}

arm_part_rule = {
    "\\d+\\s*mg\\s+in\\s+dose\\s\\(\\s*\\w+\\s+\\d+\\.\\d+\\s+ml\\s+spray\\s+of\\sa\\s+\\d+\\s*mg\\s*/\\s*ml\\s+solution\\s+in\\s+\\w+\\s+nostril\\s*\\)": "nalaxone_specifict_1"
}

nalaxone_arm_part_rule = {
    "mg_part": "\\d+ mg",
    "first_part": "\d+\s*mg\s*/\s*ml",
    "second_part": "\w+\s+\d+\.\d+\s+ml"
}

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


def nalaxone_format_1(data, protocol_values):
    print("nalaxone format 1")
    print(data)
    # nalaxone_arm_spec_rule(data[])

    for each_prediction in data:
        nalaxone_arm_spec_rule(each_prediction, protocol_values)

def nalaxone_specifict_1(data, pattern, protocol_values):
    nalaxone_arm_part = []
    arm_part = dict()

    if "arm_part" in protocol_values:
        arm_part = protocol_values["arm_part"]

        if "nalaxone_arm_part" in arm_part:
            nalaxone_arm_part = arm_part["nalaxone_arm_part"]

    search_arm_part = re.findall(pattern, data, re.IGNORECASE)

    if search_arm_part:
        arm_part_array = []

        for each_search_parm_part in search_arm_part:
            arm_part_dic = dict()

            for key, pattern in nalaxone_arm_part_rule.items():
                search_object = re.search(pattern, each_search_parm_part, re.IGNORECASE)

                if search_object:
                    if key == "first_part":
                        arm_part_dic[key] = "(" + search_object.group(0)
                    elif key == "second_part":
                        arm_part_dic[key] = search_object.group(0) + ")"
                    else:
                        arm_part_dic[key] = search_object.group(0)

                else:
                    print("ERROR! nalaxone_specifict_1 has pattern missmatch", pattern, "data:", each_search_parm_part)

            arm_part_array.append(arm_part_dic)


        nalaxone_arm_part.append(arm_part_array)
        arm_part["nalaxone_arm_part"] = nalaxone_arm_part
        protocol_values["arm_part"] = arm_part

def arm_part_discover(data, protocol_values):
    print("arm_part_discover")
    print(data)

    for each_data in data:
        for pattern, function_name in arm_part_rule.items():
            pattern_match = re.search(pattern, each_data, re.IGNORECASE)

            if pattern_match:
                eval(function_name)(each_data, pattern, protocol_values)

def join_arm(specifier_itrator, each_element, speicifier, arm):
    if specifier_itrator:
        if each_element == speicifier[specifier_itrator]["mg_part"]:
            first_part = ''
            second_part = ''

            if "first_part" in speicifier[specifier_itrator]:
                first_part = speicifier[specifier_itrator]["first_part"]

            if "second_part" in speicifier[specifier_itrator]["second_part"]:
                second_part = ', ' + speicifier[specifier_itrator]["second_part"]

            arm += f" {each_element} {first_part}{second_part}"

        specifier_itrator += 1

    else:
        arm += f" {each_element}"

def get_arm_part(specifier_itrator, each_element, speicifier):
    if specifier_itrator:
        try:
            mg_values, first_part, second_part = speicifier[specifier_itrator-1]

            if mg_values == each_element:
                return first_part+', '+second_part
            else:
                print('minor irror nneed fix')
                return ''

        except Exception as e:
            return False

    return ''

def arm_design(data, armcd):
    armcd_length = len(armcd)
    speicifier = []
    arm_values = []

    if "arm" in data:
        arm_values = data["arm"]

    if "arm_part" in data:
        arm_part = data["arm_part"]

        for specifier_class, specifier_array in arm_part.items():
            if len(specifier_array) > 1:
                print("multiple prediction in", specifier_class, "need validation")

            for each_arm_prediction in specifier_array:
                for each_arm in each_arm_prediction:
                    mg_part = ''
                    first_part = ''
                    second_part = ''

                    if "mg_part" in each_arm:
                        mg_part = each_arm["mg_part"]

                    if "first_part" in each_arm:
                        first_part = each_arm["first_part"]

                    if "second_part" in each_arm:
                        second_part = each_arm["second_part"]

                    speicifier.append((mg_part, first_part, second_part))


    if mg_values in data:
        prediction_result = data[mg_values]

        for each_possible_values in data[mg_values]:
            # real_value = validation(each_possible_values, "arm_design")
            real_values = each_possible_values

            if len(real_values) <= armcd_length:
                arm = ''
                i = 0

                if len(speicifier) == 0:
                    specifier_itrator = False
                else:
                    specifier_itrator = 1

                for each_element in real_values:
                    if len(armcd) > i:
                        if armcd[i].isalpha(): # problem
                            arm += f"{each_element} {get_arm_part(specifier_itrator, each_element, speicifier)}"

                            specifier_itrator += 1
                            i += 1

                        else:
                            while not armcd[i].isalpha():
                                arm += f" {armcd[i]} "
                                i += 1

                            arm += f"{each_element} {get_arm_part(specifier_itrator, each_element, speicifier)}"
                            specifier_itrator += 1
                            i += 1

                    else:
                        arm = ''
                        print("armcd violation, armcd:", armcd, "values:", real_values)

                        break

                if arm != '':
                    arm_values.append(arm)
            else:
                print("no match")

    data["arm"] = arm_values

def arm_attribute(data):
    print("arm input: ", data)
    protocol_values = {}

    for key, mapping in logic_mapping.items():
        if key in data:
            eval(mapping)(data[key], protocol_values)

    arm_design(protocol_values, 'A-B-C-D-E')

    print("final result", protocol_values)