from numpy import split
import pandas as pd                                                          # importing pandas
import fuzzymatcher

df = pd.read_csv(r'Research\nsf21314-tab020.csv' )             # Read necessary csv
df2 = pd.read_csv(r'Faculty\headcountTenure.csv' )      
dfBackup = pd.DataFrame()
dfBackup = df



cols = df.columns                                                            # save all columns to a list
numOfCols = len(cols)                                                        # save length of columns



df = df.drop(df.columns[1], axis=1)



df = df.drop(df.index[[0,1]])

i = 2
for x in range(10):
    df = df.drop(df.columns[i], axis=1)
    i+=1



new_header = df.iloc[0] #grab the first row for the header
df = df[1:] #take the data less the header row
df.columns = new_header


df3 = pd.DataFrame()



#remove all commas
df = df.replace(',','', regex=True)  



#change all values to floats
for x in df.columns:
   
    df = df.apply (pd.to_numeric, errors='coerce')
    



#removed first row
df = df.iloc[: , 1:]




unmatched_fuzzy_df = fuzzymatcher.fuzzy_left_join(CurrentTable,HERDTable,left_on=['SchoolName'],right_on=['HERDSchoolName'])






list1 = []
list2 = []
years = []
for x in df.columns:
    for y in df2.columns:
        if x == y:
            list1.append(df.columns.get_loc(x))
            list2.append(df2.columns.get_loc(y))
            years.append(x)


# add Institution column back and move to front
df['Institution'] = dfBackup.iloc[:, 0]
cols = list(df.columns)                                    # Move last column to beginning
cols = [cols[-1]] + cols[:-1]
df = df[cols]



print(df)
print(df2)




# do math
count = 0
for x in years:
    first  = df.iloc[:, list1[count]] 
    second = df2.iloc[:, list2[count]]
    df3[x] = first / second
    count+=1





df3['Institution'] = dfBackup.iloc[:, 0]

cols = list(df3.columns)                                    # Move last column to beginning
cols = [cols[-1]] + cols[:-1]
df3 = df[cols]


df3.to_csv(r'Research\totalResearchExpPerTenure.csv', index=False)
print(df3)

print("Script is complete")
