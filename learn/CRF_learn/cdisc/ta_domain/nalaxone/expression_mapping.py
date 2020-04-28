from learn.CRF_learn.cdisc.ta_domain.default_variable_name import *
from learn.CRF_learn.cdisc.ta_domain.nalaxone.arm_match import arm_match_selector_1
import re

"""data identification"""
arm_attribute_rule = {
    "(\d+)\s+in\s+dose": (1, "combination", "search"),
    "([\d/.]+\s*mg)": (0, mg_values, "findall")
}

arm_part_rule = {
    "\\d+\\s*mg\\s+in\\s+dose\\s\\(\\s*\\w+\\s+\\d+\\.\\d+\\s+ml\\s+spray\\s+of\\sa\\s+\\d+\\s*mg\\s*/\\s*ml\\s+solution\\s+in\\s+\\w+\\s+nostril\\s*\\)": "arm_match_selector_1"
}
