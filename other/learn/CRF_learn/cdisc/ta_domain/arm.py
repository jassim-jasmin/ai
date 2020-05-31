from other.learn.CRF_learn.cdisc.ta_domain.prediction_label_mapping import *
# from learn.CRF_learn.cdisc.ta_domain.default_variable_name import *

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

                    if (mg_part, first_part, second_part) not in speicifier:
                        speicifier.append((mg_part, first_part, second_part))


    if mg_values in data:
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
                        if armcd[i].isalpha():
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

                if len(armcd)>i: # If armcd not match  with predicted mg_valuse, then it should not be added
                    arm = ''

                if arm != '':
                    arm_values.append(arm)

            else:
                print("no match")

    if arm_values:
        data["arm"] = arm_values

def generate_arm(data, armcd):
    # print("arm input: ", data)
    protocol_values = {}

    for key, mapping in label_mapping.items():
        if key in data:
            eval(mapping)(data[key], protocol_values) # label_mapping has defined functions, if matching the key here
            # the function call happens and values are stored in protocol_values

    arm_design(protocol_values, armcd)
    # print("final result", protocol_values)

    return protocol_values