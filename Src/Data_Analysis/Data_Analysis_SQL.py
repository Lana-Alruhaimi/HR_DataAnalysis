import sqlite3 as sql
import pandas as pd

########### Load, Clean, & Insert Data ###########

### Load data into Pandas data frame & clean it
df = pd.read_csv('Data/Employee_Data.csv') #allows read after folder changes and code stays portable
df = df.dropna() #drop null values (clean data)

### Create local SQLite database and insert data
Emp_db ='Data/Employee_Data.db'
try:
    conn = sql.connect(Emp_db) #create connection
    print(f"\nSuccessful connection to {Emp_db}.")
    df.to_sql('Table_of_Employees', conn, if_exists='replace',index=False) #replaces current to make sure the data is as up-to-date as possible
    print("\nData inserted successfully.")

    
    cursor = conn.cursor()
    '''
    # Print table
    cursor.execute("SELECT * FROM Table_of_Employees")
    rows = cursor.fetchall()
    print("\n--------Table of Employees--------")
    headers = [description[0] for description in cursor.description] #points cursor at column names
    print (headers)

    for row in rows:
        print (row)
    '''
    print("\n\n\n\n**********************************************************\n")
    ########### Data Analysis Begins ###########
    
    ### Given Questions ###

    # How many total employees are there?
    cursor.execute("SELECT COUNT(EmployeeNumber) FROM Table_of_Employees")
    Emp_Amount = cursor.fetchone()[0] # takes result as num , instead of tuple
    print (f"\n- Number of Employees: {Emp_Amount}\n")

    # What is the employee count for each department?
    cursor.execute("SELECT Department, COUNT(EmployeeNumber) FROM Table_of_Employees GROUP BY Department")
    Dept_Num = cursor.fetchall()
    print ("- Employees by Department:")
    for row in Dept_Num:
        print(f"{row[0]}:{row[1]}")

    # What is the average monthly income by job role?
    cursor.execute("SELECT JobRole, AVG(MonthlyIncome) AS Avg_Sal FROM Table_of_Employees GROUP BY JobRole ORDER BY Avg_Sal")
    Avg_Sal_Role = cursor.fetchall()
    print ("\n- Average Monthly Salary by Role (lowest to highest):")
    for row in Avg_Sal_Role:
        print(f"{row[0]}: {row[1]}")
    
    # Who are the top 5 employees by performance rating?
    cursor.execute("SELECT EmployeeNumber, PerformanceRating FROM Table_of_Employees ORDER BY PerformanceRating DESC LIMIT 5")
    Top5_Rate = cursor.fetchall()
    print (f"\n- Top 5 Employees by Performance Rating:")
    for row in Top5_Rate:
        print(f"(Employee Number: {row[0]}) Rating: {row[1]}")

    # Which department has the highest average performance rating?
    cursor.execute("SELECT Department, AVG(PerformanceRating) AS Avg_Rate FROM Table_of_Employees GROUP BY Department ORDER BY Avg_Rate DESC LIMIT 1")
    Max_Rate = cursor.fetchone()
    print(f"\n- The {Max_Rate[0]} Department has the Highest Average Performance Rating: {Max_Rate[1]}")

    #### My Questions ###

    # What is the average monthly income by total working years? (sorted by highest income to lowest)
    cursor.execute("SELECT TotalWorkingYears, AVG(MonthlyIncome) AS Avg_Sal FROM Table_of_Employees GROUP BY TotalWorkingYears ORDER BY Avg_Sal DESC") #DESC maks it high to low instead of the opposite
    Avg_Sal_Years = cursor.fetchall()
    print("\n- Average Salary by Years Working (Highest to lowest):")
    for row in Avg_Sal_Years:
        print(f"{row[0]}: {row[1]}")

    # What is the average salary hike % by Education field (sorted by highest salary hike % to lowest)
    cursor.execute("SELECT EducationField, AVG(PercentSalaryHike) AS Avg_Sal_Hike FROM Table_of_Employees GROUP BY EducationField ORDER BY Avg_Sal_Hike DESC")
    Avg_Sal_Hike = cursor.fetchall()
    print("\n- Average Salary Hike Percent by Education Field (Highest to lowest):")
    for row in Avg_Sal_Hike:
        print(f"{row[0]}: {row[1]}")

    # What is the average monthly salary by gender?
    cursor.execute("SELECT Gender, AVG(MonthlyIncome) FROM Table_of_Employees GROUP BY Gender")
    Avg_Sal_G = cursor.fetchall()
    print("\n- Average Salary for each Gender:")
    for row in Avg_Sal_G:
        print(f"{row[0]}: {row[1]}")

    ########### Data Analysis Ends ###########

except sql.Error as e: #saves error in var to print later (helps understand the reason for error)
    print(f"\nError: {e}")
finally:
    if 'conn' in locals() and conn:
        conn.close() # closing force saves any updates and unlocks db
        print("\nDatabase connection closed.\n")
