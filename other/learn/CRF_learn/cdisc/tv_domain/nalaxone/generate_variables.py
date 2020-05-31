import re

def variable_VISIT(data):
    row_count = -1
    visit_array = []
    visitdy_array = []

    for each_element in data:
        row_count += 1
        number = None

        if each_element.isalnum():
            # print(each_element, "is number")
            number = each_element

        elif each_element[0] == '-': # start with - is considering a number part :todo: if exception need to change logic
            # print("negative", each_element)
            number = each_element

        if number:
            if row_count == 1:
                visit_array.append(f"SCREENING {number}")
                visitdy_array.append(28) #:todo: the logic is wrong need to replace SCREENNIG  visitdy

            else:
                visit_array.append(f"DAY {number}")
                visitdy_array.append(number)

        elif row_count != 0 and row_count != len(data)-1:
            visitdy_array.append(0)
            visit_array.append(0)

        if row_count == len(data)-1:
            to_digit_obj = re.search('to +(\d+)', each_element)
            if to_digit_obj:
                to_digit = to_digit_obj.group(1)
                visitdy_array.append(int(visitdy_array[len(visitdy_array)-1]) + int(to_digit)) # adding (+3 to 5 days) => 5 is adding

        """
        Follow up is comming at last need revise the logic
        """

    if visit_array:
        visit_array.append("FOLLOW-UP")

    return visit_array, visitdy_array

def variable_TVSTRL():
    pass

def find_variables(data):
    tv_variable = {}
    visit_array, visitdy_array = variable_VISIT(data)
    tv_variable['VISIT'] = visit_array
    tv_variable['VISITDY'] = visitdy_array

    return tv_variable