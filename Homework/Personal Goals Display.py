# ================================
# PERSONAL GOALS DISPLAY
# ================================

# ---------- PART 1: import the keyword module ----------
import keyword


# ---------- PART 2: ask the three questions ----------
# YOUR CODE HERE
# Use input() three times and store each answer in its own variable:
person_name=input("Enter Your Name:")  
goal_name=input("One skill that you want to get better at:")
target_month=input("Month you want to achieve this goal:")
daily_practice=input("Time for practice each day:")


# ---------- PART 3: store the practice time ----------



# ---------- PART 4: the heading ----------
print("\nMY PERSONAL GOAL PLAN")


# ---------- PART 5: the four plan lines ----------
# YOUR CODE HERE
# Four print() statements, each with a label and a variable separated by a comma:
print("Name:",person_name)
print("Goal:",goal_name)
print("Target Month:",target_month)
print("Daily Practice:",daily_practice)

# ---------- PART 6: two lines that join up ----------
print("Status: Not Started", end=" ")
print("Reminder:Practice EVERY DAY!")


# ---------- PART 7: the sentence and the keywords ----------
print("Your name is",person_name,"and you are working on",goal_name,"which you think will be accomplished by",target_month,"by practicing for",daily_practice,"every day.")
print(keyword.kwlist)