# Data Analysis on HR Dataset
MIT License
Data analysis and interactive dashboard creation on HR database. 

## Table of Content:
* [Project Overview](#project-overview)
* [Data Source and Dictionary](#data-source-and-dictionary)
* [Technology Stack](#technology-stack)
* [Setup and Local Installation](#setup-and-local-installation)
* [Author and Acknowledgements](#author-and-acknowledgements)

## Project Overview:
The purpose of the project is to create an interactive dashboard and conduct data analysis to help HR members gain a better understanding of employee data. This could result in improved efficiency, due to the HR members better understanding the employees, and in turn, how those employees can help the organization grow and grow alongside it.

## Data Source and Dictionary:
Data obtained from Kaggle dataset: https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset
EducationField is the field the employee got their degree in. 
JobRole is the employee's current title.
JobSatisfaction measures how satisfied the employee is with their job, with 4 being the most satisfied and 1 being the least satisfied.
MonthlyIncome is the employee's monthly salary.

## Technology Stack:
Language used is Python (libraries used: Pandas, SQLite3, Streamlit, and Plotly Express).
Pandas and SQLite3 are used to analyse the data, Streamlit and Plotly Express are used to build an interactive dashboard.

## Setup and Local Installation:
Make sure you have Anaconda, Conda, Python, and Git installed before beginning.

### 1- Clone the Repository:
open command prompt and clone the repository with the command below
'git clone https://github.com/Lana-Alruhaimi/HR_DataAnalysis.git'

then open the project directory
'cd HR_DataAnalysis'

### 2- Create and activate Conda:
using environment.yml, create a new conda enviornment with all necessary dependancies.
'conda env create -f environment.yml'

then activate it
'conda activate base'

### 3- Run Streamlit
after installing everthing, you can launch streamlit with the command below:
'streamlit run Dashboard_ST_PX.py'

## Author and Acknowledgements:
Code written by Lana, Data provided by Kaggle
