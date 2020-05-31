import joblib
from other.learn.CRF_learn.prediction_dir.input_preprocessing import preprocess, tagging, extractEntities

# Load model
model_path = "model\\test_2.pkl"
input_data = "GRANTOR(S): Gregory E. Seller and Pasquale Bettino, Jr. who are married to each as Joint Tenants he"\
             "reby GRANT(S) to Gregory E. Seller, a single man, the following described real property in the "\
             "County of Riverside , State of California"

def crf_prediction(model_path, input_text):
    from os import sep
    model_path = f"model{sep}{model_path}.pkl"
    crf_seller = joblib.load(model_path)
    parsed = preprocess(input_text)
    prediction = crf_seller.predict(parsed)
    # print(len(prediction))
    final_result = extractEntities(prediction[0], tagging(input_text))

    # print(final_result)

    return crf_seller, final_result

# crf_prediction(model_path, input_data)