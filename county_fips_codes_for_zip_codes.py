#!/bin/python
# source files:
# http://quickfacts.census.gov/qfd/download/FIPS_CountyName.txt
# http://www.unitedstateszipcodes.org/zip_code_database.csv

import sys, re, csv
counties = {}
no_match = []
zip_fips = {}
fips_regex = re.compile('^[0-9]{5}')
fips_data = open('data/FIPS_CountyName.txt').readlines()
zip_data = 'data/zip_code_database.csv'
output_file = open('output/zip_code_to_fips_county_code.txt','w')

for line in fips_data:
  data = line.strip()
  fips_cd = data[0:5]
  if fips_regex.match(fips_cd) and fips_cd[2:5] != '000':
    county_name, state_cd = data[6:].split(',')
    state_cd = state_cd.replace(' ','')
    county_name = county_name.upper().replace('.','')
    counties[(state_cd, county_name)] = fips_cd

# now, read the zip code database file
# warning, this is a super-quick hack and this is O(sucky). it could be
# much more efficient. 
# we should really build an intermediate list of unique counties found in the 
# zip code file but a) i'm being lazy and b) this is small data. runtime is  
# quick. 

# in a few places, we need to clean text. we'll do the following
# - convert it to upper case
# - remove periods (i.e. ST.)
# - remove the surrounding double-quotes
with open(zip_data, 'rb') as f:
    reader = csv.reader(f)
    for data in reader:
      zip_code = data[0]
      state_cd = data[5].upper()

      county_name = data[6].replace('"','').upper().replace('.','')
 
      try:
        fips_cd_for_zip_code = counties[(state_cd, county_name)]
        zip_fips[zip_code] = fips_cd_for_zip_code
        output_file.write("%s\t%s\t%s\t%s\n" % 
          (zip_code, fips_cd_for_zip_code, county_name, state_cd))
      except KeyError:
        no_match.append((state_cd, county_name))

output_file.close()

print "found county matches for %d zip codes" % len(zip_fips.items())
print "-------"
print "couldn't find a match for the following %d items." %len(set(no_match))
print "investigate possible data issues."
for itm in set(no_match):
  print itm
