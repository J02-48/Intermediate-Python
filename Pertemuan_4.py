##SETUP
import pandas as pd
df = pd.read_csv("titanic.csv")
print(df.loc[:,"Age"].value_counts())
##DROP MISSING VALUES
data = df
print(data)
data.dropna(axis=0, how="all", inplace=True)
print(data)
#how = "all" menghapus semuanya jika itu missing value
#how = "any" menghapus jika minimal ada satu missing value
##MENGISI MISSING VALUE
fc = df.fillna(data["Age"].median())
y = df.loc[:, "Age"]
print(y.value_counts())
print(df.isna().sum())
##MENGISI MISSING VALUE JIKA JUMLAHNYA LEBIH DARI 50%
perc = 50
min_count = int(((100-perc)/100)*df.shape[0]+1)
xyz = df.dropna(axis=1, thresh=min_count)
print(xyz)
print(xyz.isna().sum())
