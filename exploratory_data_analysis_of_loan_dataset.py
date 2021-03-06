# -*- coding: utf-8 -*-
"""Exploratory Data Analysis of Loan Dataset

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SxHD_PYhoVObLsJd2RlgLJGUY2Hr4Vyr
"""

import pandas as pd
a=pd.read_csv("/content/loan_data.csv - loan_data.csv.csv")
a

# Commented out IPython magic to ensure Python compatibility.
import seaborn as sns
# %matplotlib inline

sns.jointplot(x="Education",y="ApplicantIncome",data=a,kind="scatter")

sns.jointplot(x="Credit_History",y="ApplicantIncome",data=a,kind="reg")

import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(40, 20))
sns.barplot(x="ApplicantIncome",y="Loan_Amount_Term",data=a)

sns.barplot(x="Gender",y="ApplicantIncome",data=a)

plt.figure(figsize=(40, 10))
sns.barplot(x="ApplicantIncome",y="Credit_History",hue="Gender",data=a)

plt.figure(figsize=(40,20))
sns.barplot(x="CoapplicantIncome",y="ApplicantIncome",hue="Gender",data=a)

sns.barplot(x="Gender",y="Credit_History",data=a)

sns.barplot(x="ApplicantIncome",y="Gender",data=a,order=["Male","Female"])

sns.countplot(x="Gender",data=a)

sns.countplot(x="Credit_History",hue="Gender",data=a)

sns.countplot(y="Credit_History",hue="Gender",data=a)

sns.boxplot(x="Credit_History",y="ApplicantIncome",data=a)

a.pivot_table(values="ApplicantIncome",index="Credit_History",columns="Gender")

