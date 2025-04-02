# output.py

# File Name : output.py
# Student Name: Asfia Siddiqui
# email: siddiqaf@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 4/3/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: The assignment is to evelop a VS project that accesses our SQL Server.

# Brief Description of what this module does: This module creates the output in the command prompt
# Citations: 

# Anything else that's relevant:

class Sentense():

    def get_sentense(self, description, brand, manufacturer, number_sold):
        """
        Create a descriptive sentense 
        @param description String: The product description
        @param brand String: The brand name
        @param manufacure String: The manufacurer name
        @param number_sold int: The number of item sold
        @return String: Descriptive sentense 
        """
        sentense = "The number of sold " + description + " of " + brand + " produced by "+ manufacturer + " is "+ str(number_sold)
        print(sentense)


        