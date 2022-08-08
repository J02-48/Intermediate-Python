#import library
import pandas as pd
import numpy as np
#Series
s = pd.Series(data=[[1,2,3],
                    [4,5,6]])
y = pd.Series(data=["Jonathan","james","fenny"])
x = pd.Series(data=[1,2,3,4,5,6])
print(s)
print(x)
print(y)
#Mengambil syntax menjadi series
myList = [1,2,3,4,5]
List = ["apple","orange","banana"]
z = pd.Series(myList)
d = pd.Series(List)
print(z)
print("buah2an:\n",d)
#Create a dictionary of Series then change it to DataFrame
v = {"Name":pd.Series(data=["evan","Louis","john"]),
     "Age":pd.Series(data=[15,16,17]),
     "Rating":pd.Series(data=[3.40,4.33,3.89])}
abc = pd.DataFrame(v)
print(abc)
#Menggabungkan 2 dataframe
df = pd.DataFrame([[1,2],[3,4]], columns=list("AB"), index=["x","y"])
df2 = pd.DataFrame([[5,6],[7,8]], columns=list("AB"), index=["x","y"])
df = df.append(df2)
print(df)
#membuat dataframe dari file csv
m = pd.read_csv("hotel.csv")
print(m)
print(m.shape)
print(m.head(10))
print(m.tail(15))
print(m.dtypes)
#edit dalam dataframe
w = {"Name":pd.Series(data=["evan","Louis","john"]),
     "Age":pd.Series(data=[15,16,17]),
     "Rating":pd.Series(data=[3.40,4.33,3.89])}
w = pd.DataFrame(w)
w.index = [1,2,3]
print(w)
#membuat dataframe dari file excel
u = pd.read_excel("CAR_MAINTENANCE.xlsx")
u = pd.DataFrame(u)
print(u)
#data summarization
print(m.describe())
print(m.astype("object").describe())
print(m.info())
#Selecting and Indexing
#iloc
data = m
print(data)
print(data.iloc[0:1133,0:6]) #iloc untuk menampilkan data yang kita mau saja
print(data.iloc[:,0:4])
print(data.iloc[[0,-1],:])
cv = data.iloc[:10,:3]
print(cv)
print(cv.iloc[[1,3], -1:]) #melakukan slicing data
#loc
apa = m
print(data.loc[3:23, "adults"])
#filtering
print(data.loc[data["adults"] == 0])
#sorting
data = pd.read_csv("hotel.csv")
x = data.sort_values(by=["adults"], ascending=False)
print(x.loc[:,"adults"])
#conditionally adding columns
data["children"] = np.where(data["adults"]>1, "bocil", "short")
print(data.loc[:,"children"])
print(data["children"].value_counts())
data["children"] = np.where(data["adults"]==0, "yatim","anak biasa")
print(data.loc[:,"children"])
print(data["children"].value_counts())
#Group by Summarize
k = pd.read_csv("hotel.csv")
p = k.groupby("hotel")["children"].agg(["mean", "sum"])
print(p)
print(p["children"].value_counts())
