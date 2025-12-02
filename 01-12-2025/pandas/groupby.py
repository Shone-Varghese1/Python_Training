import pandas as pd

df = pd.DataFrame({
    "Name": ["Aisha", "Rahul", "John", "Neha", "Imran"],
    "Marks": [85, 92, 78, 65, 55],
    "City": ["Mumbai", "Delhi", "Chennai", "Bangalore", "Hyderabad"],
    "Age": [22, 25, 23, 21, 24]
})


city_count=df.groupby("City")["Name"].count()
print(city_count)
avg_marks = df.groupby("City")["Marks"].mean()
print(avg_marks)