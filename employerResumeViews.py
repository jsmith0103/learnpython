#!/usr/bin/python
# -*- coding: utf-8 -*-
#https://docs.python.org/2/library/email-examples.html
#https://stackoverflow.com/questions/882712/sending-html-email-using-python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import psycopg2
import sys

con = None
server = None

try:

    con = psycopg2.connect(host='', database='firstDB', user='postgres')

#   get state info here
    cur = con.cursor()
    sqlstate = """SELECT *
        FROM (
            SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsCustomerService' 
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsCC'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsEmailFrom'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsErrorNotification'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsTo'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsCSContactPhone'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsProactiveContactTeamName'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'name'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'abbrev'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsAccountDisable'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsAppName'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsBCC'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsEmailBodyState01'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsEmailBodyState02'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsEmailBodyState03'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsEmailBodyState04'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsEmailBodyState05'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsEmailBodyState06'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsEmailBodyState07'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsEmailBodyState08'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsEmailBodyState09'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsEmailBodyState10'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsEmailBodyEmployer01'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsEmailBodyEmployer02'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsEmailBodyEmployer03'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsEmailBodyEmployer04'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsEmailBodyEmployer05'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsEmailBodyEmployer06'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsEmailBodyEmployer07'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsEmailBodyEmployer08'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsEmailBodyEmployer09'
            UNION SELECT vname, vvalue FROM custom.dbo.application_variables WHERE vname = 'employerResumeViewsEmailBodyEmployer10'
        ) AS AppVar
        PIVOT
        (
            MAX(vvalue)
            FOR vname IN(employerResumeViewsCustomerService, 
                employerResumeViewsCC, 
                employerResumeViewsEmailFrom, 
                employerResumeViewsErrorNotification, 
                employerResumeViewsTo, 
                employerResumeViewsCSContactPhone, 
                employerResumeViewsProactiveContactTeamName, 
                name, 
                abbrev, 
                employerResumeViewsAccountDisable, 
                employerResumeViewsAppName, 
                employerResumeViewsBCC,
                employerResumeViewsEmailBodyState01,
                employerResumeViewsEmailBodyState02,
                employerResumeViewsEmailBodyState03,
                employerResumeViewsEmailBodyState04,
                employerResumeViewsEmailBodyState05,
                employerResumeViewsEmailBodyState06,
                employerResumeViewsEmailBodyState07,
                employerResumeViewsEmailBodyState08,
                employerResumeViewsEmailBodyState09,
                employerResumeViewsEmailBodyState10,
                employerResumeViewsEmailBodyEmployer01,
                employerResumeViewsEmailBodyEmployer02,
                employerResumeViewsEmailBodyEmployer03,
                employerResumeViewsEmailBodyEmployer04,
                employerResumeViewsEmailBodyEmployer05,
                employerResumeViewsEmailBodyEmployer06,
                employerResumeViewsEmailBodyEmployer07,
                employerResumeViewsEmailBodyEmployer08,
                employerResumeViewsEmailBodyEmployer09,
                employerResumeViewsEmailBodyEmployer10)
        ) AS Vars"""
    cur.execute(sqlstate)

    row = cur.fetchone()

    if row[11] == '':
        appname = row[1]
    else:
        appname = row[11]

    bodyemployer = ''
    for x in range(23,32):
        bodyemployer += row[x]

    bodystate = ''
    for x in range(13,22):
        bodystate += row[x]

    fromaddr = row[3]
    server = smtplib.SMTP('192.168.168.11', 587)
    server.starttls()
    server.login(fromaddr, "YOUR PASSWORD")

#   get user recordset here, and process
    sqlemployer = """SELECT MAX(ervs.eriid), u.usvuserid, u.usvemail, u.usvfname, u.usvlname, COALESCE(u.usvphone1, '') AS usvphone1, COALESCE(u.usvphone2, '') AS usvphone2, c.covname, u.usiid, MAX(ervs.erdcreatedat), ISNULL(n.naics,'N/A'), ISNULL(n.title,'N/A') AS naicstitle
        FROM production.dbo.Users u
            INNER JOIN production.dbo.EmployerResumeViews ervs ON u.usiid = ervs.usiid
            LEFT JOIN production.dbo.Company c ON u.usiid = c.usiid 
            LEFT JOIN production.dbo.NAICSMain n ON c.covnaics = n.naics
        WHERE ervs.ertprocessflag = 1 AND ervs.erdprocessed IS NULL AND ervs.erdcreatedat >= DATEADD(d,-5,GETUTCDATE())
        GROUP BY u.usvuserid, u.usvemail, u.usvfname, u.usvlname, COALESCE(u.usvphone1, ''), COALESCE(u.usvphone2, ''), c.covname, u.usiid, ISNULL(n.naics,'N/A'), ISNULL(n.title,'N/A');"""
    cur.execute(sqlemployer)

    while True:

        row = cur.fetchone()

        if row == None:
            break

        userid = row[2]
        companyname = row[8]
        userfirstname = row[4]
        userlastname = row[5]

        toaddr = "ADDRESS YOU WANT TO SEND TO"
        msg = MIMEMultipart('alternative')

        msg['Subject'] = "SUBJECT OF THE MAIL"
        msg['From'] = fromaddr
        msg['To'] = toaddr

        bodyworking = bodyemployer

#        https://stackoverflow.com/questions/882712/sending-html-email-using-python
        bodytext = bodyworking
        bodyhtml = bodyworking

        part1 = MIMEText(bodytext,'plain')
        part2 = MIMEText(bodyhtml,'html')

        msg.attach(part1)
        msg.attach(part2)

        server.sendmail(fromaddr, toaddr, msg.as_string())


except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)


finally:

    server.quit()

    if con:
        con.close()
