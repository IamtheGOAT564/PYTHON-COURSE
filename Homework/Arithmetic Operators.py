team1 = 85
team2 = 90
team3 = 78
team4 = 92
team5 = 80


total_points = team1 + team2 + team3 + team4 + team5
average_points = total_points / 5

print("Total Points:", total_points)
print("Average Points per Team:", average_points)


stars_per_point = 2
total_stars = total_points * stars_per_point

print("Total Reward Stars:", total_stars)


full_boxes = total_stars // 25
leftover_stars = total_stars % 25

print("Full Boxes of 25 Stars:", full_boxes)
print("Leftover Stars:", leftover_stars)

last_week = 400

print("Did we score higher than last week?", total_points > last_week)
print("Did we score the exact same as last week?", total_points == last_week)
print("Did we score at least as much as last week?", total_points >= last_week)


total_points += 15  
print("Total after adding bonus points:", total_points)

total_points -= 5
print("Total after subtracting missed-task points:", total_points)