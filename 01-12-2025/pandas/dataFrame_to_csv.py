import pandas as pd


data={
    "Name": ["Shone","Ravi","Hari"],
    "Marks":[75,87,98],
    "city":["mumbai","Delhi","chennai"]
}
df1 = pd.DataFrame(data)
df1.to_csv("data.csv", index=False)
print("csv file created")

