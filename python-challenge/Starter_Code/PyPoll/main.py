# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 15:29:18 2023

@author: karso
"""
#Data Cleaning & Collection --------------------------

#Import dependencies
import os
import csv

#Initialize counter list
name_index = ["Charles Casper Stockham","Diana DeGette","Raymon Anthony Doane"]
vote_counter = [0 , 0 , 0]

#Save csv file path under a variable election_data
election_data = os.path.join('..', 'Resources','election_data.csv')

#Open csv for reader
with open(election_data, 'r') as csvfile:
    
#Save reader function under reader
    reader = csv.reader(csvfile)

#Take the length of the first column in the csv
    
#Skip header on csv file under csv_header
    csv_header = next(reader, None)

#Open for loop to read obtain value counts for votes
    for row in reader:

#Conditional to count Charles Casper Stockham votes
        if row[2] == "Charles Casper Stockham":
#Append to counter
            vote_counter[0] += 1
            
#Conditional to count Diana DeGette votes
        elif row[2] == "Diana DeGette":
#Append to counter
            vote_counter[1] += 1
            
#Conditional to count Raymon Anthony Doane votes            
        elif row[2] == "Raymon Anthony Doane":
#Append to counter
            vote_counter[2] += 1
            
#Open second reader to collect the column length *** Workaround for above reader not counting column length
with open(election_data, 'r') as csvfile2:
    reader2 = csv.reader(csvfile2)
    
#Skip header on csv file under csv_header
    csv_header = next(reader2, None)
    
#Take the length of the first row of the csv
    total_votes = len(next(zip(*reader2)))
    

#Saving vote percentages under respective variable names
ccs_percent = round((vote_counter[0]/total_votes)*100, 3)
dd_percent = round((vote_counter[1]/total_votes)*100, 3)
rad_percent = round((vote_counter[2]/total_votes)*100, 3)

#Save winning index to max with name index
winning_index = vote_counter.index(max(vote_counter))

#Output Design --------------------------------------
print("Election Results")
print("")
print("---------------------------------------------")
print("")
print(f"Total Votes: {total_votes}")
print("")
print("---------------------------------------------")
print("")
print(f"Charles Casper Stockham: {ccs_percent}% ({vote_counter[0]})")   
print(f"Diane Degette: {dd_percent}% ({vote_counter[1]})")
print(f"Raymon Anthony Doane: {rad_percent}% ({vote_counter[2]})")
print("")
print("---------------------------------------------")
print("")
print(f"Winner: {name_index[winning_index]}")
print("")
print("---------------------------------------------")

#Output text file design------------------------------

#Create path for new text file to write
output_text = os.path.join('..','analysis','ElectionResults.txt')

with open(output_text, 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------------------\n")
    text.write(f"Total Votes: {total_votes}\n")
    text.write("---------------------------------------------------\n")
    text.write(f"Charles Casper Stockham: {ccs_percent}% ({vote_counter[0]})\n")
    text.write(f"Diane Degette: {dd_percent}% ({vote_counter[1]})\n")       
    text.write(f"Raymon Anthony Doane: {rad_percent}% ({vote_counter[2]})\n")        
    text.write("---------------------------------------------------\n")
    text.write(f"Winner: {name_index[winning_index]}\n")
    text.write("---------------------------------------------------\n")