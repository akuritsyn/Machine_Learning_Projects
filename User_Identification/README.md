# Identification of internet users based on their internet behavior

## Introduction / Problem statement
In this project we are solving a problem of user identification based on their behavior on the Internet. This is a complex and interesting problem at a junction of data science and behavioral phsycology. For example, many email providers are trying to identify email hackers based on their behavior. Obviously, a hacker will behave differently than the email owner: he may not be deleting emails after reading them as the email owner used to do, he will be marking messages differently, etc. If this is a case, such an intruder can be identified and expelled from the email box by offering the true owner to enter his email acccount by using a code sent via SMS. In data science such problems are called "Traversal Pattern Mining" or "Sequential Pattern Mining". Such problems are solved, for example, by a Google analytics team.

Here,  we will attempt to identify a person based on data about websites sequentially visited by him/her. The idea is that users move differently between websites and this can help to identify them. We'll be using data from the [article](http://ceur-ws.org/Vol-1703/paper12.pdf)  "A Tool for Classification of Sequential Data". 

The data came from the proxy-servers at Blaise Pascal University and looks like this: there is a csv-file with a name user\*\*\*\*.csv, where stars respresent 4 digits corresponding to the user ID. Each file contains information about website visits in the following format: *timestamp, visited web-site*

The full dataset with description is available from the link in the [article](http://fc.isima.fr/~kahngi/cez13.zip).
However, for initial model development, we will not use data from all 3000 users, but from 10 and 150. Here is a [Link](https://yadi.sk/d/_HK76ZDo32AvNZ) to archive *capstone_websites_data.zip*. 10-user data set will be used for initial model development and 150-user for further validation. Then the model will be used to participate in [Kaggle competition](https://inclass.kaggle.com/c/identify-me-if-you-can4) (1st place was achieved).

This project consists of several parts: 
1. Data preparation
2. Feature preparation and initial data analysis 
3. Analysis of additional features
4. Comparison of classification algorithms
5. SGDClassifier and Kaggle competition
6. Vowpal Wabbit library & tf-idf
7. Conclusions
