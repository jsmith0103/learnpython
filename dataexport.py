#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


con = None
fout = None


try:
     
    con = psycopg2.connect(database='firstDB', user='postgres') 
    
    cur = con.cursor()
    fout = open('cars', 'w')
    cur.copy_to(fout, 'cars', sep="|")                        
   

except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)

except IOError, e:    
    print 'Error %s' % e   
    sys.exit(1)
    
finally:
    
    if con:
        con.close()

    if fout:
        fout.close() 