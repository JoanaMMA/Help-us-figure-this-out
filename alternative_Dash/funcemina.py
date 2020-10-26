# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 11:43:38 2020

@author: xXJaneXx
"""


import pandas as pd
import numpy as np

from sklearn import metrics
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

from pprint import pprint

# Get the data and change ? to nan-values
cle = pd.read_csv('processed.cleveland.csv', keep_default_na=False, na_values=["?"])

# Change num to goal
cle.rename(columns={'num': 'goal'}, inplace=True)

# Replacing NaN-values with most frequent

replc = SimpleImputer(strategy= 'most_frequent')
replc = replc.fit_transform(cle)
cle = pd.DataFrame(replc, columns=cle.columns)

#Labels
# Everything except goal
cle_features = cle.drop(['goal'], axis=1)
# Only goal
cle_label = cle['goal']

#normalization
feat_NoNorm = cle_features.drop(['age', 'trestbps', 'chol', 'oldpeak', 'thalach'], axis=1)
numerical = 'age', 'trestbps', 'chol', 'thalach', 'oldpeak', 
X = cle_features[[c for c in cle_features if c in numerical]]

scaler = StandardScaler()
feat_norm = scaler.fit_transform(X)
feat_norm = pd.DataFrame(feat_norm, columns=X.columns)

cle_feat = pd.concat([feat_norm,feat_NoNorm], axis=1)

#train
X_train, X_test, y_train, y_test = train_test_split(cle_feat, cle_label, test_size=0.3, random_state=321, stratify=cle_label)

#best model
lrclf = LogisticRegression(multi_class='ovr', max_iter=2000)
# lrclf.fit(X_train, y_train)
print('The parameters are:\n')
pprint(lrclf.get_params())

# C = np.logspace(0, 4, num=10)
# penalty = ['l1', 'l2']
# solver = ['liblinear', 'saga']
# hyperparameters = dict(C=C, penalty=penalty, solver=solver)

# randomizedsearch = RandomizedSearchCV(logistic, hyperparameters)
# best_model_random = randomizedsearch.fit(features, target)
# print(best_model_random.best_estimator_)


penalty = ['none', 'l1', 'l2', 'elasticnet']
solver = ['newton-cg', 'lbfgs', 'liblinear', 'saga']
C_lr = np.logspace(0, 4, num=10)

random_grid_lr = {'penalty': penalty,
                 'solver': solver,
                 'C': C_lr}
print('The random grid parameters are:\n')
pprint(random_grid_lr)

from sklearn.model_selection import RandomizedSearchCV

lr_random = RandomizedSearchCV(estimator = lrclf, param_distributions = random_grid_lr, n_iter=100, cv =5, verbose=2, n_jobs = -1)
lr_random.fit(X_train, y_train)

best_penalty  = lr_random.best_params_['penalty']
best_solver      = lr_random.best_params_['solver']
best_C_lr = lr_random.best_params_['C']

lrclf_best = LogisticRegression(multi_class='ovr', penalty=best_penalty, C=best_C_lr, solver=best_solver, max_iter=2000)
lrclf_best.fit(X_train, y_train)

y_pred_lr = lrclf_best.predict(X_test)
print(classification_report(y_test, y_pred_lr))

confusion_matrix(y_test, y_pred_lr)
print(confusion_matrix(y_test, y_pred_lr))


model=lrclf_best # Change to best performing model here
model.fit(X_train, y_train)

#data_to_classify = [45, 1, 2, 120, 155, 1, 0, 140, 0, 1.5, 3, 0, 3.0]
#colnames = X_test.columns

#sample = pd.DataFrame(data = [data_to_classify], columns = colnames)
#sample
#prediction = model.predict(sample)
#print("The Patient has a predicted risk for Heart disease of ", prediction[0])
#print(sample)