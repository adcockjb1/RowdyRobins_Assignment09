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
# Citations:

# Anything else that's relevant:


from databaseManagementPackage.databaseManagement import *
from randomPickPackage.randomPick import *
from queryPackage.query import *


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

# Question3,4
qrl = Query()
manufacure_qurey_stetement = qrl.query_manufacurer(manufacturer_id)
manufacturer = dbm.submit_sql_to_server(conn, manufacure_qurey_stetement)
manufacturer = manufacturer.fetchall()[0][0]

# Question5
brand_qurey_stetement = qrl.query_brand(brand_id)
brand = dbm.submit_sql_to_server(conn, brand_qurey_stetement)
brand = brand.fetchall()[0][0]

# Question6
number_sold_qurey_stetement = qrl.query_number_sold(product_id)
number_sold = dbm.submit_sql_to_server(conn, number_sold_qurey_stetement)
number_sold = number_sold.fetchall()[0][0]

