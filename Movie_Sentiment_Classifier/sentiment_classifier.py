from sklearn.externals import joblib

class SentimentClassifier(object):
    def __init__(self):
        self.model = joblib.load("classifier.pkl")
        self.classes_dict = {0: "negative", 1: "positive", -1: "prediction error"}

    def predict_text(self, text):
        try:
            return self.model.predict([text])[0]
        except:
            print "prediction error"
            return -1

    def get_prediction_message(self, text):
        prediction = self.predict_text(text)
        class_prediction = prediction
        return self.classes_dict[class_prediction]
