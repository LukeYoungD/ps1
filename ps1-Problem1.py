
# MIT OC - CS600 - Introduction to Computer Science and Programming
# Problem Set 1: 3 Simple Problems - Problem 1 Min Payment
# Name: Luke Young
# Collaborators: None
# Time Spent: 00:12 (hr:min)
# 2018 04 20 23:20

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

float balance = 0.0
float apy     = 0.0
float minPay  = 0.0

balance = (float)rawinput("What is your current Balance? ")
apy     = (float)rawinput("What is the anual interest rate as a decimal? ")
minPay  = (float)rawinput("What is the minimum payment rate")
