# -*- coding: utf-8 -*-
import json
import paramiko
import requests
import numpy as np
import pandas as pd

dataset = pd.read_csv('lowtest_hor.csv', low_memory=False)
data_5 = dataset.iloc[-5:, :]
data_5 = data_5['state']
data_5 = np.array(data_5)
s = [[int(data_5[0]), int(data_5[1]), int(data_5[2]), int(data_5[3]), int(data_5[4])]]
state_la = int(data_5[4])
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='172.20.110.72', port=22, username='root', password='1212')
data = json.dumps({"signature_name": "serving_default", "instances": s})

headers = {"content-type": "application/json"}
json_response = requests.post('http://172.20.110.29:8501/v1/models/state:predict',
                              data=data, headers=headers)
predictions = json.loads(json_response.text)["predictions"]
predictions = np.array(predictions)
predictions = np.round(predictions)
state_curr = predictions[0]

if state_curr == 4:
    switch_on = 1
else:
    switch_on = 0
