field1= 75
field2= 90
field3= 120
field4= 135
field5= 150
sum=field1+field2+field3+field4+field5
average=sum/5
print(sum)
print(average)
price_per_kg=15
earnings=sum*15
print(earnings)
bags=sum//25
leftover=sum%25
print(bags)
print(leftover)
last_year = 500
print("Better than last year?  :", sum > last_year)
print("Same as last year?      :", sum == last_year)
print("At least as good?       :", sum >= last_year)
total += 30
print("After bonus crop   :", total, "kg")

# Subtract 15 kg saved as seeds for next season
total -= 15
print("After seed reserve :", total, "kg")

# Final bag count after all adjustments
bags = total // 25
print("Final bags packed  :", bags)