#Get the total
total = float(input("How much is the bill? ")) 

#Get the number of people spliting the bill
num_of_ppl_paying = float(input("How many people are splitting the bill? "))

#Decide how much you want to tip
percent_tip = float(input("How much do you want to tip? (15, 20, or 22 percent) "))

#Calculate the tip
cost_per_person = round(total/num_of_ppl_paying*(1 + percent_tip/100), 2)

#print the result
print("Your cost is " + str(cost_per_person))