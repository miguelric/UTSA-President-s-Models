import pandas as pd                                                          # importing pandas

df = pd.read_csv(r'Enrollment\fallEnrollment_2004-2020.csv')             # Read necessary csv

cols = df.columns                                                            # save all columns to a list
numOfCols = len(cols)                                                        # save length of columns

print(df)

df2 = pd.DataFrame()


df2["Total Enrollment"] = df["Institution Name"]


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
    

#print(insideParanth)


splitAtUnder = []
count3 = 0
# for x in insideParanth split at the _ ( ['F0102_F1A)', 'F0102_F1A)' ->  [['F1920', 'F1A)']        ) and add into splitAtDash
for string in insideParanth:                                                     # for x in list of columns with numbers split according to _
    string = string.split("F")
    splitAtUnder.insert(count3, string)
    count+=1


numsWithF = []
count2 = 0
go = len(splitAtUnder) 
# while count2 is less than the length of the splitAtDash move them to the numsWithF list (['F1920', 'F1A)'], ['F1920', 'F1A)'] ->   ['F1920', 'F1920', 'F1920'])
while count2 < go:
    #print(split[count2][1])
    numsWithF.insert(count2, splitAtUnder[count2][1])
    count2+=1

print(numsWithF)




yearsInList = []
count3 = 0

# for x in numsWithF split at the F (  ['F1920', 'F1920', 'F1920'] ->    ['', '1920'], ['', '1920'], ['', '1920']         ) and add into yearsInList
for string in numsWithF:                                         
    string = string.split("_")
    yearsInList.insert(count3, string)
    count+=1


years = []
count2 = 0
go = len(yearsInList) 
# while count2 is less than the length of the yearsInList move them to the years list ( ['', '0102'], ['', '0102'], ['', '0102'] to    ['0102', '0102', '0102', '0203',]   )
while count2 < go:
    years.insert(count2, yearsInList[count2][0])
    count2+=1




years2 = []
count2 = 0
for string in years:
    string = string.split("R")
    years2.insert(count2,string)
    count2+=1



years3 = []
count2 = 0
go = len(years2) 
# while count2 is less than the length of the yearsInList move them to the years list ( ['', '0102'], ['', '0102'], ['', '0102'] to    ['0102', '0102', '0102', '0203',]   )
for x in years2:
    try:
        years3.insert(count2, years2[count2][1])
        count2+=1
    except:
        years3.insert(count2, years2[count2][0])
        count2+=1




years4 = []
count2 = 0
for string in years3:
    string = string.split(")")
    years4.insert(count2, string)
    count2+=1

print(years4)



finalYearsCols = []
count2 = 0
go = len(years4) 
# while count2 is less than the length of the yearsInList move them to the years list ( ['', '0102'], ['', '0102'], ['', '0102'] to    ['0102', '0102', '0102', '0203',]   )
while count2 < go:
    finalYearsCols.insert(count2, years4[count2][0])
    count2+=1

print(finalYearsCols)
reversed_list = finalYearsCols[::-1]
print(reversed_list)

start = 2
for x in reversed_list:
    df2[x] = df.iloc[:, start]
    start+=1

print(df2)

df2.to_csv(r'Enrollment\totalEnrollment.csv')
print(df2)

 