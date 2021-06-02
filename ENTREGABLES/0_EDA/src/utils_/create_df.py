# Functions to create smaller and sorted df

# ------ Import the necessary libraries ------

import pandas as pd
import numpy as np

# -----------------------------------------------------------------------------------------------

# Function to groupby a DataFrame by a column
def groupby_country(data, column):

    # Group df with their max value as entry
    covid_groupby = data.groupby(column).max()
    covid_groupby.reset_index(inplace=True)

    # Actualize columns: "deaths_ratio", "non_risky_age", "risky_age"

    covid_groupby["deaths_ratio"] = covid_groupby["total_deaths"]/covid_groupby["total_cases"] * 100
    covid_groupby["non_risky_age"] = 100 - covid_groupby["aged_65_older"] - covid_groupby["aged_70_older"]
    covid_groupby["risky_age"] = 100 - covid_groupby["non_risky_age"]

    # Reorder columns
    covid_groupby = covid_groupby[["continent", "country", "median_age", "aged_65_older", "aged_70_older", "non_risky_age", "risky_age", "total_cases", "total_deaths", "deaths_ratio", "hospital_beds_per_thousand", "gdp_per_capita", "HDI", "Poverty %"]]

    return covid_groupby

# -----------------------------------------------------------------------------------------------

# Function to return df from the countries of each continent
def cases_continent(data,column,continent): # data:covid_groupby, column:"continent", continent: each continent
    # Mask to return Df with the condition
    x = data[data[column] == continent]

    return x


# Function to sort the values of each continent and take 5 head and 5 tail to do a bigger Dataset
def sort_value(continent, column): # Continent: continent, column: column to sort by
    y = continent.sort_values(column, ascending=False)
    # print(len(y.values))

    if len(y.values) > 10:
        x = y.head(5).append(y.tail(5))
        return x

    return y


# Function to concatenate the sorted values of each continent by column ("gdp per capita")
def concatenate_df(df1, df2, df3, df4, df5, df6, column):
    gdp_mundo_sorted = pd.concat([df1, df2, df3, df4, df5], axis=0)
    
    # Sort values from the new dataset
    gdp_mundo_sorted = gdp_mundo_sorted.sort_values(column, ascending=False)
    gdp_mundo_sorted.reset_index(inplace=True, drop=True)

    return gdp_mundo_sorted
