import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('../../Data/Employee_Data.csv') #allows read after folder changes and code stays portable

########### Interactive Filter (Age) ###########

### Create filter
Age_Min = int(df['Age'].min())
Age_Max = int (df['Age'].max())
Age_Select = st.sidebar.slider(
    'Select Age Range',
    min_value = Age_Min,
    max_value = Age_Max,
    value =(Age_Min,Age_Max)
)

### Interactively filter employee's data
Filtered_df = df [df['Age'].between(Age_Select[0],Age_Select[1])]

Depts = Filtered_df['Department'].unique() #list of dept names (no repeating) for dropdown chart
Brand_Colors = ['#4f008c','#c2a6cf','#e4d9eb','#e4e9ee'] # Brand colors hex code

########### Data Visualization ###########

### Bar chart (Employees per Department) 
Dept_Num = Filtered_df['Department'].value_counts().reset_index() #counts emp per dept and converts to dataframe so i can use plotly express (more customization)
Dept_Num.columns = ['Department','Number of Employees'] #label of columns i want in the bar chart

Dept_Num_Bar = px.bar( #Bar creation
    Dept_Num,
    x = 'Department',
    y = 'Number of Employees',
    color='Department', #makes each bar diff color
    color_discrete_sequence= Brand_Colors,
    title = "Employees by Department"
) 
st.plotly_chart (Dept_Num_Bar) #to display the bar chart

### Pie chart (job satisfaction)
Sat_Num = Filtered_df['JobSatisfaction'].value_counts().reset_index() #Sat_Num = number of employees per satisfaction level
Sat_Num.columns = ['Job Satisfaction','Number of Employees']

Sat_Pie = px.pie(
    Sat_Num,
    values='Number of Employees',
    names = 'Job Satisfaction',
    color= 'Job Satisfaction',
    color_discrete_sequence=Brand_Colors,
    title = 'Job Satisfaction Distribution',
)
st.plotly_chart(Sat_Pie)

### Box chart (salary per education field)
Edu_Field_Box = px.box(
    Filtered_df,
    x = 'EducationField', # x because it is fixed (categorical)
    y = 'MonthlyIncome',
    color = 'EducationField',
    color_discrete_sequence=Brand_Colors,
    title = 'Salary Distribution by Education Field'
)
st.plotly_chart(Edu_Field_Box)

### Dropdown Menu (departments)
Selected_Dept = st.selectbox('Choose a department', Depts) #creates dropdown menu & saves users choice
Filtered_Dept = Filtered_df[Filtered_df['Department']==Selected_Dept] #filters depts based on selected dept
st.dataframe(Filtered_Dept) # Displays result as table


########### Update Employee Data ###########

### Add New Employee
st.header ("Add New Employee")

with st.form("New_Emp_Info_Form"):
    st.write("Enter Employee's Information: ")
    Emp_Num = st.number_input("Employee Number", step=1) #step=1 makes it only integers
    Dept = st.selectbox("Department",Depts)
    Edu_Field = st.text_input("Education Field")
    Job_Role = st.text_input("Job Role")
    Sal = st.number_input("Monthly Income", min_value=0) #so salary isnt negative
    Submitted = st.form_submit_button('Add Employee') #submit button
    
if Submitted:
    New_Emp_Data = { #create dictionary
        "EmployeeNumber":Emp_Num,
        "Department":Dept,
        "EducationField":Edu_Field,
        "JobRole": Job_Role,
        "MonthlyIncome":Sal
        }
    if not all(New_Emp_Data.values()): #aka if there are empty fields
        st.warning("Please make sure all fields are filled.")
    elif Emp_Num in df ['EmployeeNumber'].values:
        st.warning("An employee with that number already exists")
    else:
        New_Emp_df = pd.DataFrame([New_Emp_Data]) #dataframe for new employee
        df = pd.concat([df,New_Emp_df],ignore_index=True) #add to main dataframe and make sure no indexes are repeated
        df.to_csv('Employee_Data.csv', index=False) #save df w/new employee (in csv file), dont add row num to csv
        st.success("New employee has been added.")
        st.rerun()


#### Update Employee Salary
st.header("Update Employee Salary")

with st.form("Update_Sal_Form"):
    st.write("Enter Employee Information:")
    Emp_Num_Update = st.number_input("Employee Number", step=1) #Employee number that will have updated salary
    Sal_Update = st.number_input("Monthly Income", min_value=0)
    Submitted_Update = st.form_submit_button('Update Employee Salary')

    if Submitted_Update: #no need for dictionary, because we are updating a value, not inserting a row
        if Emp_Num_Update not in df ['EmployeeNumber'].values: # we can't update the salary if the employee doesn't exist
            st.warning("An employee with that number doesn't exist")
        else:
            Sal_Update_Index = df[df['EmployeeNumber'] == Emp_Num_Update].index #finds index based on employee number
            df.loc[Sal_Update_Index,'MonthlyIncome'] = Sal_Update #updates employee salary
            df.to_csv('Employee_Data.csv', index=False) 
            st.success(f"Employee salary has been updated for Employee number: {Emp_Num_Update}.")
            st.rerun()
