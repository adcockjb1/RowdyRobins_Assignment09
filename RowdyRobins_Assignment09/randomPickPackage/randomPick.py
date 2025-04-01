# File Name : randomPick.py
# Student Name: Joseph Adcock
# email: adcockjb@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 4/3/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: The assignment is to develop a VS project that accesses our SQL Server.

# Brief Description of what this module does: This module creates a class that helps to pick a random row
# Citations:

# Anything else that's relevant:

import random

class RandomPick:
    def random_pick_row(self, rows):
        random_row = random.choice(rows)
        """
        Pick one random row and store each element in variables.
        @param rows list: The list where to pick a row
        @return each element from the row
        """
        valid_rows = [
            row for row in rows
            if row.ProductID and row.Description and row.ManufacturerID and row.BrandID
        ]

        if not valid_rows:
            return None  

        return random.choice(valid_rows)