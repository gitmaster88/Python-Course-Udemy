import pandas as pd
import sqlite3

# import some data from .csv to DataFrames
airports = pd.read_csv('C:/Python-Course-Udemy/extra_pandas_practice/airports.csv')
airport_freq = pd.read_csv('C:/Python-Course-Udemy/extra_pandas_practice/airport-frequencies.csv')
runways = pd.read_csv('C:/Python-Course-Udemy/extra_pandas_practice/runways.csv')

# SQLite connection creation
con = sqlite3.connect('testdatabase.db')

# write DataFrames into new SQLite tables, just to have some data to work with
airports.to_sql("airports", con, if_exists="replace")
airport_freq.to_sql("airport_freq", con, if_exists="replace")
runways.to_sql("runways", con, if_exists="replace")

# read sqlite tables into DataFrames using Pandas
airports_from_db = pd.read_sql_query("SELECT * FROM airports", con)
airport_freq_from_db = pd.read_sql_query("SELECT * FROM airport_freq", con)
runways_from_db = pd.read_sql_query("SELECT * FROM runways", con)

# join using pandas
test_join = airport_freq_from_db.merge(airports_from_db[airports_from_db.ident == 'KLAX'][['id']],
                            left_on='airport_ref', right_on='id', how='inner')[
    ['airport_ident', 'type', 'description', 'frequency_mhz']]

# loading the DF into sqlite
test_join.to_sql("test_join", con, if_exists="replace")

# query the table to validate final result
test_join_from_db = pd.read_sql_query("SELECT * FROM test_join", con)

# result validation
print(airports_from_db.head(2))
print()
print(airport_freq_from_db.head(2))
print()
print(runways_from_db.head(2))
print()
print(test_join_from_db)
con.close()
