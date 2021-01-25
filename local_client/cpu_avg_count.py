# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

dataset = pd.read_csv('report.csv')
data_120 = dataset.iloc[-120:, :]
cpu = data_120['CPU ']
cpu_add = 0
for i in range(0, 120):
    cpu_add = cpu_add + cpu[i]
cpu_avg = cpu_add / 120

print(cpu_avg)