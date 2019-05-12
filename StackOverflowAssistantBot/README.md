# Stackoverflow Assistant NLP Chatbot - Coursera [HSE NLP](https://www.coursera.org/learn/language-processing) final project
### The Chatbot up and running on AWS and can be accessed via Telegram messenger at AKStackOverflowBot. It is able to 
*answer programming questions using Stackoverflow dataset 
*chit-chat and simulate dialogue on all non-programming related questions

1. The model for running the bot is pre-trained using Jupyter notebook called training.ipynb:
* To detect intent of users questions we'll train a classifier, which uses StackOverflow posts tagged with one programming language as positive samples and
dialogue phrases from movie subtitles as negative samples. The classifier will perform binary classification on TF-IDF representation of texts.
* For those questions, that have programming-related intent, we will train a 2nd one-vs-rest classifier to predict a programming language 
(only one tag per question allowed here) and then rank candidates within the tag using embeddings. Since it is costly to compute such representations for possible
answers in real time, we will create a databse with precomputed representations. Then, when we get a question in real time, we only need to compute its embedding and then
compute cosine-similarity to get the highest ranked answer.

2. The workflow for running the chatbot on AWS: AWS --> ssh --> tmux --> docker --> python

2.1 Create AWS instance
You can use [this instructions](https://github.com/hse-aml/natural-language-processing/blob/master/AWS-tutorial.md) 

2.2 ssh to it & copy all nesessary files to <bot_folder>

2.3 Create a new tmux session:
tmux new -s <bot_session>
tmux detach or Ctrl+b & d - to disconnect
tmux attach -t <bot_session>
cd <bot_folder>

2.4 Run docker:
docker tutorial: https://github.com/hse-aml/natural-language-processing/blob/master/Docker-tutorial.md

docker pull akashin/coursera-aml-nlp
get list of containers: docker ps -a
remove old container: docker rm coursera-aml-nlp

Start new container and mount a directory from your local machine within the container using -v option:
docker run -it -p 8080:8080 --name coursera-aml-nlp -v $PWD:/root/coursera akashin/coursera-aml-nlp
- can use different path instead of PWD

2.5 Integrate bot to [Telegram](https://telegram.org) messenger
Talk to @BotFather in Telegram. The command "/newbot" will create a bot for you. You will be prompted to enter a name and a username for your bot. After that, you will be given a <new_token>.

2.5 Run python:
python3 main_bot.py --token=<your token>
Ctrl+b & d - to detach tmux session