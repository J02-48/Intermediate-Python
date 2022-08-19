##SETUP
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("hotel.csv")
print("Inilah final project jonathan")
input("Berikut adalah Gambaran Awal Data, ketik apapun untuk lanjut: ")
##SOAL 1 GAMBARAN AWAL DATA
print("\n----------- Gambaran Awal Data -----------")
print(df)
print("\nBerikutnya adalah missing data")
input("Ketik apapun untuk melanjutkan:")
##SOAL 2 PROPERTIES DATA
print("\n----------- Missing Data -----------")
print(df.isna().sum())
print("\nBerikutnya adalah tipe data")
input("Ketik apapun untuk melanjutkan:")
print("\n----------- Data Types-----------")
print(df.dtypes)
print("\nBerikutnya adalah jumlah data")
input("Ketik apapun untuk melanjutkan:")
##SOAL 3 MEAN MEDIAN DAN STANDAR DEVIASI
MedianValues = df[["is_canceled", "lead_time", "arrival_date_year",
                "arrival_date_week_number", "arrival_date_day_of_month",
                "stays_in_weekend_nights", "stays_in_week_nights", "adults",
                "children", "babies", "is_repeated_guest", "previous_cancellations",
                "previous_bookings_not_canceled", "booking_changes",
                "agent", "company", "days_in_waiting_list", "adr", "required_car_parking_spaces",
                "total_of_special_requests"]].median()
MeanValues = df[["is_canceled", "lead_time", "arrival_date_year",
                "arrival_date_week_number", "arrival_date_day_of_month",
                "stays_in_weekend_nights", "stays_in_week_nights", "adults",
                "children", "babies", "is_repeated_guest", "previous_cancellations",
                "previous_bookings_not_canceled", "booking_changes",
                "agent", "company", "days_in_waiting_list", "adr", "required_car_parking_spaces",
                "total_of_special_requests"]].mean()
StdValues = df[["is_canceled", "lead_time", "arrival_date_year",
                "arrival_date_week_number", "arrival_date_day_of_month",
                "stays_in_weekend_nights", "stays_in_week_nights", "adults",
                "children", "babies", "is_repeated_guest", "previous_cancellations",
                "previous_bookings_not_canceled", "booking_changes",
                "agent", "company", "days_in_waiting_list", "adr", "required_car_parking_spaces",
                "total_of_special_requests"]].std()
print("\n----------- Jumlah Data -----------")
print(df.count())
print("\nBerikutnya adalah median data")
input("Ketik apapun untuk melanjutkan:")
print("\n----------- Median -----------")
print(MedianValues)
print("\nBerikutnya adalah standar deviasi data")
input("Ketik apapun untuk melanjutkan:")
print("\n----------- Standar Deviasi -----------")
print(StdValues)
print("\nBerikutnya adalah mean data")
input("Ketik apapun untuk melanjutkan:")
print("\n----------- Mean -----------")
print(MeanValues)
print("\nBerikutnya adalah maksimum data")
input("Ketik apapun untuk melanjutkan:")
##SOAL 4 MAXIMUM DAN MINIMUM UNTUK KOLOM DENGAN DATA NUMERIK
MaxValues = df[["is_canceled", "lead_time", "arrival_date_year",
                "arrival_date_week_number", "arrival_date_day_of_month",
                "stays_in_weekend_nights", "stays_in_week_nights", "adults",
                "children", "babies", "is_repeated_guest", "previous_cancellations",
                "previous_bookings_not_canceled", "booking_changes",
                "agent", "company", "days_in_waiting_list", "adr", "required_car_parking_spaces",
                "total_of_special_requests"]].max()
MinValues = df[["is_canceled", "lead_time", "arrival_date_year",
                "arrival_date_week_number", "arrival_date_day_of_month",
                "stays_in_weekend_nights", "stays_in_week_nights", "adults",
                "children", "babies", "is_repeated_guest", "previous_cancellations",
                "previous_bookings_not_canceled", "booking_changes",
                "agent", "company", "days_in_waiting_list", "adr", "required_car_parking_spaces",
                "total_of_special_requests"]].min()
print("\n----------- Maximum -----------")
print(MaxValues)
print("\nBerikutnya adalah nilai minimum data")
input("Ketik apapun untuk melanjutkan:")
print("\n----------- Minimum -----------")
print(MinValues)
print("\nBerikutnya adalah jumlah missing value setelah melakukan drop")
input("Ketik apapun untuk melanjutkan:")
##SOAL 5 MENYELESAIKAN MASALAH MISSING VALUE
perc = 50
min_count = int(((100-perc)/100)*df.shape[0]+1)
df = df.dropna(axis=1, thresh=min_count)
print("\n----------- Jumlah Missing Value Setelah Drop -----------")
print(df.isna().sum())
print("\nBerikutnya adalah jumlah missing value data setelah semuanya diisi")
input("Ketik apapun untuk melanjutkan:")
for column in df.columns:
    df["country"].fillna(df["country"].mode()[0], inplace=True)
    df["children"].fillna(df["children"].mode()[0], inplace=True)
    df["agent"].fillna(int(df["agent"].mean()), inplace=True)
print("\n----------- Semua Missing Value Sudah Terisi -----------")
print(df.isna().sum())
print("\nBerikutnya adalah penambahan column")
input("Ketik apapun untuk melanjutkan: ")
#SOAL 6 MEMBUAT KATEGORI BARU
condlist = [df["lead_time"]<50,
            (df["lead_time"]>=50) & (df["lead_time"]<=100),
            df["lead_time"]>100]
choicelist = ["Short","Medium", "Long"]
df["type"]= np.select(condlist, choicelist)
print(df)
print("\nBerikutnya adalah filtering data")
input("Ketik apapun untuk melanjutkan: ")
##SOAL 7 Filter reservation_status_date > 2017
print(df.loc[df["reservation_status_date"]>"2017"])
print("\nBerikutnya adalah visualisasi data")
input("Ketik apapun untuk melanjutkan: ")
##SOAl 8 Visualisasi arrival_date_montha
JanuaryValues=(df["arrival_date_month"]=="January").sum()
FebruaryValues=(df["arrival_date_month"]=="February").sum()
MarchValues=(df["arrival_date_month"]=="March").sum()
AprilValues=(df["arrival_date_month"]=="April").sum()
MayValues=(df["arrival_date_month"]=="May").sum()
JuneValues=(df["arrival_date_month"]=="June").sum()
JulyValues=(df["arrival_date_month"]=="July").sum()
AugustValues=(df["arrival_date_month"]=="August").sum()
SeptemberValues=(df["arrival_date_month"]=="September").sum()
OctoberValues=(df["arrival_date_month"]=="October").sum()
NovemberValues=(df["arrival_date_month"]=="November").sum()
DecemberValues=(df["arrival_date_month"]=="December").sum()
x = ["January","February","March","April","May","June","July","August",
     "September","October","November","December"]
y = [JanuaryValues, FebruaryValues, MarchValues, AprilValues, MayValues, JuneValues,
     JulyValues, AugustValues, SeptemberValues, OctoberValues, NovemberValues, DecemberValues]
plt.plot(x,y)
plt.title("Monthly Visitors")
plt.legend(["Visitors"])
plt.xlabel("Month")
plt.ylabel("Visitors")
plt.grid(True)
plt.tight_layout()
print("Visualisasi Data Dalam Bentuk Line Graph:")
plt.show()
print("Jadi, pengunjung paling banyak adalah Agustus")