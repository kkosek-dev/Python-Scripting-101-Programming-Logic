# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 15:28:57 2023

@author: karso
"""

#Import Libraries
import os
import csv

#Save file path under budget_csv
budget_csv = os.path.join('..','Resources','budget_data.csv')

#Initialize lists and variables
total_months = 0
total_pf = 0
month_list = []
pf_list=[]
pf_raw = []
pf_cleaned=[]
change_list = []
greatest_inc =[]
greatest_dec = []

#Open file for reader
with open(budget_csv, 'r') as csvfile:
    
#Save reader function under reader
    reader = csv.reader(csvfile)
    
#Save header on csv file under csv_header
    csv_header = next(reader, None)
    
#Collect values from csv into respective lists
    for row in reader:
        
#Month & Profit/Loss list collection
        month_list.append(row[0])
        pf_list.append(int(row[1]))
        
#Calculate summations
        total_months = int(len(month_list))
        total_pf = sum(pf_list)
        
#Clean up rows to compare change values  
    pf_cleaned = [row for row in pf_list]
    pf_cleaned.pop()
    pf_raw = pf_list[1:]
    
#Zip together cleaned up columns
    avg_list = zip(pf_raw, pf_cleaned)
    
#Calculate average change in new table
    for row in avg_list:
        change_list.append(row[0] - row[1])
        
#Formula for average change across period
    average_pf = round(sum(change_list)/len(change_list),2)
    
#Clean up month_list to match change list
    month_list_clean = month_list[1:]
    
#Zip together Change with Month to find greatest Inc and Dec
    greatest_list = zip(month_list_clean, change_list)

#Loop through greatest list to pull max and min values
    for row in greatest_list:

#Conditional to find max and store under greatest_inc
        if row[1] == max(change_list):
            greatest_inc.append(row[0])
            greatest_inc.append(row[1])
            
#Conditional to find min and store under greatest_dec
        if row[1] == min(change_list):
            greatest_dec.append(row[0])
            greatest_dec.append(row[1])

#Print output to the Terminal
print("Financial Analysis")
print("---------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_pf}")
print(f"Average Change: ${average_pf}")       
print(f"Greatest Inc in Profits: {greatest_inc[0]} (${greatest_inc[1]})")
print(f"Greatest Dec in Profits: {greatest_dec[0]} (${greatest_dec[1]})")        
print("---------------------------------------------------")
    
#Create an output path for my text file
output_text = os.path.join('..','analysis','Financial_Analysis.txt')

#Open the "new" text file and fill with Financial Analysis output
with open(output_text, 'w') as text:
    text.write("Financial Analysis\n")
    text.write("---------------------------------------------------\n")
    text.write(f"Total Months: {total_months}\n")
    text.write(f"Total: ${total_pf}\n")
    text.write(f"Average Change: ${average_pf}\n")       
    text.write(f"Greatest Inc in Profits: {greatest_inc[0]} (${greatest_inc[1]})\n")
    text.write(f"Greatest Dec in Profits: {greatest_dec[0]} (${greatest_dec[1]})\n")        
    text.write("---------------------------------------------------\n")
        
