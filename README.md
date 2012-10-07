zip-code-data-hacking
=====================

sourcing publicly available files, generate useful zip code-county data. 

My goal is to be able to map zip codes to county FIPS codes, without paying. 

I was able to find a zip code database from unitedstateszipcodes.org, each zip code had a county name but not a county FIPS code. I was able to find County FIPS codes on the census.gov site through some google hacking.

The data files are in the data directory - I'll eventuall add code to make sure the latest data files are retrieved at runtime. I didn't do this yet because I didn't want to hammer the sites while I was quickly iterating - a local copy did just fine.

The troubled python code county_fips_codes_for_zip_codes.py will attempt to match the two data sets and yield data in the tab-delimited format:
zip_code county_fips_cd county_name state_cd

this will be saved to the output directory.

I did this because geo data is difficult to find and the scummy data-for-sale sites SEOd their way ahead of any useful information. 

I haven't put a lot of time into this and I can certainly use some help and polishing. In the meantime, the output data is pretty damn good for a first effort.
