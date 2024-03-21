#How many total combinations are possible? Show the math along with the code!
num_sides = 6
total_combinations = num_sides ** 2
print("Total combinations when two dice are rolled:", total_combinations)

#Calculate and display the distribution of all possible combinations that can beobtained 
#when rolling both Die A and Die B together. Show the math along with the code!
distribution=[[0] * 6 for _ in range(6)]
for combination in range(total_combinations):
    die_a  = combination // 6 + 1;
    die_b  = combination % 6 + 1;
    distribution[die_a-1][die_b-1] = (die_a,die_b)
print("\nDistribution of all possible combinations:")
for row in distribution:
    print(row)

#Calculate the Probability of all Possible Sums occurring among the number of
#combinations from (2).
for sums in range(2, 13):
    print("\n")
    count=0
    for combination in range(total_combinations):
        die_a  = combination // 6 + 1;
        die_b  = combination % 6 + 1;
        if die_a+die_b==sums:
            print("(",die_a,",",die_b,")")
            count+=1
    probability=count/total_combinations
    print(f"P(Sum = {sums})  :   {count}/{total_combinations} = {probability:.2f}")
   
