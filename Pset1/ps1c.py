#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 20:45:28 2025

@author: sarahfulkerson
"""

semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
total_cost = 1000000
current_savings = 0.0
number_of_months = 36
downpayment = total_cost * portion_down_payment

starting_salary = float(input("Enter the starting salary: "))

epsilon = 1
number_of_guesses = 0
low = 0
high = 10000
guess = (high + low)//2

while abs(low - high) > epsilon:
    annual_salary = starting_salary
    monthly_salary = annual_salary / 12
    current_savings = 0.0
    
    for n in range(number_of_months):
        current_savings += (monthly_salary * (guess/10000)) + (current_savings*(r/12))
        if (n + 1) % 6 == 0:
            annual_salary = annual_salary * (1 + semi_annual_raise)
            monthly_salary = annual_salary / 12
    
    if abs(current_savings - downpayment) <= 100:
        break
    elif current_savings < downpayment:
        low = guess
    else:
        high = guess
    
    guess = (high + low)//2
    number_of_guesses += 1

if abs(current_savings - downpayment) < 100:
    print("Best savings rate:", guess/10000)
    print("Steps in bisection search:", number_of_guesses)
else:
    print("It is not possible to pay the down payment in three years.")
