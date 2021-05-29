import pandas as pd
import numpy as np

#1. Read Salaries.csv as a dataframe called
sal=pd.read_csv("Salaries.csv")

#2. Check the head of the DataFrame.
print(sal.head())

#3. Use the .info() method to find out how many entries there are.
print(sal.info())

#4. What is the average BasePay ?
print("Average BasePay : ", sal['BasePay'].mean())

#5. What is the highest amount of OvertimePay in the dataset ?
print("The highest amount of OvertimePay in the dataset : ", sal['OvertimePay'].max())

#6. What is the job title of JOSEPH DRISCOLL ?
sal_JOSEPH_DRISCOLL=sal[sal['EmployeeName']=='JOSEPH DRISCOLL']
print("The job title of JOSEPH DRISCOLL : ",sal_JOSEPH_DRISCOLL
['JobTitle'])

#7. How much does JOSEPH DRISCOLL make (including benefits)?
print("JOSEPH DRISCOLL make (including benefits) : ",sal_JOSEPH_DRISCOLL['TotalPayBenefits'])

#8. What is the name of highest paid person (including benefits)?
sal_highest_paid_person=sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()]
print("Name of highest paid person : ")
print(sal_highest_paid_person[['EmployeeName','TotalPayBenefits']])

#9. What is the name of lowest paid person (including benefits)?
sal_lowest_paid_person=sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].min()]
print("Name of lowest paid person : ")
print(sal_lowest_paid_person[['EmployeeName','TotalPayBenefits']])

#10. What was the average (mean) BasePay of all employees per year? (2011-2014) ?
print("The average (mean) BasePay of all employees per year? (2011-2014) : \n",sal.groupby('Year').mean()['BasePay'])

#11. How many unique job titles are there?
print("Number of job titles : ",sal['JobTitle'].unique())

#12. What are the top 5 most common jobs?
print("5 most common jobs : \n",sal['JobTitle'].value_counts().head(5))

#13. How many Job Titles were represented by only one person in 2013?
print("Number of Job Titles were represented by only one person in 2013 : ",sum(sal[sal['Year']==2013]['JobTitle'].value_counts()==1))

#14. How many people have the word Chief in their job title? (This is pretty tricky)
list =sal['JobTitle']
count=0
for x in list:
    if x.lower().find('chief') != -1:
        count+=1
print("Number of people have the word Chief in their job title: ", count)

#15. Bonus: Is there a correlation between length of the Job Title string and Salary?
lenght_of_job_title = []
for i in list:
    lenght_of_job_title.append(len(i))
sal['Lenght Of Job Title'] = lenght_of_job_title
print(sal[['Lenght Of Job Title', 'TotalPayBenefits']].corr())