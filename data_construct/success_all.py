# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

dataset_success = pd.read_csv(
    'C:/Users/sch/PycharmProjects/pythonProject3/data/success.csv')
dataset_success_ad = pd.read_csv(
    'C:/Users/sch/PycharmProjects/pythonProject3/data/success_ad.csv')
dataset_success_hyscal = pd.read_csv(
    'C:/Users/sch/PycharmProjects/pythonProject3/data/success_hyscal.csv')
dataset_success_k8s = pd.read_csv(
    'C:/Users/sch/PycharmProjects/pythonProject3/data/success_k8s.csv')

data = np.zeros((4, 100))
data[0] = dataset_success['0']
data[1] = dataset_success_ad['0']
data[2] = dataset_success_k8s['0']
data[3] = dataset_success_hyscal['0']
names = ['success', 'success_ad', 'success_k8s', 'success_hyscal']
data = data.T
data = pd.DataFrame(data=data)
data.to_csv('C:/Users/sch/PycharmProjects/pythonProject3/csv/success.csv', header=names)