
import pandas as pd

pd.set_option("max.rows",6)

dta=pd.read_csv("health_inspection_chi.csv")
pd.read_json("health_inspection_chi_sample.json",orient="records",lines=True,)

import request  #to read data from an online resource

print(dta.index) #0 to 25000 means 25000 visits to restaurants for health inspection
print(dta.head()) #give me the first 5 rows so i know whats going on!

dta=dta.set_index('inspection_id')
print(dta)
print(dta.head())

print(dta.address)
print(dta[['address']])

print(dta.columns)

print(dta.city)
print(dta.loc[[1965287,1329698]])

print(dta.iloc[[0,2]]) #give me the first and third record
print(dta.iloc[:5]) #give me the first 5 records
print(dta.iloc[:5,[0,5]]) #give me the first 5 rows and give me the 0th column and 5th column

dta.inspection_date=dta.inspection_date.apply(pd.to_datetime)

print(dta.info())

del dta['location'] #deleting a column from table in pandas

print(dta.violations.isnull()) #if certain values of violations column are null or not

with pd.option_context("display.max_colwidth",500):
    print(dta.violations.head())

