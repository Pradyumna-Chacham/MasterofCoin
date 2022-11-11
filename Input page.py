import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Budget Calculator
Salary=float(input("Enter salary per month:"))
it_rate=float(input("Enter income tax rate of your income bracket:"))
Sal_bIT=Salary
Sal_aIT=(Salary-((it_rate*Salary)/100))
#Housing Expenses
r=float(input("Enter amount paid for housing every month:"))
m=float(input("Enter maintenance fees:"))
i=float(input("Enter insurance amount per month:"))
u=float(input("Enter amount paid for utilities:"))
d1={'Category':['Rent','Maintenance','Insurance','Utilities'],'Amount':[r,m,i,u]}
df1=pd.DataFrame(d1)
df1.groupby(['Category']).sum().plot(kind='pie',subplots=True,autopct='%1.0f%%')
plt.title("Housing Expenses Breakdown")
Housing_exp=r+m+i+u
#Transportation
vehicle_loan=float(input("Enter amount paid for vehicle loan:"))
petrol=float(input("Enter amount paid for fuel:"))
car_insurance=float(input("Enter amount paid for car insurance:"))
car_maintenance=float(input("Amount spent on car_maintenance:"))
other_transport=float(input("Other transport costs:"))
d2={'Category':["Vehicle loan","Fuel","Car Insurance","Car maintenance","Other"],'Amount':[vehicle_loan,petrol,car_insurance,car_maintenance,other_transport]}
df2=pd.DataFrame(d2,columns=['Category','Amount'])
print("Transportation costs")
df2.groupby(['Category']).sum().plot(kind='pie',subplots=True,autopct='%1.0f%%')
plt.title('Transportation Expenses Breakdown')
Transportation_exp=vehicle_loan+petrol+car_insurance+car_maintenance+other_transport
#Loan payments
Credit_card=float(input("Credit card payments:"))
edu_loan=float(input("Education loan payment per month:"))
other_loan=float(input("Other loans:"))
d3={'Category':['Credit card',"Education Loan","Other loans"],'Amount':[Credit_card,edu_loan,other_loan]}
df3=pd.DataFrame(d3,columns=['Category','Amount'])
df3.groupby(['Category']).sum().plot(kind='pie',subplots=True,autopct='%1.0f%%')
plt.title('Loan Payments breakdown')
Loan_exp=Credit_card+edu_loan+other_loan
#Living expenses
clothing=float(input("Clothing expenses:"))
household_exp=float(input("Amount spent on household supplies:"))
d4={'Category':['Clothing','Household expenses'],'Amount':[clothing,household_exp]}
df4=pd.DataFrame(d4)
df4.groupby(['Category']).sum().plot(kind='pie',subplots=True,autopct="%1.0f%%")
plt.title("Living Expenses Breakdown")
Living_exp=clothing+household_exp
#Food
food=float(input("Amount spent on food:"))
meals=float(input("Amount spent on dining out:"))
d8={'Category':['Food','Meals'],'Amount':[food,meals]}
df8=pd.DataFrame(d8)
df8.groupby(['Category']).sum().plot(kind='pie',subplots=True,autopct='%1.0f%%')
plt.title('Food Expenses Breakdown')
Food_exp=food+meals
#healthcare
medicines=float(input("Enter amount spent on medicines:"))
dr_fees=float(input("Enter amount spent for doc consultation:"))
d5={'Category':['Medicines','Doctor consultation/fees'],'Amount':[medicines,dr_fees]}
df5=pd.DataFrame(d5)
Healthcare_exp=medicines+dr_fees
df5.groupby(['Category']).sum().plot(kind='pie',subplots=True,autopct='%1.0f%%')
plt.title('Healthcare Expenses')
#Savings 
Pension=float(input("Enter pension:"))
investments=float(input("Enter investments you want to contribute:"))
print("Recommended 15% of your income")
mutual_fund=float(input("Enter amount you want to invest in mutual funds:"))
fd=float(input("Fixed Deposit:"))
Savings_exp=Pension+investments+mutual_fund+fd
d6={'Category':['Mutual Funds','Fixed Deposit','Pensions','Investments'],'Amount':[mutual_fund,fd,Pension,investments]}
df6=pd.DataFrame(d6)
df6.groupby(['Category']).sum().plot(kind='pie',subplots=True,autopct='%1.0f%%')
plt.title('Savings Breakdown')
#Miscellaneous 
hobbies=float(input("Hobbies:"))
travel=float(input("Travel & Vacation:"))
recreation=float(input("Amount spent on recreation:"))
Other_exp=float(input("Other Expenses:"))
d7={'Category':['Hobbies','Travel','Recreation','Other Expenses'],'Amount':[hobbies,travel,recreation,Other_exp]}
df7=pd.DataFrame(d7)
df7.groupby(['Category']).sum().plot(kind='pie',subplots=True,autopct='%1.0f%%')
plt.title('Miscellaneous Expenses')
Miscellaneous_exp=hobbies+travel+Other_exp+recreation
#Total Expenses
Expdict={'Category':['Housing','Transportation','Loan','Living Expenses','Food Expenses','Healthcare','Miscellaneous','Savings'],'Amount':[Housing_exp,Transportation_exp,Loan_exp,Living_exp,Food_exp,Healthcare_exp,Miscellaneous_exp,Savings_exp]}
Expdf=pd.DataFrame(Expdict)
Expdf.groupby(['Category']).sum().plot(kind='pie',subplots=True,autopct='%1.0f%%')
plt.title("Total Expenses Breakdown")
#Data Insights
Hpercent=((Housing_exp*100)/Sal_aIT)
Tpercent=((Transportation_exp*100)/Sal_aIT)
Lpercent=((Living_exp*100)/Sal_aIT)
Fpercent=((Food_exp*100)/Sal_aIT)
Loanpercent=((Loan_exp*100)/Sal_aIT)
Healthpercent=((Healthcare_exp*100)/Sal_aIT)
Savingspercent=((Savings_exp*100)/Sal_aIT)
Mpercent=((Miscellaneous_exp*100)/Sal_aIT)
#SALARY TABLE
ls=[['Housing',Housing_exp,Housing_exp*12,Hpercent],['Transportation',Transportation_exp,Transportation_exp*12,Tpercent],['Loan',Loan_exp,Loan_exp*12,Loanpercent],['Living Expenses',Living_exp,Living_exp*12,Lpercent],['Healthcare',Healthcare_exp,Healthcare_exp*12,Healthpercent],['Miscellaneous',Miscellaneous_exp,Miscellaneous_exp*12,Mpercent],['Savings',Savings_exp,Savings_exp*12,Savingspercent]]
finaldf=pd.DataFrame(ls,columns=['Category','Monthly spending','Annual spending','Percent of Income'])
#Printing output
Expenses=Housing_exp+Transportation_exp+Loan_exp+Living_exp+Healthcare_exp+Miscellaneous_exp+Savings_exp
sal={'Category':['Salary before Tax','Salary after Tax','Expenses'],'Monthly':[Sal_bIT,Sal_aIT,Expenses],'Annual':[Sal_bIT*12,Sal_aIT*12,Expenses*12]}
df9=pd.DataFrame(sal)
print("FINAL SUMMARY")
print(df9)
print("="*10)
print("Housing Expenses")
print(df2)
print("="*10)
print("Loan and other expenses")
print(df3)
print("="*10)
print("Living Expenses")
print(df4)
print("="*10)
print("Food")
print(df8)
print("="*10)
print("Healthcare")
print(df5)
print("="*10)
print("Savings")
print(df6)
print("="*10)
print("Miscellaneous")
print(df7)
print("="*10)
print("Expenses Breakdown")
print(Expdf)
print("="*10)
print("Final Insights")
print(finaldf)
print("="*10)
plt.show()
























































