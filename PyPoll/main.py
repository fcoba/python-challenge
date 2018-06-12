import os
import csv

total_votes = {}

poll1 = csv.reader(open('election_data_1.csv'), delimiter=",")
next(poll1, None) 
for row in poll1:
    candidate = row[2]
    if  candidate in total_votes.keys(): 
        total_votes[candidate] = total_votes[candidate] + 1
    else:
        total_votes[candidate]=1

poll2 = csv.reader(open('election_data_2.csv'), delimiter=",")
next(poll2, None) 
for row in poll2:
    candidate = row[2] 
    if  candidate in total_votes.keys(): 
        total_votes[candidate] = total_votes[candidate] + 1
    else:
        total_votes[candidate]=1
        
tv = total_votes.values()

vk = total_votes.keys()

candidates_with_votes = 'The complete list of candidates who received votes are: \n' + '\n'.join(list(total_votes.keys()))
print(candidates_with_votes)

for candidate in list(vk):
    Vv = total_votes[candidate]/sum(list(tv))*100
    percent_votes = 'The percentage of votes ' + candidate + ' won is ' + str(round(Vv, 2)) + '%' + ', and the total number of votes ' + candidate + ' got is ' + str(total_votes[candidate])
    print(percent_votes)

vklist = list(vk)
tvlist = list(tv)

winner = 'The winner of the election based on popular vote is ' + str(vklist[tvlist.index(max(tvlist))]) + ', with ' + str(max(tvlist)) + ' votes'
print(winner) 

Data_File = open('Poll_Results.txt', "w")
Data_File.write(candidates_with_votes + "\n")
Data_File.write(percent_votes + "\n")
Data_File.write(winner + "\n")
Data_File.close()
