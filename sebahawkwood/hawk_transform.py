#!/usr/bin/env python
# coding: utf-8

# Import dependencies from Extract script
import seba_extract as se
print(f"""
Seba Tables Received.
----------------------------------
...beginning Hawk TRANSFORM
""")


# Cities by population. Merge with cities by crime
master_df = se.clean_cities_df.merge(se.clean_crime_df, how='inner', left_index=True, right_index=True)

# Merge with cities by age
master_df = master_df.merge(se.clean_ages_final_df, how='left', on='City')

# Merge with cities by home price
master_df =  master_df.merge(se.clean_home_df, how="inner", on='City')

# Merge with cities by unemployment
master_df = master_df.merge(se.unemployment_df, how='inner', on="City")

# Create list of keys for the master dictionaries from the dataframe index and column names
keys = []
keys.append(master_df.index.name)

for column in master_df.columns.to_list():  
    keys.append(column)
    
keys

# iterate over rows in the dataframe and transform rows into individual dictionaries
master_list = []
for x in range(len(master_df)):
    
    # Empty dictionary to hold this record
    dictionary = {}
    
    # Insert city name from dataframe index
    value = master_df.index[x]
    dictionary.update({keys[0]: value})
        
    # Insert other key value pairs from dataframe columns
    for i in range(len(keys) - 1):

        value = master_df.iloc[x,i]
        
        # For numpy data types take the value of the data, otherwise leave data as is 
        try:
            value = value.item()
        except:
            value = value

        # Write document dictionary
        dictionary.update({keys[i+1]: value})
    
    master_list.append(dictionary)

print(f"""
----------------------------------
Hawk List Transformed!
----------------------------------
Return: Master List of Dictionaries
""")



