import sqlite3 as sql
import pandas as pd

########### Load, Clean, & Insert Data ###########

### Load data into Pandas data frame & clean it
df = pd.read_csv('Employee_Data.csv') #Employee data is saved as df
df = df.dropna() #drop null values (clean data)

### Create local SQLite database and insert data
Emp_db ='Employee_Data.db'
try:
    conn = sql.connect(Emp_db) #create connection
    print(f"Successful connection to {Emp_db}.")
    df.to_sql('Table of Employees', conn, if_exists='replace',index=False) #replaces current to make sure the data is as up-to-date as possible
    print("Data inserted successfully.")
except sql.Error as e: #saves error in var to print later (helps understand the reason for error)
    print(f"Error: {e}")
finally:
    if 'conn' in locals() and conn:
        conn.close() # closing force saves any updates and unlocks db
        print("Database connection closed.")


########### Data Analysis ###########