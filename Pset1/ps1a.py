#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:33:43 2025

@author: sarahfulkerson
"""

portion_down_payment =0.25
current_savings = 0.0
r = 0.04
number_of_months = 0

annual_salary = float(input("Enter annual salary: "))
portion_saved = float(input("Enter portion of salary to be saved: "))
total_cost = float(input("Enter the cost of your dream home: "))

downpayment = total_cost * portion_down_payment
monthly_salary = annual_salary / 12

while current_savings <= downpayment:
    current_savings += (monthly_salary * portion_saved) + (current_savings*(r/12))
    number_of_months += 1
    
print("Number of months:", number_of_months)