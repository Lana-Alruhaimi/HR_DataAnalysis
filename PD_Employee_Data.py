import pandas as pd


########### Load & Clean Data ###########

df = pd.read_csv('Employee_Data.csv') #Employee data is saved as df
df = df.dropna() #drop null values (clean data)
print(df.info()) #print proving there are no null values
print("\n\n\n\n**********************************************************\n")


########### Data Analysis ###########

### Given Questions ###

# How many total employees are there? 
Emp_Num = df.shape[0] #number of rows (for columns replace 0 w/ 1)
print (f"\nNumber of Employees: {Emp_Num}")


# What is the employee count for each department? 
Dept_Num = df.groupby('Department').size() #group by splits into smaller dfs, size counts rows
print (f"\nEmployees per Department:\n{Dept_Num}")

# What is the average monthly income by job role? (sorted by highest income to lowest)
Avg_Sal_Role= df.groupby('JobRole')['MonthlyIncome'].mean().sort_values(ascending=False) #[specify column to calculate], mean is avg, sort values orders it
print (f"\nAverage Monthly Salary per Role (Highest to lowest):\n{Avg_Sal_Role}")

# Who are the top 5 employees by performance rating? 
Top5_Rate = df.nlargest(5,'PerformanceRating')# would add ['Name'] if I only wanted to print their names, but df doesnt have names
print (f"\nTop 5 Employees by Performance Rating:\n{Top5_Rate}")

# Which department has the highest average performance rating? 
Avg_Rate = df.groupby("Department")['PerformanceRating'].mean() #Avg per dept
Max_Rate_Dept = Avg_Rate.idxmax() #idxmax returns the index(name) of highest dept
Max_Rate_Num = Avg_Rate.max()
print(f"\nThe {Max_Rate_Dept} Department has the Highest Average Performance Rating: {Max_Rate_Num}")



#### My Questions ###

# What is the average monthly income per total working years? (sorted by highest income to lowest)
Avg_Sal_Years = df.groupby('TotalWorkingYears')['MonthlyIncome'].mean().sort_values(ascending=False)
print(f"\nAverage Salary per Years Working (Highest to lowest):\n{Avg_Sal_Years}")

# What is the average salary hike % per Education field (sorted by highest salary hike % to lowest)
Avg_SalH_Edu = df.groupby('EducationField')['PercentSalaryHike'].mean().sort_values(ascending=False) #average salary hike
print(f"\nAverage Salary Hike Percent per Education Field (Highest to lowest):\n{Avg_SalH_Edu}")

# What is the average monthly salary per gender?
Avg_Sal_G = df.groupby('Gender')['MonthlyIncome'].mean()
print (f"\nAverage Salary for each Gender:\n{Avg_Sal_G}")
