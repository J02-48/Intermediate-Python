##SETUP
import pandas as pd
import numpy as np
df = pd.read_csv("uber2016.csv")
print("\nData Awal: ")
print(df)
##PENGERJAAN
condlist = [df["MILES*"]<5, df["MILES*"]>10, df["MILES*"]>=5]
choicelist = ["Short Trip", "Long Trip", "Medium Trip"]
df["MILES*"]= np.select(condlist, choicelist, 0)
print("\nDataFrame setelah membuat kategori baru:")
print(df)
