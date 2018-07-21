#!/bin/bash

SCRIPT_DIR=`dirname $0`
cd $SCRIPT_DIR

mkdir tmp 
pushd tmp
wget -O GeoLite2-Country-CSV.zip "http://geolite.maxmind.com/download/geoip/database/GeoLite2-Country-CSV.zip"
unzip -j GeoLite2-Country-CSV.zip
python ../lite2tolegacy.py > ../GeoIPCountryWhois.csv
popd

python csv2dat.py -w GeoLiteCountry.dat mmcountry GeoIPCountryWhois.csv
