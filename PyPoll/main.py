import pandas as pd

filepath="Resources/election_data.csv"

df=pd.read_csv(filepath)

Total_votes=df["Voter ID"].count() #1

#2 This is the middle part of the content, making it a dataframe
df_group=df.groupby(["Candidate"])
percentage=round((df_group["Voter ID"].count()/Total_votes),4)
percentage=percentage.map("{:.2%}".format)
percentage=pd.DataFrame(percentage).reset_index()
df1=percentage.rename(columns={"Voter ID": "Percentage"})
df1
total_number=df_group["Voter ID"].count()
total_number=pd.DataFrame(total_number).reset_index()
df2=total_number.rename(columns={"Voter ID": "Total"})
df2
dft=pd.merge(df1,df2,on="Candidate")
dft=dft.sort_values("Total",ascending=False)
dft.reset_index(drop=True,inplace=True)

Winner=dft.iloc[dft["Total"].idxmax(),0] #3


dft['Candidate'] = [f'{x}:' for x in dft["Candidate"]]
#dft["Candidate"] = dft["Candidate"].astype(str)+":"
dft["Total"]=[f'({x})' for x in dft['Total']]


#add the "#1 Total Votes" and "#3 Winner" to the #2 dataframe
dft.loc[-2]=["Election Results","",""]
dft.loc[-1] = ["Total Votes:", Total_votes, ""]  
dft.loc[4] = ["Winner:",Winner,""]
dft = dft.sort_index()



dft.to_csv('PyPoll.txt', sep='\t',index=False,header=False)
