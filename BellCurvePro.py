import statistics
import plotly.figure_factory as ff 
import pandas as pd 
import csv 

df = pd.read_csv('data.csv')
Avg =  df["Avg Rating"].tolist()
median = statistics.median(Avg)
mean = statistics.mean(Avg)
mode = statistics.mode(Avg)
fig = ff.create_distplot([df["Avg Rating"].tolist()],["Average Rating Of Mobile Brands"])
print(median)
print(mean)
print(mode)
fig.show()
