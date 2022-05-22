from numpy import split
import pandas as pd                                                          # importing pandas

df = pd.read_csv(r'Alumni, Age, Giving, Endowment\endowment_2003-2020.csv')             # Read necessary csv

df3 =  pd.read_csv(r'Alumni, Age, Giving, Endowment\12moFTE_2003-2020.csv')

cols = df.columns                                                            # save all columns to a list
numOfCols = len(cols)                                                        # save length of columns


df2 = pd.DataFrame()


#print(df)

colsWithNums = []                                                             
count = 0

def has_numbers(inputString):                                                # function that checks if string has any numbers
    return any(char.isdigit() for char in inputString)

colsWithNums = []                                                             
count = 0
for string in cols:                                                           # for every item in list find the ones with numbers and add it to colsWithNums 
    if has_numbers(string) == True:
        colsWithNums.insert(count, string)
        count+=1

#print(colsWithNums)



splitAtParanth = []                       
count1 = 0
# for x in numsCols split at the ( (Instruction - Current year total (F1920_F1A)' ->     'Institutional support - Current year total ', 'F0102_F1A)   ) and add into splitAtParanth
for string in colsWithNums:                                                     # for x in list of columns with numbers split according to (
    string = string.split("F")
    splitAtParanth.insert(count1, string)
    count+=1


insideParanth = []
count2 = 1
go = len(splitAtParanth) 
# while count2 is less than the length of the splitAtParanth move them to the insideParanth list ('Institutional support - Current year total ', 'F0102_F1A)' ->  'F0102_F1A)', 'F0102_F1A)'])
while count2 < go:
    insideParanth.insert(count2, splitAtParanth[count2][1])
    count2+=1

#print(insideParanth)



splitAtUnder = []
count3 = 0
# for x in insideParanth split at the _ ( ['F0102_F1A)', 'F0102_F1A)' ->  [['F1920', 'F1A)']        ) and add into splitAtDash
for string in insideParanth:                                                     # for x in list of columns with numbers split according to _
    string = string.split("_")
    splitAtUnder.insert(count3, string)
    count+=1

#print(splitAtUnder)


numsWithF = []
count2 = 0
go = len(splitAtUnder) 
# while count2 is less than the length of the splitAtDash move them to the numsWithF list (['F1920', 'F1A)'], ['F1920', 'F1A)'] ->   ['F1920', 'F1920', 'F1920'])


while count2 < go:
    #print(splitAtUnder[count2][1])
   
    numsWithF.insert(count2, splitAtUnder[count2][0])
    count2+=1


#print(numsWithF)

df2 = pd.DataFrame()


count = 0
for x in numsWithF:
    numsWithF[count] = numsWithF[count][:2] + '-' + numsWithF[count][2:]
    count+=1
print(numsWithF)







start = 2
start2 = 2
start3 = 3
count = 0
while count < 15:
    answ = df.iloc[:, start]/ ( df3.iloc[:, start2] + df3.iloc[:, start3])
    df2[numsWithF[count]] = answ
    start +=1
    start2 +=2
    start3 +=2
    count +=1



df2['Institution Name'] = df["Institution Name"]            # Add names of Institutions to df2

cols = list(df2.columns)                                    # Move last column to beginning
cols = [cols[-1]] + cols[:-1]
df2 = df2[cols]



df2.to_csv(r'Alumni, Age, Giving, Endowment\endowmentAssetsFTE.csv')
print(df2)


