import pandas as pd                                                          # importing pandas

df = pd.read_csv(r'AdminCost\adminAndInstruction_2002-2020.csv')             # Read necessary csv

cols = df.columns                                                            # save all columns to a list
numOfCols = len(cols)                                                        # save length of columns

def has_numbers(inputString):                                                # function that checks if string has any numbers
    return any(char.isdigit() for char in inputString)

colsWithNums = []                                                             
count = 0
for string in cols:                                                           # for every item in list find the ones with numbers and add it to colsWithNums 
    if has_numbers(string) == True:
        colsWithNums.insert(count, string)
        count+=1


splitAtParanth = []                       
count1 = 0
# for x in numsCols split at the ( (Instruction - Current year total (F1920_F1A)' ->     'Institutional support - Current year total ', 'F0102_F1A)   ) and add into splitAtParanth
for string in colsWithNums:                                                     # for x in list of columns with numbers split according to (
    string = string.split("(")
    splitAtParanth.insert(count1, string)
    count+=1


insideParanth = []
count2 = 1
go = len(splitAtParanth) 
# while count2 is less than the length of the splitAtParanth move them to the insideParanth list ('Institutional support - Current year total ', 'F0102_F1A)' ->  'F0102_F1A)', 'F0102_F1A)'])
while count2 < go:
    insideParanth.insert(count2, splitAtParanth[count2][1])
    count2+=1
    

splitAtUnder = []
count3 = 0
# for x in insideParanth split at the _ ( ['F0102_F1A)', 'F0102_F1A)' ->  [['F1920', 'F1A)']        ) and add into splitAtDash
for string in insideParanth:                                                     # for x in list of columns with numbers split according to _
    string = string.split("_")
    splitAtUnder.insert(count3, string)
    count+=1


numsWithF = []
count2 = 0
go = len(splitAtUnder) 
# while count2 is less than the length of the splitAtDash move them to the numsWithF list (['F1920', 'F1A)'], ['F1920', 'F1A)'] ->   ['F1920', 'F1920', 'F1920'])
while count2 < go:
    #print(split[count2][1])
    numsWithF.insert(count2, splitAtUnder[count2][0])
    count2+=1


yearsInList = []
count3 = 0
# for x in numsWithF split at the F (  ['F1920', 'F1920', 'F1920'] ->    ['', '1920'], ['', '1920'], ['', '1920']         ) and add into yearsInList
for string in numsWithF:                                                 
    string = string.split("F")
    yearsInList.insert(count3, string)
    count+=1


years = []
count2 = 0
go = len(yearsInList) 
# while count2 is less than the length of the yearsInList move them to the years list ( ['', '0102'], ['', '0102'], ['', '0102'] to    ['0102', '0102', '0102', '0203',]   )
while count2 < go:
    years.insert(count2, yearsInList[count2][1])
    count2+=1


distictYears = pd.unique(years)                             # isolate only unique years not all of them

# will be converting all unique years to only have second year (1920 to 20)
finalYears = []
count = 0
for string in distictYears:                                                    
    s1 = string[len(string)//2:]
    finalYears.insert(count, s1)


# for every year (20, 19, etc) add FY 20 to the beginning (20 -> FY 2020)
finalYears = ["FY 20" + item for item in finalYears]

# starting index's for initial calculation
startInstruction = 2        
startAcademic = 3
startInstitutional = 4

# make new df to include new columns
df2 = pd.DataFrame()

# for every year (FY 2020, FY 2019, etc) make a column that does the calculations
for x in finalYears:
    df2[x] = df.iloc[:, startInstitutional] / (df.iloc[:, startAcademic] + df.iloc[:, startInstruction])
    startAcademic +=3
    startInstitutional +=3
    startInstruction +=3

df2['Institution Name'] = df["Institution Name"]            # Add names of Institutions to df2

cols = list(df2.columns)                                    # Move last column to beginning
cols = [cols[-1]] + cols[:-1]
df2 = df2[cols]




df2.to_csv(r'Other\admin.csv')
print(df2)

print("Script is complete")

