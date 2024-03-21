num_sides = 6
total_combinations = num_sides ** 2
print("Total combinations when two dice are rolled:", total_combinations)


def undoom_dice(die_a, die_b):
    a = [min(4, spots) for spots in die_a]
    b = [min(6, spots) for spots in die_b]
    return a, b
die_a = [1, 2, 3, 4, 5, 6]
die_b = die_a
new_die_a, new_die_b = undoom_dice(die_a, die_b)
print("")
print(" Modified Values of the dice      ")
print("\nNew Die A:", new_die_a)
print("New Die B:", new_die_b)


distribution = [[0] * 6 for _ in range(6)]
for i in range(len(new_die_a)):
    for j in range(len(new_die_b)):
        distribution[i][j] = (new_die_a[i] , new_die_b[j])
print("Distribution of combinations:")
for row in distribution:
    print(row)
    
    
for sums in range(2, 13):
    print("\n")
    count=0
    for j in range(len(new_die_b)):
        for i in range(len(new_die_a)):
            distribution[i][j] = (new_die_a[i] + new_die_b[j])
            if distribution[i][j]==sums:
                print("(",new_die_a[i],",",new_die_b[j],")")
                count+=1
    probability=count/total_combinations
    print(f"P(Sum = {sums})  :   {count}/{total_combinations} = {probability:.2f}")
