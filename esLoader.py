# coding: utf-8
import csv
import json
import os
 
count = 0
f = open('passwords.csv', 'r')
reader = csv.DictReader( f, delimiter = '|', fieldnames = ( 'password','hash' ) )

for row in reader:
    out = json.dumps( row )
    # print out
    count = count + 1
    # print ("""curl -XPUT http://localhost:9200/rainbow/hash/""" + str(count) + """ -d '"""+ out + """ '""")
    os.system ("""curl -XPUT http://localhost:9200/rainbow2/hash/""" + str(count) + """ -d '"""+ out + """ '""")

f.close()