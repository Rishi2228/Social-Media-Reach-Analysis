import pandas as pd 
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\LENOVO\Downloads\Instagram_Reach_Analysis_data.csv")
df.head()
df.info()
df.describe()
df.isnull().sum()
#distribution of impression 
plt.figure(figsize=(8,5))
plt.hist(df["Impressions"], bins=20)
plt.title ('distribution of impression')
plt.xlabel('impression')
plt.ylabel('frequency')
plt.show()
#likes vs impressions
plt.figure(figsize=(8,5))
plt.scatter(df['Likes'],df['Impressions'])
plt.title('Likes vs Impressions')
plt.xlabel('Likes')
plt.ylabel('Impressions')
plt.show()
#comments vs impressions
plt.figure(figsize=(8,5))
plt.scatter(df['Comments'],df['Impressions'])
plt.title('Comments vs Impressions')
plt.xlabel('Comments')
plt.ylabel('Impressions')
plt.show()
#shares vs impressions
plt.figure(figsize=(8,5))
plt.scatter(df['Shares'],df['Impressions'])
plt.title('Shares vs Impressions')
plt.xlabel('Shares')
plt.ylabel('Impressions')
plt.show()
#Top 10 posts
top10=df.sort_values(by='Impressions',ascending=False).head(10)

plt.figure(figsize=(10,5))
plt.bar(range(len(top10)), top10['Impressions'])
plt.title('Top 10 post by Impressions')
plt.xlabel('Post number')
plt.ylabel('Impressions')
plt.show()
#correlation matrix
corr=df.corr(numeric_only=True)
print(corr)
#engagement rate
df['Engagement']=(df['Likes']+df['Comments']+df['Shares']+df['Saves'])
print(df['Engagement'].head(150))
df.to_csv("Instagram_Reach_Analysis_Final.csv", index=False)
