
# Loan Eligibility preidictor

Loan Eligibility preidictor is an AI based web app which has been built to classify customers whether they are eligible for taking Home loan from a insurance company.


## Problem Statement

Dream Housing Finance company deals in all kinds of home loans. They have presence across all urban, semi urban and rural areas. Customer first applies for home loan and after that company validates the customer eligibility for loan.

Company wants to automate the loan eligibility process (real time) based on customer detail provided while filling online application form. These details are Gender, Marital Status, Education, Number of Dependents, Income, Loan Amount, Credit History and others. To automate this process, they have provided a dataset to identify the customers segments that are eligible for loan amount so that they can specifically target these customers. 


## Proposed Solution

After the complete deployment of the WebApp in cloud. The webapp can be used by every customer of the insurance company to check their eligibility for taking loan. After filling the required details the webapp will be declaring their eligibility within some seconds of time. 
This will not only automate the process of customer verification but will also save a lot of time of both customer and the company itself.




Since the details entered by each customer will be saved in the database of the company so that they can further do some research on their customer reach. In this way they can target perticular group of customers. 


## Approach

The classical machine learning tasks like Data Exploration, Data Cleaning, Feature Engineering, Model Building and Model Testing.
#### Data Exploration
I started exploring datasets using pandas, NumPy,matplotlib and seaborn.
#### Data cleaning
checking null values, checking outliers, checking imbalance in dataset.
#### Data Visualization
Ploted colleration matrix to get insights about dependend and independed variables. making bar graphs, box plot, scatter plot, etc.
#### Model Selection
Made many Models(linear regression, svm, xgboost, Random Forest). All models were performing quite well so I selected Support Vector machine with an accuracy of 0.81 after perfoming hyperparameter tuning. 
#### Model Dump
As per selected trained model is dumped to pickled format for app development.


## Tools Used

- #### Pycharm has been used as IDE
- #### Streamlit : as a web framework
- #### Mongodb : mongodb compass for local and Atlas mongodb for cloud.
- #### Numpy,Pandas,Seaborn,Matplotlib : for EDA
- #### Heroku : used for deployment.
## User Interface
![Screenshot (22)](https://user-images.githubusercontent.com/66490787/151321419-1d882627-3dc6-4e41-a0d0-c9045d9da871.png)

![Screenshot (21)](https://user-images.githubusercontent.com/66490787/151321472-8ae343c5-df1e-4c84-8c81-8a3fc5b78650.png)



## Demo 


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)



