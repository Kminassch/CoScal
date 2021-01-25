# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

dataset_connect = pd.read_csv(
    'C:/Users/sch/PycharmProjects/pythonProject3/data/connect.csv')
dataset_connect_ad = pd.read_csv(
    'C:/Users/sch/PycharmProjects/pythonProject3/data/connect_ad.csv')
dataset_connect_hyscal = pd.read_csv(
    'C:/Users/sch/PycharmProjects/pythonProject3/data/connect_hyscal.csv')
dataset_connect_k8s = pd.read_csv(
    'C:/Users/sch/PycharmProjects/pythonProject3/data/connect_k8s.csv')

data = np.zeros((4, 100))
data[0] = dataset_connect['0']
data[1] = dataset_connect_ad['0']
data[2] = dataset_connect_k8s['0']
data[3] = dataset_connect_hyscal['0']
names = ['connect', 'connect_ad', 'connect_k8s', 'connect_hyscal']
data = data.T
data = pd.DataFrame(data=data)
data.to_csv('C:/Users/sch/PycharmProjects/pythonProject3/csv/connect.csv', header=names)