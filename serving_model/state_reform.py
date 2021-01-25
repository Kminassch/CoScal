import pandas as pd
import numpy as np

dataset = pd.read_csv('C:/Users/sch/PycharmProjects/pythonProject3/data/state.csv')
state = dataset['state']
state = state.values

state_len = len(state)-5

state_re = np.zeros((state_len, 6), dtype=np.int)


for i in range(0, state_len):
    for j in range(0, 6):
        m = int(round(state[i+j]))
        if m > 4:
            m = 4
        state_re[i, j] = int(m)

csv = pd.DataFrame(data=state_re)
names = ['state01', 'state02', 'state03', 'state04', 'state05', 'state_p']
csv.columns = names
csv.to_csv('C:/Users/sch/PycharmProjects/pythonProject3/data/state_preprocessed.csv')
