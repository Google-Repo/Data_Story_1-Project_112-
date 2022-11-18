#all module imported here:
import csv
import statistics

import numpy as np
import pandas as pd
import plotly.express as px

#plotly graph:
df = pd.read_csv("savings_data_final.csv")
fig = px.scatter(df,y="quant_saved", color = "highschool_completed")
fig.show()

# Calculating Mean, Median and Mode:
print("Mean and Median for the Data: ")
with open("savings_data_final.csv", newline='') as f:
    reader = csv.reader(f)
    savings_data = list(reader)

savings_data.pop(0)

all_savings =[]
for data in savings_data:
    all_savings.append(float(data[0]))

print(f"Mean of Savings - {statistics.mean(all_savings)}")
print(f"Median of Savings - {statistics.median(all_savings)}")
print(f"Mode of Savings - {statistics.mode(all_savings)}")
print("")

# Calculating the standard Deviation of the Data:
print(f"Standard Deviation of all the data - {statistics.stdev(all_savings)}")

#Calculation of Data:
age = []
savings = []
for data in savings_data:
  if float(data[5]) != 0:
    age.append(float(data[5]))
    savings.append(float(data[0]))

correlation = np.corrcoef(age, savings)
print('')
print(f"Correlation between the age of the person and their savings is - {correlation[0,1]}")


