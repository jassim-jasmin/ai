# from learn.CRF_learn.cdisc.ta_domain.nalaxone.default_variable_name import *

import re

nalaxone_arm_part_name = "nalaxone_arm_part"
first_part_name = "first_part"
second_part_name = "second_part"
mg_part_name = "mg_part"
arm_part_name = "arm_part"

nalaxone_arm_part_rule = {
    mg_part_name: "\\d+ mg",
    first_part_name: "\d+\s*mg\s*/\s*ml",
    second_part_name: "\w+\s+\d+\.\d+\s+ml"
}

def arm_match_selector_1(data, pattern, protocol_values):
    nalaxone_arm_part = []
    arm_part = dict()

    if arm_part_name in protocol_values:
        arm_part = protocol_values[arm_part_name]

        if nalaxone_arm_part_name in arm_part:
            nalaxone_arm_part = arm_part[nalaxone_arm_part_name]

    search_arm_part = re.findall(pattern, data, re.IGNORECASE)

    if search_arm_part:
        arm_part_array = []

        for each_search_parm_part in search_arm_part:
            arm_part_dic = dict()

            for key, pattern in nalaxone_arm_part_rule.items():
                search_object = re.search(pattern, each_search_parm_part, re.IGNORECASE)

                if search_object:
                    if key == first_part_name:
                        arm_part_dic[key] = "(" + search_object.group(0)

                    elif key == second_part_name:
                        arm_part_dic[key] = search_object.group(0) + ")"

                    else:
                        arm_part_dic[key] = search_object.group(0)

                else:
                    print("ERROR! nalaxone_specifict_1 has pattern missmatch", pattern, "data:", each_search_parm_part)

            arm_part_array.append(arm_part_dic)


        nalaxone_arm_part.append(arm_part_array)
        arm_part[nalaxone_arm_part_name] = nalaxone_arm_part
        protocol_values[arm_part_name] = arm_part
