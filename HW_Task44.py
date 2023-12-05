import pandas as pd 
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head(20))
data['result'] = 1
data.set_index([data.index, 'whoAmI'], inplace=True)
data = data.unstack(level=-1, fill_value = 0)
print()
print(data)