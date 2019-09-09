import pandas as pd
import matplotlib as plt

df = pd.read_csv("datos/iris.csv")

print(df.columns)

print(df.head(3))

print(df[u'Sepal.Length'].head(3))

print("Media: " + str(df[u'Sepal.Length'].mean()))
print("Standard deviation: " + str(df[u'Sepal.Length'].std()))
print("Kurtosis: " + str(df[u'Sepal.Length'].kurtosis()))
print("Skewness: " + str(df[u'Sepal.Length'].skew()))

df[u'Sepal.Length'].plot.hist()

