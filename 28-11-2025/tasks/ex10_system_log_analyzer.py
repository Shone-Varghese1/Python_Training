# 10. System Log Analyzer
# Read system.log and count:
# number of ERROR lines
# number of WARNING lines
# number of INFO lines
# Write the summary into log_summary.txt .
error_count=0
warning_count=0
info_count=0
with open("./textfiles/system.log","r") as f:
    for line in f.readlines():
        data=line.split()
        if "[INFO]"  in data:
            info_count+=1
        elif "[WARNING]" in data:
            warning_count+=1
        elif "[ERROR]" in data:
            error_count+=1
        else:
            continue
with open("./textfiles/system_log_summary.txt","w") as f:
    f.write(f"Error count : {error_count}\nWarning count : {warning_count}\nInfo count : {info_count}\n\n")



