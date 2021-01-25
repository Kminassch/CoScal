# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

data_success = pd.read_csv('C:/Users/sch/PycharmProjects/pythonProject3/csv/success.csv')
success = data_success['success']
success_ad = data_success['success_ad']
success_k8s = data_success['success_k8s']
success_hyscal = data_success['success_hyscal']
data = np.zeros((5, 4))

data[0, 0] = np.mean(success[0:20])
data[1, 0] = np.mean(success[0:40])
data[2, 0] = np.mean(success[0:60])
data[3, 0] = np.mean(success[0:80])
data[4, 0] = np.mean(success[0:100])

data[0, 1] = np.mean(success_ad[0:20])
data[1, 1] = np.mean(success_ad[0:40])
data[2, 1] = np.mean(success_ad[0:60])
data[3, 1] = np.mean(success_ad[0:80])
data[4, 1] = np.mean(success_ad[0:100])

data[0, 2] = np.mean(success_k8s[0:20])
data[1, 2] = np.mean(success_k8s[0:40])
data[2, 2] = np.mean(success_k8s[0:60])
data[3, 2] = np.mean(success_k8s[0:80])
data[4, 2] = np.mean(success_k8s[0:100])

data[0, 3] = np.mean(success_hyscal[0:20])
data[1, 3] = np.mean(success_hyscal[0:40])
data[2, 3] = np.mean(success_hyscal[0:60])
data[3, 3] = np.mean(success_hyscal[0:80])
data[4, 3] = np.mean(success_hyscal[0:100])
names = ['success', 'success_ad', 'success_k8s', 'success_hyscal']
data = pd.DataFrame(data=data)
data.to_csv('C:/Users/sch/PycharmProjects/pythonProject3/csv/success_avg.csv', header=names)