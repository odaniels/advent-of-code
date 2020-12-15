spoken = {n: t + 1 for t, n in enumerate([16,1,0,18,12,14,19])}
next_num = 0
for turn in range(len(spoken) + 1, 30000000): # 2020 for PART 1
    spoken[next_num], next_num = turn, turn - spoken.get(next_num, turn)
print("PART 2:", next_num)