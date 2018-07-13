import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")
total_month=0
total_Revenue=0
maxN=0
maxdate=""
minN=0
mindate=""
averageAll=0
averageCount=0
previous=0
# Open and read csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csvreader:
        total_month=total_month+1   #calculate the total month
        total_Revenue=total_Revenue+int(row[1]) 
        averageCount=averageCount+1     # get the total row without header
        if previous != 0:   #check if it is at start row
            averageAll=averageAll+(int(row[1])-previous)
        
        if (int(row[1])-previous)>maxN: # get max and min number from change
            maxN=int(row[1])-previous
            maxdate=row[0]
        elif (int(row[1])-previous)<minN:
            minN = int(row[1])-previous
            mindate=row[0]
        previous = int(row[1])  #save the value for next run of loop to get the previous value


print("The total moth is : "+str(total_month))  
print("The total revenue is : "+str(total_Revenue))
#print(str(averageAll))
print("The Average Change is : "+str(averageAll/averageCount))
print("The Greatest increase is at "+maxdate+" : "+str(maxN))
print("The Greatest decrease is at "+mindate+" : "+str(minN))

