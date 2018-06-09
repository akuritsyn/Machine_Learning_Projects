## Movie Sentiment Classifier

In this project we perform sentiment analysis of movie reviews.

A pipeline consisting of a CountVectorizer, tf-idf and LinearSVC is employed to build a classifier, then a standard ntlk data set is used for classifier training, and 
finally a web demo is created using flask.

Instructions for executing on your local machine:
1. Run SentimentClassifierModel.ipynb to generate classfier.pkl 
2. Run: python demo.py from its directory
3. Open demo in a browser: http://127.0.0.1:5000/sentiment-demo

A demo is also running on the AWS ([link1](http://13.57.29.37/sentiment-demo), [link2](http://ec2-13-57-29-37.us-west-1.compute.amazonaws.com/sentiment-demo)).
Note that due to space constraints on free AWS accounts, the model hosted there has been trained on a smaller data set and therefore is not as accurate.
I will add detailed instructions on how to run a flask app on AWS EC2 instance (Apache webserver on Ubuntu) in the near future. In the meanwhile you can refer to [this tutorial](http://www.datasciencebytes.com/bytes/2015/02/24/running-a-flask-app-on-aws-ec2/).

As a follow up step, one can try to add a confidence metric to the results based on the predicition probability reported by the classifier.

