#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


con = None

uId = 1
uPrice = 62300 

try:
     
    con = psycopg2.connect("dbname='firstDB' user='postgres'") 
    
    cur = con.cursor()

    cur.execute("UPDATE Cars SET Price=%s WHERE Id=%s", (uPrice, uId))        
    con.commit()
    
    print "Number of rows updated: %d" % cur.rowcount
    
   

except psycopg2.DatabaseError, e:
    
    if con:
        con.rollback()
    
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()