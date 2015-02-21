__author__ = 'georgev'


import csv

with open('Data.csv','rb') as csvfile:
    spamreader= csv.reader(csvfile,delimiter=',')
    for row in spamreader:
        print (row[0],row[1])

