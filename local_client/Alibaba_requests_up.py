import pandas as pd
import numpy as np

dataset = pd.read_csv('C:/Users/sch/PycharmProjects/pythonProject3/data/Alibaba_requests.csv')
requests = dataset['requests']

# convert to 5mim scale
requests_len = int(len(requests)/30)
k = []
sum_of = 0
for j in range(0, requests_len):
    for i in range(0, 30):
        sum_of = requests[30*j+i] + sum_of
    re_sum = sum_of/30
    sum_of = 0
    k.append(re_sum)

# ceil it and save
requests = np.ceil(k)
requests = requests.astype(np.int)

# jmeter limit
# requests = requests*300
requests = requests * 225

csv = pd.DataFrame(data=requests)
names = ['requests']
csv.columns = names
csv.to_csv('C:/Users/sch/PycharmProjects/pythonProject3/data/Alibaba_requests_up_5min_6core.csv')
