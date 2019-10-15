#!/usr/bin/env python
# coding: utf-8

# In[1]:

print(f"...starting EXTRACT of Seba Tables.")

import pandas as pd


# In[2]:


# Pandas Web Scrape URLs
# URL for the 'California Median Age by City'
age_url = 'http://www.usa.com/rank/california-state--median-age--city-rank.htm'

# URL for the 'California Crime Rate by Cities Table'
crime_url = 'https://en.wikipedia.org/wiki/California_locations_by_crime_rate'

# URL for the 'List of cities and towns in California'
cities_url = 'https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_California'


# In[3]:


# Use the read_html function in Pandas to automatically scrape any tabular data from a page
age_table = pd.read_html(age_url)
crime_table = pd.read_html(crime_url)
cities_table = pd.read_html(cities_url)


# In[4]:


# Read CSV Files


# In[5]:


# Create Data Frame for Each Data Set

# Median Age DF
ages_df = age_table[0]
ages_df.columns = ['Rank', 'Median Age', 'City/Population']

# Crime Rate DF
crime_rate_df = crime_table[2]
crime_rate_df.columns = ['City','County', 'Population', 'Population density', 'Violent crimes',  
              'Violent crime rate per 1,000 persons', 'Property Crimes', 'Property crime rate per 1,000 persons']

# Cities DF
cities_df = cities_table[1]
cities_df.columns = ['City','Type', 'County', 'Population', 'sq mi', 'sq km', 'Incorporated']

# Read the Unemployment CSV into a Pandas DataFrame
csv_path = "Resources/Unemployment Rate California Cities.csv"

# Unemployment DF
unemployment_df = pd.read_csv(csv_path)

# Read the Median Home Price CSV into a Pandas DataFrame
csv_path = "Resources/median_home_price_city_ca.csv"

# Median Home Price DF
home_df = pd.read_csv(csv_path)


# In[6]:


# Clean Median Age DF

# Split the 'City/Population' column to isolate the city
ages_df[['City','Population']] = ages_df['City/Population'].str.split('/',expand=True)

# Delete unwanted columns using the columns parameter of drop
clean_ages_df = ages_df.drop(["Rank", "City/Population", "Population"], axis=1)

# Remove the 'CA' from the end of each city name
clean_ages_df['City'] = clean_ages_df['City'].str.replace(', CA ', '')

# Delete the first row to remove redundant header
clean_ages_final_df = clean_ages_df.drop(clean_ages_df.index[0])

# Re-Arrange the order of the columns
clean_ages_final_df = clean_ages_final_df[['City','Median Age']]

# Set the index to the 'City' column
clean_ages_final_df.set_index('City', inplace=True)

# Display Datframe
clean_ages_final_df.head()


# In[7]:


# Clean Crime Rate DF

# Delete unwanted columns using the columns parameter of drop
clean_crime_df = crime_rate_df.drop(["County","Population", "Population density", "Violent crime rate per 1,000 persons", "Property crime rate per 1,000 persons"], axis=1)

# Set the index to the 'City' column
clean_crime_df.set_index('City', inplace=True)

# Display Datframe
clean_crime_df.head()


# In[8]:


# Clean Cities DF

# Delete unwanted columns using the columns parameter of drop
clean_cities_df = cities_df.drop(["Type", "sq mi", "sq km", "Incorporated"], axis=1)

# Set the index to the 'City' column
clean_cities_df.set_index('City', inplace=True)

# Display Datframe
clean_cities_df.head()


# In[9]:


# Clean Unemployment DF

# Remove trailing space off the "Area Name"
unemployment_df['Area Name'] = unemployment_df['Area Name'].str.rstrip()

# Rename the first column
unemployment_df.rename(columns={"Area Name": "City"}, inplace=True)

# Delete unwanted columns using the columns parameter of drop
unemployment_df = unemployment_df.drop(["County"], axis=1)

# Set the index to the 'City' column
unemployment_df.set_index('City', inplace=True)

# Display Datframe
unemployment_df.head()


# In[10]:


# Clean Meadian Home Price DF

# Delete unwanted columns using the columns parameter of drop
clean_home_df = home_df.drop(["RegionID", "County"], axis=1)

# Rename the last column
clean_home_df.rename(columns={"Aug-19": "Median Home Price"}, inplace=True)

# Set the index to the 'City' column
clean_home_df.set_index('City', inplace=True)

# Display Datframe
clean_home_df.head()


# In[11]:


# Save all tables directly to an html file

# Median Age Table
clean_ages_final_df.to_html('Resources/clean_age_table.html')

# Crime Rate Table
clean_crime_df.to_html('Resources/crime_rate_table.html')

# Cities Table
clean_cities_df.to_html('Resources/clean_population_table.html')

# Unemployment Table
unemployment_df.to_html('Resources/clean_unemployment_table.html')

# Median Home Price Table
clean_home_df.to_html('Resources/clean_home_table.html')


# In[12]:


# Save all tables directly to an CSV file

# Median Age Table
clean_ages_final_df.to_csv('Resources/clean_age.csv')

# Crime Rate Table
clean_crime_df.to_csv('Resources/clean_crime.csv')

# Cities Table
clean_cities_df.to_csv('Resources/clean_population.csv')

# Unemployment Table
unemployment_df.to_csv('Resources/clean_unemployment.csv')

# Median Home Price Table
clean_home_df.to_csv('Resources/clean_home.csv')


print(f"""
----------------------------------
Seba Tables Extracted!
----------------------------------
Return: 5 Dataframes
----------------------------------
""")



