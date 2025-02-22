#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 20:45:28 2025

@author: sarahfulkerson
"""

semi_annual_raise = 0.07
r = 0.04
total_cost = 1000000
downpayment = total_cost * 0.25

annual_salary = float(input("Enter annual salary: "))

current_savings = 0.0
number_of_months = 36
max_savings_rate = 10000
low = 0
high = max_savings_rate
epsilon = 1
guess = (high + low)/2.0
steps_in_bisection_search = 0

while abs(guess - high) >= epsilon:
    
    
    guess = (high + low)/2.0
    steps_in_bisection_search += 1
    
    
print("Number of months:", number_of_months)