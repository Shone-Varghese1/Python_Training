import pandas as pd

df=pd.DataFrame({
    "Name":["shone","Rahul","John"],
    "Marks":[85,92,78],
    "city":["Mumbai","Delhi","Chennai"]
})

df.to_json("students.json",orient="records",indent=4)
print("JSon file created")

df2=pd.read_json("students.json")
print(df2)