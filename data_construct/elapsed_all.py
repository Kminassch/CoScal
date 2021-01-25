# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

dataset_elapsed = pd.read_csv(
    'C:/Users/sch/PycharmProjects/pythonProject3/data/elapsed.csv')
dataset_elapsed_ad = pd.read_csv(
    'C:/Users/sch/PycharmProjects/pythonProject3/data/elapsed_ad.csv')
dataset_elapsed_hyscal = pd.read_csv(
    'C:/Users/sch/PycharmProjects/pythonProject3/data/elapsed_hyscal.csv')
dataset_elapsed_k8s = pd.read_csv(
    'C:/Users/sch/PycharmProjects/pythonProject3/data/elapsed_k8s.csv')

data = np.zeros((4, 100))
data[0] = dataset_elapsed['0']
data[1] = dataset_elapsed_ad['0']
data[2] = dataset_elapsed_k8s['0']
data[3] = dataset_elapsed_hyscal['0']
names = ['elapsed', 'elapsed_ad', 'elapsed_k8s', 'elapsed_hyscal']
data = data.T
data = pd.DataFrame(data=data)
data.to_csv('C:/Users/sch/PycharmProjects/pythonProject3/csv/elapsed.csv', header=names)