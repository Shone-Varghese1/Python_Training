# raw_data="""EmployeeID,Name,Department,Title,Email,Phone,Location,Salary,HireDate,Manager
# E001,Jordan Wilson,Engineering,Software Engineer,jordan.wilson@example.com,+91-9876543210,Kochi,850000,2019-06-12,Cameron Brown
# E002,Alex Davis,Engineering,Senior Software Engineer,alex.davis@company.com,+91-9876543211,Bengaluru,1200000,2018-03-20,Jamie Anderson
# E003,Taylor Moore,HR,HR Manager,taylor.moore@corp.org,+91-9876543212,Kochi,950000,2020-01-15,Drew Johnson
# E004,Morgan Smith,Sales,Account Executive,morgan.smith@example.com,+91-9876543213,Chennai,700000,2021-09-01,Jordan Brown
# E005,Riley Anderson,Marketing,Content Strategist,riley.anderson@company.com,+91-9876543214,Mumbai,780000,2017-11-10,Casey Miller
# E006,Cameron Thomas,Finance,Financial Analyst,cameron.thomas@corp.org,+91-9876543215,Pune,820000,2016-08-25,Alex Davis
# E007,Jamie Taylor,Engineering,DevOps Engineer,jamie.taylor@example.com,+91-9876543216,Kochi,980000,2019-05-30,Morgan Smith
# E008,Drew Johnson,Support,Support Specialist,drew.johnson@company.com,+91-9876543217,Hyderabad,600000,2022-02-18,Riley Anderson
# E009,Casey Miller,Design,UX Designer,casey.miller@corp.org,+91-9876543218,Kochi,900000,2020-07-22,Taylor Moore
# E010,Alex Brown,Engineering,QA Engineer,alex.brown@example.com,+91-9876543219,Bengaluru,820000,2018-12-12,Cameron Thomas
# E011,Jordan Smith,Admin,Staff/Assistant,jordan.smith@company.com,+91-9876543220,Kochi,550000,2015-03-03,Drew Johnson
# E012,Taylor Anderson,Operations,Operations Manager,taylor.anderson@corp.org,+91-9876543221,Delhi,1100000,Jamie Taylor
# E013,Morgan Davis,Engineering,Data Engineer,morgan.davis@example.com,+91-9876543222,Kochi,1050000,2021-01-04,Riley Anderson
# E014,Riley Wilson,Sales,Sales Manager,riley.wilson@company.com,+91-9876543223,Mumbai,1150000,2017-04-14,Casey Miller
# E015,Cameron Brown,Marketing,SEO Specialist,cameron.brown@corp.org,+91-9876543224,Chennai,730000,2019-10-02,Alex Davis
# E016,Jamie Moore,Engineering,ML Engineer,jamie.moore@example.com,+91-9876543225,Bengaluru,1300000,2020-03-29,Morgan Smith
# E017,Drew Taylor,Finance,Senior Accountant,drew.taylor@company.com,+91-9876543226,Kochi,900000,2018-02-05,Taylor Anderson
# E018,Casey Johnson,Support,Service Desk Lead,casey.johnson@corp.org,+91-9876543227,Pune,750000,2016-06-11,Riley Wilson
# E019,Alex Miller,Design,Product Designer,alex.miller@example.com,+91-9876543228,Hyderabad,980000,2022-08-23,Cameron Brown
# """
#
#
# with open("employees.csv", "w", encoding="utf-8",newline="") as f:
#     f.write(raw_data)

# print("employees.csv created!")

import pandas as pd

df = pd.read_csv("employees.csv")
data_list = df.to_dict(orient="records")
print(data_list[:3])
