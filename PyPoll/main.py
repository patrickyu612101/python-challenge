import os
import csv
import pandas as pd

text_file = open("Output.txt", "w")

election_data = os.path.join("Resources", "election_data.csv")
#pdFile= pd.read.csv(election_data,"encoding="ISO-8859-1")
pdFile= pd.read_csv(election_data)  #read the data with pandas
total=pdFile["Voter ID"].count()    # get total votes

listCandidate= pdFile["Candidate"].unique()   #get candidates with votes
len=listCandidate.size  #get size of candidates
listvotes=pdFile["Candidate"].value_counts() # also use this to calculate
winner=""
winnervote=0


print("Election Results")
text_file.write("Election Results\n")
print("------------")
text_file.write("------------\n")
print("Total votes: "+str(total))
text_file.write("Total votes: "+str(total)+"\n")
print("------------")
text_file.write("------------\n")
i = 0
for i in range(len) :   #test range is only in how much candidate, 
    percent= listvotes[i]/total *100    #find the percent
    percent=percent.round()
    if listvotes[i]>winnervote: #find the winner 
        winnervote=listvotes[i]
        winner = listCandidate[i]

    print(listCandidate[i]+" : "+str(listvotes[i])+" votes  ("+str(percent)+"%)")   #print the result by use the same index so I can add string between
    text_file.write(listCandidate[i]+" : "+str(listvotes[i])+" votes  ("+str(percent)+"%)\n")

print("------------")
text_file.write("------------\n")
print("Winner is : "+ winner)
text_file.write("Winner is : "+ winner+"\n")
print("------------")
text_file.write("------------\n")


text_file.close()