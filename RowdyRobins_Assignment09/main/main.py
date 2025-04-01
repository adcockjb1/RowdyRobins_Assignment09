# File Name : main.py
# Student Name: Asfia Siddiqui
#               Joseph Adcock
#               Kengo Ishizuka
# email: siddiqaf@mail.uc.edu
#        adcockjb@mail.uc.edu
#        ishizuko@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 4/3/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: The assignment is to develop a VS project that accesses our SQL Server.

# Brief Description of what this module does: This module completes the question requirments outlined in the assignment details
# Citations: ChatGPT

# Anything else that's relevant:


from databaseManagementPackage.databaseManagement import *
from randomPickPackage.randomPick import *


dbm = DatabaseManagement()
conn = dbm.connect_to_database()
# Question1
cursor = dbm.submit_sql_to_server(conn, 'SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID  FROM tProduct')

# Question2
rows = cursor.fetchall()
rnd = RandomPick()
random_row = rnd.random_pick_row(rows)
product_id = random_row.ProductID
description = random_row.Description
manufacturer_id = random_row.ManufacturerID
brand_id = random_row.BrandID