# coding: utf-8
import csv
import ipaddress

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

location_file = "GeoLite2-Country-Locations-en.csv"
blocks_file = "GeoLite2-Country-Blocks-IPv4.csv"

if ( len(sys.argv) > 2 ):
    location_file = sys.argv[1]
    blocks_file = sys.argv[2]
   
location = {}
try:
    with open(location_file) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            row = map( lambda x: x.decode('utf-8'), row)
            if row[4]:
                location[row[0]] = (row[4],row[5])
#                print( "%s => %s, %s" % (row[0],row[4],row[5]) )
            elif row[2]:
                location[row[0]] = (row[2],row[3])
#                print( "%s => %s, %s" % (row[0],row[2],row[3]) )
except IOError as e:
    print(e)
except csv.Error as e:
    print(e)

try:
    with open(blocks_file) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            row = map( lambda x: x.decode('utf-8'), row)
            nw = ipaddress.ip_network(row[0])
            row_id = None
            if row[1]:
                loc_id = row[1]
            elif row[2]:
                loc_id = row[2]
            start = nw.network_address
            end = nw.broadcast_address
            int_start = int(nw.network_address)
            int_end = int(nw.broadcast_address)
            print('"%s","%s","%s","%s","%s","%s"' % (start,end,int_start,int_end, location[loc_id][0], location[loc_id][1] ))
except IOError as e:
    print(e)
except csv.Error as e:
    print(e)
