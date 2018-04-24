
# MIT OC - CS600 - Introduction to Computer Science and Programming
# Problem Set 1: 3 Simple Problems - Problem 2 Pay off debt in 1 year
# Name: Luke Young
# Collaborators: None
# Time Spent: 00:30 (hr:min)
# 2018 04 24 02:26

# Program: Finding the minimum payment required to pay off the debt
# Using Bisection Search
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

balance = float(raw_input("What is your current Balance? "))
apr     = float(raw_input("What is the annual interest rate as a decimal? "))

boundUpper = round(((balance * (1 + (apr / 12.0)) ** 12.0) / 12.0), 2)
boundLower = round((balance / 12.0), 2)

minPay     = 0.0
principle  = 0.0
endBalance = 0.0
paid       = False

# main algorithm
while paid == False:
    tempBalance = balance
    minPay      = round(((boundUpper + boundLower) / 2), 2)

    month     = 1
    for month in range(1, 13): #runs 12 times
        
        principle = round((minPay - (apr / 12 * tempBalance)), 2)
        tempBalance   = round((tempBalance - principle), 2)

        if -0.20 < tempBalance < 0 :
            endBalance = tempBalance
            paid = True
            break
    # end for loop
    #logic for Bisection Search
    if (tempBalance > 0):
        boundLower = minPay
    else:
        boundUpper = minPay
    
    print("minPay Value: " + str(minPay))
    print("Ending balance was: " + str(tempBalance))

# end while loop

# print results
print("RESULT")
print("Monthly payment to pay off debt in 1 year: " + str(minPay))
print("Number of months needed: " + str(month))
print("Balance " + str(endBalance))
