#!/usr/bin/env python
# coding: utf-8

# # BMI CALCULATOR 
# The purpose of this project is to create a BMI Calculator using python programming language and by referencing: https://mercer-health.com/services/weight-management-center/bmi-calculator
# 
# BMI is calculated by the following formula: (weight in pounds x 703) / (height in inches x height in inches).
# 
# The BMI classifies individuals from obese to underweight based on the following metrics: 
# 
#     BMI Score     Classification      Health Risk
#     Under 18.5      Underweight	      Minimal 
#     18.5 - 24.9     Normal Weight        Minimal 	
#     25 - 29.9	   Overweight	       Increased 
#     30 - 34.9	   Obese	            High 
#     35 - 39.9	   Severely Obese	   Very High 
#     40 and over     Morbidly Obese	   Extremely High 

# In[38]:


# Create name, weight and heigh inputs 

first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

name = first_name + ' ' + last_name

weight = int(input('Enter your weight in pounds: '))

height = int(input('Enter your height in inches: '))

# Introduce BMI Formula
BMI = (weight * 703)/ (height * height)
print(name +', your BMI is: ' + str(BMI))

# create an if statement for BMI classification metrics
if BMI > 0: 
    if (BMI < 18.5): 
        print(name + ', you are underweight with minimal health risk.')
    elif (BMI <= 24.9): 
        print(name + ', you are normal weight with minimal health risk.')
    elif (BMI < 29.9): 
        print(name + ', you are overweight with an increased health risk.')
    elif (BMI < 34.9): 
        print(name + ', you are obese with a high health risk.')
    elif (BMI < 39.9): 
        print(name + ', you are severely obese with a very high health risk.')
    else: 
        print(name + ', you are morbidly obese with an extremely high health risk.')
else: 
    print('Please enter valid input')


# In[ ]:




