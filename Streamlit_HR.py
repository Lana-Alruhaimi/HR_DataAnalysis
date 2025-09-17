import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('Employee_Data.csv')

Depts = df['Department'].unique() #list of dept names (no repeating)
Brand_Colors = ['#4f008c','#c2a6cf','#e4d9eb','#e4e9ee'] # Brand colors hex code

########### Data Visualization ###########

### Bar chart (Employees per Department) 
Dept_Num = df['Department'].value_counts().reset_index() #counts emp per dept and converts to dataframe so i can use plotly express (more customization)
Dept_Num.columns = ['Department','Number of Employees'] #label of columns i want in the bar chart

Bar = px.bar( #Bar creation
    Dept_Num,
    x = 'Number of Employees',
    y = 'Department',
    color='Department', #makes each bar diff color
    color_discrete_sequence= Brand_Colors,
    title = "Employees per Department"
) 
st.plotly_chart (Bar) #to display the bar chart

### Pie chart (job satisfaction)
Sat_Num = df['JobSatisfaction'].value_counts().reset_index() #Sat_Num = number of employees per satisfaction level
Sat_Num.columns = ['Job Satisfaction','Number of Employees']

Pie = px.pie(
    Sat_Num,
    values='Number of Employees',
    names = 'Job Satisfaction',
    color= 'Job Satisfaction',
    color_discrete_sequence=Brand_Colors,
    title = 'Job Satisfaction Distribution',
)
st.plotly_chart(Pie)

### Box chart (salary per education field)
Box = px.box(
    df,
    x = 'EducationField', # x because it is fixed (categorical)
    y = 'MonthlyIncome',
    color = 'EducationField',
    color_discrete_sequence=Brand_Colors,
    title = 'Salary Distribution by Education Field'
)
st.plotly_chart(Box)

### Dropdown Menu (departments)
Selected_Dept = st.selectbox('Choose a department', Depts) #creates dropdown menu & saves users choice
Filtered_Dept = df[df['Department']==Selected_Dept] #filters depts based on selected dept
st.dataframe(Filtered_Dept) # Displays result as table


########### Update Employee Data ###########

### Add new employee
st.header ("Add new employee")

with st.form("New_Emp_Info"):
    st.write("Enter Employee's Information: ")
    EmployeeNumber = st.number_input("Employee Number", step=1) #step=1 makes it only integers
    Department = st.selectbox("Department",Depts)
    EducationField = st.text_input("Education Field")
    JobRole = st.text_input("Job Role")
    MonthlyIncome = st.number_input("Monthly Income", min_value=0) #so salary isnt negative
    submitted = st.form_submit_button('Add Employee') #submit button
    
if submitted:
    New_Emp_Data = { #create dictionary
        "Employee Number":EmployeeNumber,
        "Department":Department,
        "Education Field":EducationField,
        "Job Role": JobRole,
        "Monthly Income":MonthlyIncome
        }
    if not all(New_Emp_Data.values()): #aka if there are empty fields
        st.warning("Please make sure all fields are filled.")
    elif EmployeeNumber in df ['EmployeeNumber'].values:
        st.warning("An employee with that number already exists")
    else:
        New_Emp_df = pd.DataFrame([New_Emp_Data]) #dataframe for new employee
        df = pd.concat([df,New_Emp_df],ignore_index=True) #add to main dataframe and make sure no indexes are repeated
        df.to_csv('Employee_Data.csv', index=False) #save df w/new employee (in csv file), dont add row num to csv
        st.success("New employee has been added.")
        st.rerun()


########### Update Employee Data ###########

