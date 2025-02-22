#!/usr/bin/env python3
# -*- coding: utf-8 -*-

portion_down_payment = 0.25
current_savings = 0.0
r = 0.04
number_of_months = 0

annual_salary = float(input("Enter annual salary: "))
portion_saved = float(input("Enter portion of salary to be saved: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

downpayment = total_cost * portion_down_payment
monthly_salary = annual_salary / 12

while current_savings <= downpayment:
    current_savings += (monthly_salary * portion_saved) + (current_savings*(r/12))
    number_of_months += 1
    if number_of_months % 6 == 0:
        annual_salary = annual_salary * (1 + semi_annual_raise)
        monthly_salary = annual_salary / 12
    
print("Number of months:", number_of_months)