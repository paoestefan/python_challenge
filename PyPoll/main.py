

import csv,os
voters_csv=("Resources/election_data.csv")

K_votes=0
C_votes=0
I_votes=0
O_votes=0
Total_Votes=0
K_percent=int
C_percent=int
I_percent=int
O_percent=int
Candidates=[]


with open(voters_csv,"r",encoding="utf-8") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header=next(csvreader)

    for vote in csvreader:
        Total_Votes+=1
        if vote[2] == "Khan":
            K_votes+=1
        elif vote[2]=="Correy":
            C_votes+=1
        elif vote[2]=="Li":
            I_votes+=1
        elif vote[2]=="O'Tooley":
            O_votes+=1

(K_percent)="{:.3%}".format(K_votes/Total_Votes)
(C_percent)="{:.3%}".format(C_votes/Total_Votes)
(I_percent)="{:.3%}".format(I_votes/Total_Votes)
(O_percent)="{:.3%}".format(O_votes/Total_Votes)

TV_output=(f"The total number of votes cast:{Total_Votes}")
Separador_output="---------------------------------------"
K_output=(f"Khan:{K_percent} ({K_votes})")
C_output=(f"Correy:{C_percent} ({C_votes})")
I_output=(f"Li:{I_percent} ({I_votes})")
O_output=(f"O´Tooley:{O_percent} ({O_votes})")

Votes=[K_percent,C_percent,I_percent,O_percent]

Winner_Candidate=max(Votes)
if Winner_Candidate==K_percent:
        cw="Khan"
elif Winner_Candidate==C_percent:
        cw="Correy"
elif Winner_Candidate==I_percent:
        cw="Li"
elif Winner_Candidate==O_percent:
        cw="O´Tooley"
W_output=(f'Winner:{cw}')

print(K_output)
print(C_output)
print(I_output)
print(O_output)
print(TV_output)
print(W_output)
        
output_file="Analysis/pypoll.txt"

with open (output_file,"w") as text:
    text.write(f'Election Results')
    text.write('\n')
    text.write(Separador_output)
    text.write('\n')
    text.write(TV_output)
    text.write('\n')
    text.write(K_output)
    text.write('\n')
    text.write(C_output)
    text.write('\n')
    text.write(I_output)
    text.write('\n')
    text.write(O_output)
    text.write('\n')
    text.write(Separador_output)
    text.write('\n')
    text.write(W_output)
    text.write('\n')
    text.write(Separador_output)





        




    

 

        