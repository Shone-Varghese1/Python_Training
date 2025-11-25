emp_details={
"e1": {"dept": "IT"},
"e2": {"dept": "HR"},
"e3": {"dept": "IT"},
"e4": {"dept": "IT"},
"e5": {"dept": "Sales"}
}

dept_count={}
for e,dept in emp_details.items():
    dept=dept.get("dept")
    if dept not in dept_count:
        dept_count[dept]=1
    else:
        dept_count[dept]+=1
print(dept_count)

