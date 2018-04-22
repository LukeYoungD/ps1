
# MIT OC - CS600 - Introduction to Computer Science and Programming
# Problem Set 1: 3 Simple Problems - Problem 2 Pay off debt in 1 year
# Name: Luke Young
# Collaborators: None
# Time Spent: 00:00 (hr:min)
# 2018 04 22 19:37

# Program: Finding the minimum payment required to pay off the debt
# 
# Write a program that does the following:
# Use raw_input() to ask for the following three floating point numbers:
# 1. the outstanding balance on the credit card
# 2. annual interest rate
# 
#
# Print out the fixed minimum monthly payment, number of months
##(at most 12 and possibly less than 12) it takes to pay off the debt,
##and the balance (likely to be a negative number).
##Assume that the interest is compounded monthly according to the balance
##at the start of the month (before the payment for that month is made).
##The monthly payment must be a multiple of $10 and is the same for all months.
##Notice that it is possible for the balance to become negative
##using this payment scheme. In short:
##Monthly interest rate = Annual interest rate / 12.0
##Updated balance each month = Previous balance * (1 + Monthly interest rate)
## - Minimum monthly payment . 

balance = 0.0
apr     = 0.0
minRate  = 0.0

balance = float(raw_input("What is your current Balance? "))
apr     = float(raw_input("What is the annual interest rate as a decimal? "))

minPay    = 0.0
principle = 0.0
payTotal  = 0.0

# main algorithm
for month in range(1, 13): #runs 12 times
    if balance < 0:
        break
    
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
