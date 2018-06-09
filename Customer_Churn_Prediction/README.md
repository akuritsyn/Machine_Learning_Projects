# Customer Churn Prediction

## Introduction and Problem statement

The goal of the Customer Churn Prediction project is to find clients of a telecom company who are likely to churn.
Banks, telephone service companies, Internet service providers, pay TV companies, insurance firms, alarm monitoring services and others often use customer churn analysis and customer churn rates as one of their key business metrics, because the cost of retaining an existing customer is far less than acquiring a new one. Companies from these sectors often have customer service branches, which job is to win back defecting clients, because long-term clients can bring much more profit to a company than newly recruited ones.
In this project, we will make a prediction that a client will stop using a service during a pre-defined time period by solving a binary classification problem. We'll be using data from the 2009 competition described [here](http://www.kdd.org/kdd-cup/view/kdd-cup-2009/Intro). This is a real data set collected by the French telecom company Orange, where all the personal information about users has been deleted so that individual users can not be identified based on this data. The data set consists of 50,000 objects and comprises 190 numerical and 40 categorical variables. We'll use 40,000 objects as a training data set and remaining 10,000 as a validation data set. The data has significant imbalace, where less that 8% of users belong to the churn class.
In practice, using these predictions one can determine clients who are likely to churn and take measures to keep them as well as to idenify and fix any existing problems. In particular, model developed here can be used as a baseline for defining priorities of the customer retention campaign in the framework of a chosen economic model.

This project consists of several parts: 
1. Introduction and problem statement
2. Performance metrics and success criteria
3. Model development
4. Model performance and economic impact
5. Conclusions
