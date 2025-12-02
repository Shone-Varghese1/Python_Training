import pandas as pd

df = pd.DataFrame({
    "Name": ["Aisha", "Rahul", "John", "Neha", "Imran"],
    "Marks": [85, 92, 78, 65, 55],
    "City": ["Mumbai", "Delhi", "Chennai", "Bangalore", "Hyderabad"],
    "Age": [22, 25, 23, 21, 24]
})
df2 = df.copy()
df2.loc[2,"City"]=None
print(df2)
print(df2.isnull().sum())

df2_filled=df2.fillna("Unknown")
print(df2_filled)