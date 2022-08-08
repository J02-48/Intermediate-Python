##SETUP
import pandas as pd
df = pd.read_csv("hotel.csv")
##SOAL 1 GAMBARAN AWAL DATA
print("\n----------- Gambaran Awal Data -----------")
print(df)
input("Ketik apapun untuk melanjutkan:")
##SOAL 2 PROPERTIES DATA
print("\n----------- Missing Data -----------")
print(df.isna().sum())
input("Ketik apapun untuk melanjutkan:")
print("\n----------- Data Types-----------")
print(df.dtypes)
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
input("Ketik apapun untuk melanjutkan:")
print("\n----------- Median -----------")
print(MedianValues)
input("Ketik apapun untuk melanjutkan:")
print("\n----------- Standar Deviasi -----------")
print(StdValues)
input("Ketik apapun untuk melanjutkan:")
print("\n----------- Mean -----------")
print(MeanValues)
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
input("Ketik apapun untuk melanjutkan:")
print("\n----------- Minimum -----------")
print(MinValues)
input("Ketik apapun untuk melanjutkan:")
##SOAL 5 MENYELESAIKAN MASALAH MISSING VALUE
perc = 50
min_count = int(((100-perc)/100)*df.shape[0]+1)
df = df.dropna(axis=1, thresh=min_count)
print("\n----------- Jumlah Missing Value Setelah Drop -----------")
print(df.isna().sum())
input("Ketik apapun untuk melanjutkan:")
for column in df.columns:
    df["country"].fillna(df["country"].mode()[0], inplace=True)
    df["children"].fillna(df["children"].mode()[0], inplace=True)
df["agent"].fillna(int(df["agent"].mean()), inplace=True)
print("\n----------- Semua Missing Value Sudah Terisi -----------")
print(df.isna().sum())

