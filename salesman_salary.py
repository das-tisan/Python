#!/usr/bin/env python

basic_salary=1500
bonus_rate=200
commission_rate=0.02

numbers_of_camera = int(input("Enter the number of inputs sold: "))
price = float(input("Enter the total prices: "))

bonus = bonus_rate*numbers_of_camera
commission = commission_rate*numbers_of_camera*price

print("Bonus = %6.2f" %bonus)
print("Commission = %6.2f" %commission) 
print("Gross Salary = %6.2f" %(basic_salary+bonus+commission))