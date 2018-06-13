#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Citroen', 21000),
    (7, 'Hummer', 41400),
    (8, 'Volkswagen', 21600)
)

con = None

try:
     
    con = psycopg2.connect("dbname='firstDB' user='postgres'")   
  
    cur = con.cursor()  
    
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT PRIMARY KEY, Name TEXT, Price INT)")
    query = "INSERT INTO Cars (Id, Name, Price) VALUES (%s, %s, %s)"
    cur.executemany(query, cars)
        
    con.commit()
    

except psycopg2.DatabaseError, e:
    
    if con:
        con.rollback()
    
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()