Die_A = [1,2,3,4,5,6]
Die_B = [1,2,3,4,5,6]
# Original Dice
print("Original Dice A =", Die_A)
print("Original Dice B =", Die_B)
print("\nProbability of Original Dice :\n")

total_combinations = len(Die_A) * len(Die_B)
# Probability of all Possible Sums occurring among the number of combinations from two original dice ( DieA and DieB)
original_sums = {}
for i in range(len(Die_A)):
    for j in range(len(Die_B)):
        sums = Die_A[i] + Die_B[j]
        count = original_sums.get(sums,0)+1
        original_sums[sums] = count

for sums,count in original_sums.items():
    print("P(Sum = ",sums,") Count =",original_sums[sums],"Probability = ",count,"/",total_combinations,"=",round(count/total_combinations,2))
   
new_sums = original_sums

diceA = []
diceB = []

# DiceA Probability
def diceA_possibility(number,t):    
    if number > 4:
        return
    if len(t) > 6:
        return
    if len(t) == 6:
        if t not in diceA:
            diceA.append(t)
        return
    for i in range(number,5):          
        diceA_possibility(i,t.copy() + [i])

# DiceB Probability
def diceB_possibility(number,t):
    if number > 11:
        return
    if len(t) > 6:
        return
    if len(t) == 6:
        if t not in diceB:
            diceB.append(t)
        return
    for i in range(number+1,13):   
        diceB_possibility(i,t.copy()+[i])

# Probability of all Possible Sums occurring among the number of combinations from two new dice ( DiceA and DiceB)

def undoom_dice():
    for i in range(1,5):
        diceA_possibility(i,[i])
    for j in range(1,12):
        diceB_possibility(j,[j])
    for i in diceA:
        for j in diceB:
            temp_dict = {}
            for k in range(len(i)):
                for l in range(len(j)):
                    sums=i[k]+j[l]
                    count = temp_dict.get(sums,0)+1
                    temp_dict[sums] = count           
            mc = 0
            for sums,count in temp_dict.items():
                Original_count=new_sums.get(sums,-1)
                if count==Original_count:
                    mc+=1
            if mc == 11:
                return i,j,temp_dict
                
New_Die_A,New_Die_B,new_temp_dict = undoom_dice()

print("\nNew Dice A = ",New_Die_A)
print("New Dice B = ",New_Die_B)
print("\nProbability of New Dice :\n")

for key,count in new_temp_dict.items():
    print("P(Sum = ",key,") Count =",original_sums[key],"Probability = ",count,"/",total_combinations,"=",round(count/total_combinations,2))
