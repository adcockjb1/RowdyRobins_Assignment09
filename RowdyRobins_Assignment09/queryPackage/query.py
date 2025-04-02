# query.py

# File Name : query.py
# Student Name: Kengo Ishizuka
# email: ishizuko@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 4/3/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: The assignment is to develop a VS project that accesses our SQL Server.

# Brief Description of what this module does: This module creates some query statements.
# Citations: 

# Anything else that's relevant:

class Query:
    def query_manufacurer(self, manufacure_id):
        """
        Create a query statement for manufacturer name
        @param manufacure_id int: The manufacure_id of desired manufacturer
        @return Query statement
        """
        manufacure_qurey_stetement = 'SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = ' + str(manufacure_id)
        return manufacure_qurey_stetement


    def query_brand(self, brand_id):
        """
        Create a query statement for brand name
        @param brand_id int: The brand_id of desired brand
        @return Query statement
        """
        brand_qurey_stetement = 'SELECT Brand FROM tBrand WHERE BrandID = ' + str(brand_id)
        return brand_qurey_stetement

    def query_number_sold(self, product_id):
        """
        Create a query statement for the number of sold of a product
        @param product_id int: The product_id of desired product
        @return Query statement
        """
        number_sold_qurey_stetement = 'SELECT TOP (100) PERCENT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold FROM dbo.tTransactionDetail INNER JOIN dbo.tTransaction ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID WHERE (dbo.tTransaction.TransactionTypeID = 1) AND (dbo.tTransactionDetail.ProductID = ' + str(product_id) + ')'
        return number_sold_qurey_stetement


