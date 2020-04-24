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

text = "Period 1 All subjects will receive a single dose of BCT197 14 mg (2 x 7mg capsules) in a fasting state. Period 2 All subjects will receive 3 daily doses of azithromycin 500 mg film coated tablet and a single dose of BCT197 14 mg (2 x 7mg capsules) (24 hours after the first dose of azithromycin) ina fasting state."
get_location(text, "azithromycin 500 mg film coated tablet and a single dose of BCT197 14 mg")
