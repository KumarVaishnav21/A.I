## Read lines
# # 1st Method
f = open("E:\\2 - Week 3 and 4 Beginners Python\\3 - Python Basics\\10 - File Handling\\funny.txt", "r")
for line in f:
    print(line)
f.close()

# 2nd Method(Automatically closes the file)
with open("E:\\2 - Week 3 and 4 Beginners Python\\3 - Python Basics\\10 - File Handling\\funny.txt", "r") as f:
    for line in f:
        print(line)

    
#  3rd Method
with open("E:\\2 - Week 3 and 4 Beginners Python\\3 - Python Basics\\10 - File Handling\\funny.txt", "r") as f:
    lines = f.readlines()
    print(lines)


## Write lines
# 1st Method
with open("E:\\2 - Week 3 and 4 Beginners Python\\3 - Python Basics\\10 - File Handling\\1love.txt", "w") as f:
    f.write("I python python programming..1stwrite line testing")

# 2nd Method
with open("E:\\2 - Week 3 and 4 Beginners Python\\3 - Python Basics\\10 - File Handling\\1love.txt", "w") as f: 
     f.writelines([
         "I love Fortran\n",
         "I love pascal\n",
         "I love mainframe\n"
     ])
    
## Append lines
# 1st Method    
with open("E:\\2 - Week 3 and 4 Beginners Python\\3 - Python Basics\\10 - File Handling\\1love.txt", "a") as f: 
    f.write("\nI python AI Engineering programming..2ndwrite line testing")
    
# 2nd Method
with open("E:\\2 - Week 3 and 4 Beginners Python\\3 - Python Basics\\10 - File Handling\\1love.txt", "a") as f: 
     f.writelines([
         "I love Fortran",
         "I love pascal",
         "I love mainframe"
     ])


## Cricket Scores
player_scores = {}
with open("E:\\A.I\\2 - Week 3 and 4 Beginners Python\\3 - Python Basics\\10 - File Handling\\scores.csv", "r") as f:
    for line in f:
        player, score = line.split(',')
        score = int(score)
        if player in player_scores:
            player_scores[player].append(score)
        else:
            player_scores[player] = [score]
        
#print(player_scores)       

for player, score_list in player_scores.items():
    print(player, score_list)
    min_score = min(score_list)
    max_score = max(score_list)
    avg_score = sum(score_list)/len(score_list)
    
    print(f'{player} ==> Min: {min_score}, Max: {max_score}, Avg: {avg_score}') 
    