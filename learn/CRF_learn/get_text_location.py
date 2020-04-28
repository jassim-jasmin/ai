import re

def replace(search_text):
    search_text = search_text.replace(")", "X")
    search_text = search_text.replace(".", "X")
    search_text = search_text.replace("+", "X")
    search_text = search_text.replace("(", "X")
    search_text = search_text.replace("!", "X")
    search_text = search_text.replace("$", "X")
    search_text = search_text.replace("^", "X")
    search_text = search_text.replace("&", "X")
    search_text = search_text.replace("*", "X")
    search_text = search_text.replace("-", "X")
    search_text = search_text.replace("[", "X")
    search_text = search_text.replace("]", "X")
    search_text = search_text.replace("{", "X")
    search_text = search_text.replace("}", "X")
    search_text = search_text.replace("`", "X")
    search_text = search_text.replace("\\", "X")

    return search_text

def get_location(text, search_text):

    text = replace(text)
    search_text = replace(search_text)
    data = re.search(search_text, text)
    print(data.span())
    (l, r) = data.span()
    # print(text[l:r]+':::')

    return l, r

text = "In Part B, the absolute bioavailability of CBD will be determined by comparing an appropriate IV dose of GWP42003-P with a single oral dose of 1500 mg GWP42003-P. The IV dose will be selected based on the safety and tolerability of doses administered in Part A. In addition, the PK of CBD/THC in Part A will be taken into consideration and the lowest dose commensurate with adequate plasma levels of CBD/THC will be selected. Dependent on the PK data from each cohort in Part A, Part B may be performed in parallel with Part A."
get_location(text, "1500 mg GWP42003-P")
