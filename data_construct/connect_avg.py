# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

data_connect = pd.read_csv('C:/Users/sch/PycharmProjects/pythonProject3/csv/connect.csv')
connect = data_connect['connect']
connect_ad = data_connect['connect_ad']
connect_k8s = data_connect['connect_k8s']
connect_hyscal = data_connect['connect_hyscal']
data = np.zeros((5, 4))

data[0, 0] = np.mean(connect[0:20])
data[1, 0] = np.mean(connect[0:40])
data[2, 0] = np.mean(connect[0:60])
data[3, 0] = np.mean(connect[0:80])
data[4, 0] = np.mean(connect[0:100])

data[0, 1] = np.mean(connect_ad[0:20])
data[1, 1] = np.mean(connect_ad[0:40])
data[2, 1] = np.mean(connect_ad[0:60])
data[3, 1] = np.mean(connect_ad[0:80])
data[4, 1] = np.mean(connect_ad[0:100])

data[0, 2] = np.mean(connect_k8s[0:20])
data[1, 2] = np.mean(connect_k8s[0:40])
data[2, 2] = np.mean(connect_k8s[0:60])
data[3, 2] = np.mean(connect_k8s[0:80])
data[4, 2] = np.mean(connect_k8s[0:100])

data[0, 3] = np.mean(connect_hyscal[0:20])
data[1, 3] = np.mean(connect_hyscal[0:40])
data[2, 3] = np.mean(connect_hyscal[0:60])
data[3, 3] = np.mean(connect_hyscal[0:80])
data[4, 3] = np.mean(connect_hyscal[0:100])
names = ['connect', 'connect_ad', 'connect_k8s', 'connect_hyscal']
data = pd.DataFrame(data=data)
data.to_csv('C:/Users/sch/PycharmProjects/pythonProject3/csv/connect_avg.csv', header=names)