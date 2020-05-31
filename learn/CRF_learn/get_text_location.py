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

text = "E = 0.4 mg IM Naloxone (1 mL of a 0.4 mg/mL commercial formulation)"
get_location(text, "E = 0.4 mg IM Naloxone (1 mL of a 0.4 mg/mL commercial formulation)")
