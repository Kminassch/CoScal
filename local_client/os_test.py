import os
from time import sleep
import pandas as pd
import numpy as np
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='172.20.110.72', port=22, username='root', password='1212')
stdin, stdout, stderr = ssh.exec_command('python3 /home/sch/cpu_record/cpu_avg_count.py')

result_cpu = stdout.read().decode('utf-8')
print(result_cpu)
ssh.close()
