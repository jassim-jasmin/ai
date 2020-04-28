from learn.CRF_learn.cdisc.ta_domain.default_variable_name import *

"""data identification"""
arm_attribute_rule = {
    "(\\d+)\\s+in\\s+dose": (1, combination, "search"),
    "([\\d/.]+\\s*mg)": (0, mg_values, "findall")
}

arm_part_rule_divided = {
    "(\\d+\\s*mg\\s+gw\\S+)": (1, arm_part, "search", "op0927")
}