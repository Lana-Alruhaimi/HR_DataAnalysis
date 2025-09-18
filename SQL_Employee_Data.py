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
    df.to_sql('Table_of_Employees', conn, if_exists='replace',index=False) #replaces current to make sure the data is as up-to-date as possible
    print("Data inserted successfully.")

    ### Print table
    
    cursor = conn.cursor()
    '''
    cursor.execute("SELECT * FROM Table_of_Employees")
    rows = cursor.fetchall()
    print("\n--------Table of Employees--------")
    headers = [description[0] for description in cursor.description] #points cursor at column names
    print (headers)

    for row in rows:
        print (row)
    '''
    ########### Data Analysis Begins ###########
    
    ### Given Questions ###

    # How many total employees are there?
    cursor.execute("SELECT COUNT(EmployeeNumber) FROM Table_of_Employees")
    Emp_Amount = cursor.fetchone()[0] # takes result as num , instead of tuple
    print (f"\nNumber of Employees: {Emp_Amount}\n")

    # What is the employee count for each department?
    cursor.execute("SELECT Department, COUNT(EmployeeNumber) FROM Table_of_Employees GROUP BY Department")
    Dept_Num = cursor.fetchall()
    print ("Employees per Department:\n")
    for row in Dept_Num:
        print(f"{row[0]}:{row[1]}")

    # What is the average monthly income by job role?
    cursor.execute("SELECT JobRole, AVG(MonthlyIncome) FROM Table_of_Employees GROUP BY JobRole")
    Avg_Sal_Role = cursor.fetchall()
    print ("\n\nAverage Monthly Salary per Role (Highest to lowest):\n")
    for row in Avg_Sal_Role:
        print(f"{row[0]}: {row[1]}")
    
    # Who are the top 5 employees by performance rating?
    # Which department has the highest average performance rating?
    #### My Questions ###
    # What is the average monthly income per total working years? (sorted by highest income to lowest)
    # What is the average salary hike % per Education field (sorted by highest salary hike % to lowest)
    # What is the average monthly salary per gender?
    
    ########### Data Analysis Ends ###########

except sql.Error as e: #saves error in var to print later (helps understand the reason for error)
    print(f"Error: {e}")
finally:
    if 'conn' in locals() and conn:
        conn.close() # closing force saves any updates and unlocks db
        print("Database connection closed.")
