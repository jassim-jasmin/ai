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

text = "To determine the pharmacokinetics of 1 IN doses (1 mg, 2 mg (2 nostrils), 1 mg (2 nostril) and 9 mg) of naloxone compared to a 0.5 mg dose of naloxone administrated IM and to identify an appropriate IN dose that could achieve systemic exposure comparable to an approved parenteral dose."
get_location(text, "1 IN doses (1 mg, 2 mg (2 nostrils), 1 mg (2 nostril) and 9 mg) of naloxone compared to a 0.5 mg")
