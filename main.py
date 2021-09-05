import random

# input the number of people at the party
num_of_people = int(input("Number of people at the party: "))

ppl_dic = {}
# input their names respectively
for i in range(0, num_of_people):
    ppl_dic[i] = input(f"Name of person {str(i+1)}: ")

# input the total bill amount
bill_amount = int(input("Total bill amount: "))

# pick lucky person randomly
lucky_person = random.randint(0, num_of_people)

# split the bill equally
pay_each = bill_amount/num_of_people

# reduce 50% from lucky one and add equally to others
lucky_amount = pay_each - ((50*pay_each)/100)

pay_each = pay_each + (((50*pay_each)/100)/(num_of_people-1))

# Print the bill

for i in range(0, num_of_people):
    if i != lucky_person:
        print(f"{ppl_dic[i]}: {str(pay_each)}")
    else:
        print(f"{ppl_dic[lucky_person]}: {str(lucky_amount)}")