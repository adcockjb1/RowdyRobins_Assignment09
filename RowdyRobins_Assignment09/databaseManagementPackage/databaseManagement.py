# File Name : databaseManagement.py
# Student Name: Joseph Adcock
# email: adcockjb@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 4/3/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: The assignment is to develop a VS project that accesses our SQL Server.

# Brief Description of what this module does: This module creates a class that connects with our database
# Citations:

# Anything else that's relevant:

import pyodbc

class DatabaseManagement:
    def connect_to_database(self):
        """
        Connect to our SQL Server instance
        @return the connection object or None on failure
        """
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                                  'Database=GroceryStoreSimulator;'
                                  'uid=IS4010Login;'
                                  'pwd=P@ssword2;')
        except:
                return None
        return conn

    def submit_sql_to_server(self, conn, sql_statement):
        """
        Submit a SQL statement to our SQL Server
        @param conn connection object: The connection object
        @param sql_statement String: The SQL to submit
        @return The pyodbc cursor object that contains the query results
        """
        cursor = conn.cursor()
        cursor.execute(sql_statement) 
        return cursor