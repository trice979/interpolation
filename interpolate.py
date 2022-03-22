import pandas as pd
import numpy as np
import scipy.interpolate
import pyodbc

conn = pyodbc.connect('DSN=db_server; Trusted_Connection=yes;')

sql = """	

SELECT			[5], [10] , [15] , [20], [25] , [30], [35], [40], [45], [50], [55], [60], [65], [70], [75], [80], [85], [90], [95]
FROM  			Analytics.SCRATCH.comps

"""
df = pd.read_sql(sql, conn)
# print(df)

x = np.arange(5,100,5)
y = []

for i in x:
	y.append(df[str(i)][0])

y_interp = scipy.interpolate.interp1d(x, y)

for i in range(5,96):
	print(i, ' ' ,y_interp(i))
