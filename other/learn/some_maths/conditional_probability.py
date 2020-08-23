"""
Experiment on conditional probability.
"""

from numpy import random


def sample_purchase_data_generator(independent: bool = True) -> dict:
    """
    :var dependent: It is for experimenting dependency of age and purchase. if set age_factor will not be considered.
    """
    def set_group_count(group_list: list):
        """
        Simply assigning zero for each group.
        :var group_list: age group list
        """
        group_dicitionary = dict()

        for each_group in group_list:
            group_dicitionary[each_group] = 0

        return group_dicitionary

    def purchase_generator(total_person_count: int, age_group_dict: dict, purchase_dict: dict) -> (dict, dict):
        """
        :var total_person_count: Toal number of persons to be available in data generation
        :var age_group_dict: Dictionary of age with count initialized
        :var purchase_dict: Dictionary of purchase with count initialized
        """
        purchased_record = dict()
        total_purchase_count = 0  # initially it set as zero
        random.seed(0)
        list_of_age_group = list(age_group_dict.keys())

        for _ in range(total_person_count):
            random_individual_age = random.choice(list_of_age_group)  # a random age group
            age_factor = float(random_individual_age) / 100.0
            age_group_dict[random_individual_age] += 1  # Incrementing the age group
            random_generated_number = random.random()

            if random_generated_number < age_factor or independent:  # For getting random person to be purchased.
                total_purchase_count += 1
                purchase_dict[random_individual_age] += 1  # Setting purchase for that individual

        purchased_record['total_purchase_data'] = total_purchase_count
        purchased_record['total_person_count'] = total_person_count
        purchased_record['purchased'] = purchase_dict
        purchased_record['age_group'] = age_group_dict

        return purchased_record

    age_group = [20, 30, 40, 50, 60, 70]
    total_person = 100000
    age_group_count = set_group_count(age_group)  # declaring persons with count age as zero
    purchase_count = set_group_count(age_group)  # declaring purchase count with count as zero
    # Both count setting initially to zero
    purchase_record = purchase_generator(total_person, age_group_count, purchase_count)

    return purchase_record


"""
For computing conditional probability, we need to calculate following values

1. P(E/F) = > { E is purchase and F is probability of age }
    ie, probability_of_purchase_given_age
2. P(F) is just the probability of being an age
    ie, probability_of_age
3. P(E) is the overall probability of buying something, regardless of age
    ie, probability_of_purchase
4. P(E,F) probability of both being in a particular age and buying something
    ie, probability_of_age_and_purchase
"""


def probability_of_purchase_given_age(record: dict):
    return lambda age: float(record['purchased'][age]) / float(record['age_group'][age])


def probability_of_age(record: dict):
    return lambda age: float(record['age_group'][age]) / float(record['total_person_count'])


def probability_of_purchase(record: dict):
    return lambda age: float(purchased_record['total_purchase_data']) / float(record['total_person_count'])


def probability_of_age_and_purchase(record: dict):
    return lambda age: float(record['purchased'][age]) / float(record['total_person_count'])


purchased_record = sample_purchase_data_generator()

get_probability_of_age = probability_of_age(purchased_record)
get_probability_of_purchase_given_age = probability_of_purchase_given_age(purchased_record)
get_probability_of_purchase = probability_of_purchase(purchased_record)
get_probability_of_age_and_purchase = probability_of_age_and_purchase(purchased_record)

result = dict()

age = 30

result['P(E/F)'] = get_probability_of_purchase_given_age(age)
result['P(F)'] = get_probability_of_age(age)
result['P(E)'] = get_probability_of_purchase(age)
result['P(E,F)'] = get_probability_of_age_and_purchase(age)
result['P(E)*P(F)'] = result['P(E)'] * result['P(F)']
result['P(E,F)/P(F)'] = result['P(E,F)'] / result['P(F)']

print('age list', purchased_record['age_group'])
print('purchase list', purchased_record['purchased'])

if result['P(E,F)'] == result['P(E)*P(F)']:
    print("Independent, P(E,F) = P(E)*P(F)")

else:
    print("Dependent, P(E,F) != P(E)*P(F)")

if result['P(E/F)'] == result['P(E,F)/P(F)']:
    print('P(E/F) = P(E,F)/P(F)')

else:
    print('P(E/F) != P(E,F)/P(F)')
