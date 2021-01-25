"""
docker run -t --rm -p 8501:8501 -v "C:/Users/sch/PycharmProjects/pythonProject3/tf_model:/models/state" -e MODEL_NAME=state tensorflow/serving &

docker run -t --rm -p 8501:8501 -v "F:\data\tf_model:/models/state" -e MODEL_NAME=state tensorflow/serving &
"""

import json
from time import sleep
import paramiko
import requests
import numpy as np
import pandas as pd

dataset = pd.read_csv('C:/Users/sch/PycharmProjects/pythonProject3/data/state_adjust.csv', low_memory=False)
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
json_response = requests.post('http://localhost:8501/v1/models/state:predict',
                              data=data, headers=headers)
predictions = json.loads(json_response.text)["predictions"]
predictions = np.array(predictions)
predictions = np.round(predictions)
state_curr = predictions[0]

"""
docker update -m 100m 2d3e 4280 75bc a2d2 3019 7e0b a038
docker update -m 3.752g 2d3e 4280 75bc a2d2 3019 7e0b a038
"""
if state_curr == 0:
    if state_la == 0:
        sleep(10)
    elif state_la > 0:
        ssh.exec_command('docker restart 2d3e 4280 75bc a2d2 3019 7e0b a038 8995')
        # ssh.exec_command('docker update -m 3.752g 3d97 78cf e08b 9a15')
        ssh.close()
elif state_curr > 0:
    if state_la == 0:
        ssh.exec_command('docker stop 2d3e 4280 75bc a2d2 3019 7e0b a038 8995')
        # ssh.exec_command('docker update -m 100m 3d97 78cf e08b 9a15')
        ssh.close()
    elif state_la > 0:
        sleep(10)

# elif state_curr == 1:
#     ssh.exec_command('docker ps -a')
#     ssh.close()
# elif state_curr == 2:
#     ssh.exec_command('docker ps -a')
#     ssh.close()
# elif state_curr == 3:
#     ssh.exec_command('docker ps -a')
#     ssh.close()
# elif state_curr == 4:
#     ssh.exec_command('docker ps -a')
#     ssh.close()
