
import os
import csv

budget_csv=("Resources/budget_data.csv")

Date=[]
ProfitLoss=[]
average=0

with open(budget_csv,"r") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header=next(csvreader) 
  #* The total number of months included in the dataset
    for row in csvreader:
        Date.append(row[0])
        Totalmonths=len(Date)

  #* The net total amount of "Profit/Losses" over the entire period
        ProfitLoss.append(int(row[1]))
        Totalproloss=sum(ProfitLoss)

  #* The average of the changes in "Profit/Losses" over the entire period
        change=round(((int(row[1])-867884)/Totalmonths),2)
        
  #* The greatest increase in profits (date and amount) over the entire period
    
        greatest_increase=max(ProfitLoss)
         

 #* The greatest decrease in losses (date and amount) over the entire period
        greatest_decrease=min(ProfitLoss)
        rowlow=ProfitLoss.index(greatest_decrease)

print(Totalmonths)
print(Totalproloss)
print(change)
print((greatest_increase))
print(greatest_decrease)
print(rowlow)

output_file="Analysis/pybank.txt"

with open (output_file,"w") as text:
    text.write(f"Total months : {Totalmonths}"'\n')
    text.write(f"Total:{Totalproloss}"'\n')
    text.write(f"Average change : {change}"'\n')
    text.write(f"Greatest increase in profits:{greatest_increase}"'\n')
    text.write(f"Greatest decrease in losses:{greatest_decrease}"'\n')

    



  

