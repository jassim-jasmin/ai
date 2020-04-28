import re

nalaxone_arm_part_name = "op0927_arm_part"
first_part_name = "first_part"
second_part_name = "second_part"
mg_part_name = "mg_part"
arm_part_name = "arm_part"
mg_values = "mg_values"

op0927_arm_part_rule = {
    "(\\d+\\s*mg)\\s+(gw\\S+)": (1, mg_part_name, "search"),
    "(gw\\S+)": (1, first_part_name, "search")
}

def search_rule(data, rule):
    if rule == mg_values:

        return [data]

    return data

def op0927(value_array, protocol_values):
    print("op0927", value_array)
    mg_values_array = []
    protocol_values_data = []
    arm_part_data = {}
    protocol_values_data_main = []

    if arm_part_name in protocol_values:
        arm_part_data = protocol_values[arm_part_name]

        if "op0927" in arm_part_data:
            protocol_values_data_main = arm_part_data["op0927"]

    if mg_values in protocol_values:
        mg_values_array = protocol_values[mg_values]

    for each_value in value_array:
        rule = {}
        for expression, group_value in op0927_arm_part_rule.items():
            option = group_value[2]

            if arm_part_name in protocol_values:
                temp_data = protocol_values[arm_part_name]

                # if group_value[1] in temp_data:
                #     protocol_values_data =  temp_data[group_value[1]]

            if option == "search":
                search_object = re.search(expression, each_value, re.IGNORECASE)

                if search_object:
                    if mg_part_name != group_value[1]:
                        rule[group_value[1]] = search_rule(search_object.group(group_value[0]), group_value[1])
                        # rule = {group_value[1]: search_rule(search_object.group(group_value[0]), group_value[1])}
                    else:
                        mg_values_array.append(search_rule(search_object.group(group_value[0]), mg_values))
                        rule[mg_part_name] = search_rule(search_object.group(group_value[0]), group_value[1])
                        # rule = {mg_values: search_rule(search_object.group(group_value[0]), group_value[1])}

            elif option == "findall":
                search_object = re.findall(expression, each_value, re.IGNORECASE)
                # print("findall", search_object)

                if search_object:
                    if mg_part_name != group_value[1]:
                        # rule = {first_part_name: search_object}
                        rule[group_value[1]] = search_object
                    else:
                        rule[mg_part_name] = search_object
                        mg_values_array.append(search_object)

        protocol_values_data.append(dict(rule))

    protocol_values_data_main.append(protocol_values_data)

    if mg_values_array:
        protocol_values[mg_values] = mg_values_array

    if protocol_values_data_main:
        arm_part_data["op0927"] = protocol_values_data_main
        protocol_values[arm_part_name] = arm_part_data