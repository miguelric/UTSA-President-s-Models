from numpy import split
import pandas as pd                                                          # importing pandas

df = pd.read_csv(r'Research\nsf21314-tab020.csv' )             # Read necessary csv

cols = df.columns                                                            # save all columns to a list
numOfCols = len(cols)                                                        # save length of columns

print(cols)
df2 = pd.DataFrame()

print(df)

df = df.drop(df.columns[1], axis=1)
print(df)


df = df.drop(df.index[[0,1]])

i = 2
for x in range(10):
    df = df.drop(df.columns[i], axis=1)
    i+=1


new_header = df.iloc[0] #grab the first row for the header
df = df[1:] #take the data less the header row
df.columns = new_header




df.to_csv(r'Research\totalResearchExp.csv', index=False)
print(df)

print("Script is complete")
