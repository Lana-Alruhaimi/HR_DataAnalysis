import pandas as pd


########### Load & Clean Data ###########

df = pd.read_csv('Data/Employee_Data.csv') #allows read after folder changes and code stays portable
df = df.dropna() #drop null values (clean data)
print(df.info()) #print proving there are no null values
print("\n\n\n\n**********************************************************\n")


########### Data Analysis ###########

### Given Questions ###

# How many total employees are there? 
Emp_Amount = df.shape[0] #number of rows (for columns replace 0 w/ 1)
print (f"\n- Number of Employees: {Emp_Amount}")


# What is the employee count for each department? 
Dept_Num = df.groupby('Department').size() #group by splits into smaller dfs, size counts rows
print (f"\n- Employees by Department:\n{Dept_Num}")

# What is the average monthly income by job role? (sorted by highest income to lowest)
Avg_Sal_Role= df.groupby('JobRole')['MonthlyIncome'].mean().sort_values(ascending=False) #[specify column to calculate], mean is avg, sort values orders it
print (f"\n- Average Monthly Salary by Role (Highest to lowest):\n{Avg_Sal_Role}")

# Who are the top 5 employees by performance rating? 
Top5_Rate = df.nlargest(5,'PerformanceRating')# would add ['Name'] if I only wanted to print their names, but df doesnt have names
print (f"\n- Top 5 Employees by Performance Rating:\n{Top5_Rate}")

# Which department has the highest average performance rating? 
Avg_Rate = df.groupby("Department")['PerformanceRating'].mean() #Avg by dept
Max_Rate_Dept = Avg_Rate.idxmax() #idxmax returns the index(name) of highest dept
Max_Rate_Num = Avg_Rate.max()
print(f"\n- The {Max_Rate_Dept} Department has the Highest Average Performance Rating: {Max_Rate_Num}")



#### My Questions ###

# What is the average monthly income by total working years? (sorted by highest income to lowest)
Avg_Sal_Years = df.groupby('TotalWorkingYears')['MonthlyIncome'].mean().sort_values(ascending=False)
print(f"\n- Average Salary by Years Working (Highest to lowest):\n{Avg_Sal_Years}")

# What is the average salary hike % by Education field (sorted by highest salary hike % to lowest)
Avg_SalH_Edu = df.groupby('EducationField')['PercentSalaryHike'].mean().sort_values(ascending=False) #average salary hike
print(f"\n- Average Salary Hike Percent by Education Field (Highest to lowest):\n{Avg_SalH_Edu}")

# What is the average monthly salary by gender?
Avg_Sal_G = df.groupby('Gender')['MonthlyIncome'].mean()
print (f"\n- Average Salary for each Gender:\n{Avg_Sal_G}")
