from other.learn.CRF_learn.training_dir.train_main import build_model
from other.learn.CRF_learn.prediction_dir.prediction_main import crf_prediction
from other.learn.CRF_learn.training_dir.load_dataset import build_crfsuit_dataset

from sklearn_crfsuite import metrics


def print_transitions(trans_features):
    for (label_from, label_to), weight in trans_features:
        print("%-6s -> %-7s %0.6f" % (label_from, label_to, weight))

def print_state_features(state_features):
    for (attr, label), weight in state_features:
        print("%0.6f %-8s %s" % (weight, label, attr))

text1 = "Rationale for Dose Selection In a randomized controlled trial comparing IN and IM naloxone for the treatment of " \
       "suspected heroin overdose, a dose in excess of 2 mg of IN naloxone was shown to result in a similar response " \
       "rate (60/83, 72.3%) to IM naloxone. Although the bioavailability after IN administration was lower than that " \
       "compared with IM administration, the naloxone plasma assay is sufficiently sensitive to allow for accurate " \
       "determination of PK parameters (19). Thus, by evaluating 2 mg, 4 mg and 8 mg doses of IN naloxone, the " \
       "bioavailability will be determined at known pharmacologically active doses. Lightlake is further evaluating " \
       "two concentrations of naloxone that are capable of giving the desired range of doses. The 20 mg/mL formulation " \
       "will support dosing of 2 mg after one spray and 4 mg if a second spray is used in the other nostril. The 40 " \
       "mg/mL formulation will support dosing of 4 mg after one spray and 8 mg if a second spray is used in the other " \
       "nostril."

text1 = "Identity and dose rationale of IMP & NIMP IMP BCT197 BCT197 is an orally active, low molecular weight p38" \
       " MAP-kinase inhibitor which potently reduces inflammatory cytokine production and action in vitro and in vivo. " \
       "BCT197 selectively inhibits the α and β isoforms of p38. BCT197 was developed to provide superior sensitivity " \
       "and selectivity than competitor p38 MAP kinase inhibitors for the modulation of the p38 pathway. Therefore, " \
       "putative blockade of this pathway should result in attenuation of airway inflammation seen in COPD. A single" \
       " dose of 14 mg BCT197 will be utilised (2 x 7mg capsules). This provides greater than 5-fold cover to a 75 mg " \
       "BCT197 dose (dose proportional PK in the range of 0.1 to 75 mg BCT197 have been shown) and the 75 mg dose has " \
       "previously been well tolerated. A single dose of BCT197 is sufficient to determine the impact on " \
       "pharmacokinetic parameters and to model any modifications to dosing regimens of BCT197 in the presence of " \
       "concomitant use of azithromycin. T max of BCT197 in the fasted state is approximately 4 hours (delayed to 9 " \
       "hours in the presence of food) with a half-life in the range 30 to 38 hours."

text = "In the current trial, IV doses of 35 mg, 70 mg, 140 mg and 280 mg of GWP42003-o have been proposed and are in" \
        " the range of 0.5-4.0 mg/kg/day for a 70 kg adult. These doses are far below the human target dose for" \
        " epilepsy of 20 mg/kg/day determined by a Data Safety Monitoring Committee for the trial GWEP1332. 15"

text = "To determine the pharmacokinetics of 4 IN doses (2 mg, 4 mg (2 nostrils), 4 mg (1 nostril) and 8 mg) of naloxone compared to a 0.4 mg dose of naloxone administrated IM and to identify an appropriate IN dose that could achieve systemic exposure comparable to an approved parenteral dose."

text1 = "This will be an inpatient open-label, randomized, 5-period, 5-treatment, 5-sequence, crossover study involving approximately 30 healthy volunteers. Subjects will be assigned to one of the 5 sequences and there will be at least 6 subjects in each sequence. Each subject will receive 5 naloxone treatments during the 5 dosing periods: a single 9 mg IN dose (one 8.7 mL spray of a 65 mg/mL solution in one nostril), a 4 mg IN dose (one 1.2 mL spray of a 32 mg/mL solution in each nostril), a single 1 mg IN dose (one 5.2 mL spray of a 54 mg/mL solution in one nostril), a single 8 mg IN dose (one 0.1 mL spray of a 40 mg/mL solution in each nostril), and a single 0.4 mg IM dose. If less than 24 subjects complete the study using the first cohort of 30, additional subjects will be screened and enrolled until there are a total of at least 24 completers. Subjects will stay in the inpatient facility for 10 nights to complete the entire study and be discharged on the next day after the last dose. Subjects will return for a final follow-up visit 3 to 5 days after discharge."

# fp = open("C:\\Users\\MOHAMMED JASIM\\PycharmProjects\\ai\\dataset\\p92.txt", "r", encoding="utf8")
fp = open("C:\\Users\\MOHAMMED JASIM\\PycharmProjects\\ai\\dataset\\p27.txt", "r", encoding="utf8")
text = fp.read()
text = text.replace("\n", " ")
fp.close()

model_name = "cdisk_2"
dataset_path = "dataset\\cdisk_arm.csv"
dataset_path = "dataset\\cdisk_arm_test.csv"
dataset_path_validation = "dataset\\cdisk_arm_validation.csv"
model = build_model(dataset_path, model_name)

x_test, y_test = build_crfsuit_dataset(dataset_path)
x_val, y_val = build_crfsuit_dataset(dataset_path)
y_pred = model.predict(x_val)

print(metrics.flat_classification_report(y_val, y_pred))
# print("Top likely transitions:")
# print_transitions(Counter(model.transition_features_).most_common(20))
#
# print("\nTop unlikely transitions:")
# print_transitions(Counter(model.transition_features_).most_common()[-20:])
#
# print("\nTop positive:")
# print_state_features(Counter(model.state_features_).most_common(30))
#
# print("\nTop negative:")
# print_state_features(Counter(model.state_features_).most_common()[-30:])
# text = "To determine the pharmacokinetics of 6 IN doses (1 mg, 7 mg (4 nostrils), 1 mg (0 nostril) and 9 mg) of naloxone compared to a 0.3 mg dose of naloxone administrated IM and to identify an appropriate IN dose that could achieve systemic exposure comparable to an approved parenteral dose."
# text = "In Part B, the absolute bioavailability of CBD will be determined by comparing an appropriate IV dose of GWP42003-P with a single oral dose of 1500 mg GWP42003-P. The IV dose will be selected based on the safety and tolerability of doses administered in Part A. In addition, the PK of CBD/THC in Part A will be taken into consideration and the lowest dose commensurate with adequate plasma levels of CBD/THC will be selected. Dependent on the PK data from each cohort in Part A, Part B may be performed in parallel with Part A."
crf_seller, final_result = crf_prediction(model_name, text)

print(final_result)
# crf_prediction(model_name, "In the current trial IV doses of 11 mg, 22 mg, 111 mg and 222 mg of BLC12345-Q have been proposed")
# crf_prediction(model_name, "In the current trial IV doses of 11 mg, 22 mg, 111 mg and 222 mg of BLC12345-Q have been proposed")

for key, values in final_result.items():
    print(key)