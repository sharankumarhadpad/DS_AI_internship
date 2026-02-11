import numpy as np
import pandas as pd
values = pd.Series([700,150,300],index = ['laptop','mouse','keyboard'])
print(values)
print("laptop_price",values['laptop'])
print(values[0:2])

# task2 the grade filter
grades = pd.Series([85,None,92,45,None,78,55])
grades.isnull()
grades.fillna(0)
print(grades[grades > 60])

# task 3 the username formatter
usernames = pd.Series(['Alice','bob','Charlie_Data','daisy'])
usernames.str.strip()
usernames.str.lower()
lo = usernames.str.lower()
lo.str.contains(('a'))
print(lo[lo.str.contains('a')])
