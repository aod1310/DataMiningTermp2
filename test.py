import pandas as pd
import numpy as np
import os
import pickle
from apyori import apriori
import time

path = './ml-25m/'
# data cleaning
import pickle
with open('rating_movie_mapping_cleaning.data', 'rb') as f:
    data = pickle.load(f)
data = data.drop(data.loc[data['is_provocative']==-1].index, axis=0)

# 자극적인걸 좋아한다는 기준? 자극적인 영화에 높은 레이팅(평균 4.5이상?)
users = set(data['userId'])
print(len(users))
like_provocative = []
for user in sorted(users):
    if np.mean(data[data['userId'] == user][data['is_provocative'] == 1]['rating']) > 4.5:
        print(user)
        like_provocative.append(user)

with open('like_provocative45.users', 'wb') as f:
    pickle.dump(like_provocative, f)

print(len(like_provocative))