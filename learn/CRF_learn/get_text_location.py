import re

def get_location(text, search_text):
    data = re.search(search_text, text)
    print(data.span())
    (l, r) = data.span()
    # print(text[l:r]+':::')

    return l, r

text = "To determine the pharmacokinetics of 4 IN doses o1 mg, 2 mg o2 nostrilso, 1 mg o9 nostrilo and 0 mgo of naloxone compared to a 0.1 mg dose of naloxone administrated IM and to identify an appropriate IN dose that could achieve systemic exposure comparable to an approved parenteral dose."
get_location(text, "4 IN doses o1 mg, 2 mg o2 nostrilso, 1 mg o9 nostrilo and 0 mgo of naloxone compared to a 0.1 mg")
