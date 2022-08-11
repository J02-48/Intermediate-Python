##SETUP
import pandas as pd
import numpy as np
df = pd.read_csv("uber2016.csv")
print("\nData Awal: ")
print(df)
##PENGERJAAN
condlist = [df["MILES*"]<5,
            (df["MILES*"]>=5) & (df["MILES*"]<=10),
            df["MILES*"]>10]
choicelist = ["Short Trip","Medium Trip", "Long Trip"]
df["Trip Category"]= np.select(condlist, choicelist)
print("\nDataFrame setelah membuat kategori baru:")
print(df)
