#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys

con = None

def writeImage(data):
    fout = None

    try:
        fout = open('woman2.jpg','wb')
        fout.write(data)
    
    except IOError, e:    
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
        
    finally:
        
        if fout:
            fout.close()  


try:
    con = psycopg2.connect(database="firstDB", user="postgres") 
    
    cur = con.cursor()    
    cur.execute("SELECT Data FROM Images LIMIT 1")
    data = cur.fetchone()[0]
    
    writeImage(data)
    
except psycopg2.DatabaseError, e:

    print 'Error %s' % e    
    sys.exit(1)
    
finally:
    
    if con:
        con.close()  