
# MIT OC - CS600 - Introduction to Computer Science and Programming
# Problem Set 1: 3 Simple Problems - Problem 1 Min Payment
# Name: Luke Young
# Collaborators: None
# Time Spent: 01:00 (hr:min)
# 2018 04 21 00:20

# Program: Finding remaining balance after minimum payment
# 
# Write a program that does the following:
# Use raw_input() to ask for the following three floating point numbers:
# 1. the outstanding balance on the credit card
# 2. annual interest rate
# 3. minimum monthly payment rate
#
# For each month, print the minimum monthly payment, remaining balance,
# principle paid in the format shown in the test cases below.
# All numbers should be rounded to the nearest penny. Finally, print the result,
# which should include the total amount paid that year and the remaining balance. 

balance = 0.0
apr     = 0.0
minRate  = 0.0

balance = float(raw_input("What is your current Balance? "))
apr     = float(raw_input("What is the annual interest rate as a decimal? "))
minRate  = float(raw_input("What is the minimum payment rate as a decimal? "))

minPay    = 0.0
principle = 0.0
payTotal  = 0.0

# main algorithm
for month in range(1, 13): #runs 12 times
    print("Month: " + str(month))
    minPay    = round((balance * minRate), 2)
    principle = round((minPay - (apr / 12 * balance)), 2)
    balance   = round((balance - principle), 2)
    payTotal += round(minPay, 2)

    print("Minimum monthly payment: " + str(minPay))
    print("Principle paid:  " + str(principle))
    print("Remaining balance: " + str(balance))
# end for loop

# print results
print("RESULT")
print("Total amount paid: " + str(payTotal))
print("Remaining balance: " + str(balance))
