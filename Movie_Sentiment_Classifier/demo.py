from sentiment_classifier import SentimentClassifier
from codecs import open
import time
from flask import Flask, render_template, request
app = Flask(__name__)

print "Preparing classifier"
start_time = time.time()
classifier = SentimentClassifier()
print "Classifier is ready"
print time.time() - start_time, "seconds"

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

@app.route("/sentiment-demo", methods=["POST", "GET"])
def index_page(text="", prediction_message=""):
    if request.method == "POST":
        text = request.form["text"]
        if is_ascii(text):
            print text
        else:
            text = "Not ASCII - ERROR"

        logfile = open("demo_logs.txt", "a", "utf-8")
	print text
	print >> logfile, "<response>"
	print >> logfile, text
        prediction_message = classifier.get_prediction_message(text)
        print prediction_message
	print >> logfile, prediction_message
	print >> logfile, "</response>"
	logfile.close()
	
    return render_template('template.html', text=text, prediction_message=prediction_message)

@app.route('/')
def hello_world():
  return 'The sentiment demo is at /sentiment-demo'

if __name__ == '__main__':
  app.run(debug=True)






