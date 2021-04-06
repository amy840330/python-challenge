import pandas as pd

filepath="Resources/budget_data.csv"
df=pd.read_csv(filepath)

diff_sum=0
for i in range(0,85):
    a=df.iloc[i,1]
    b=df.iloc[i+1,1]
    diff=b-a
    diff_sum=diff_sum+diff

diff=[]
for i in range(0,85):
    a=df.iloc[i,1]
    b=df.iloc[i+1,1]
    difference=b-a
    diff.append(difference)

Total_Months=df["Date"].count()
Total=df["Profit/Losses"].sum()
Total2= f"$ {Total}"
Average_change= f"$ {round((diff_sum/85),2)}"

Greatest_Increase_in_Profits_date= df.iloc[df["Profit/Losses"].idxmax(), 0]
Greatest_Increase_in_Profits_number=max(diff)
Greatesr_Increase_in_Profits=f"{Greatest_Increase_in_Profits_date} (${Greatest_Increase_in_Profits_number})"

Greatest_Decrease_in_Profits_date= df.iloc[df["Profit/Losses"].idxmin(), 0]
Greatest_Decrease_in_Profits_number=min(diff)
Greatesr_Decrease_in_Profits=f"{Greatest_Decrease_in_Profits_date} (${Greatest_Decrease_in_Profits_number})"


FA={
    "Financial Analysis": "",
    "Total_Months:": Total_Months,
    "Total:": Total2,
    "Average Change:": Average_change,
    "Greatest Increase in Profits:": Greatesr_Increase_in_Profits,
    "Greatest Decrease:": Greatesr_Decrease_in_Profits
    }

dftry= pd.DataFrame.from_dict(FA,orient="index")
dftry.to_csv('PyBank.txt', sep='\t')