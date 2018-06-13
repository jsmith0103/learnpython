#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


con = None

try:
     
    con = psycopg2.connect(database='firstDB', user='postgres') 
    
    cur = con.cursor() 

    cur.execute("DROP TABLE IF EXISTS Friends")
    cur.execute("CREATE TABLE Friends(Id serial PRIMARY KEY, Name VARCHAR(10))")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Tom')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Jim')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Robert')")
    
    #con.commit()
       
except psycopg2.DatabaseError, e:
    
    if con:
        con.rollback()
        
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()