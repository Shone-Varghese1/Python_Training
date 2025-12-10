# Build a function log_error(message) that writes errors into error.log with timestamps.
# Simulate errors by calling the function 5 times.
import datetime
timestamp=datetime.datetime.now()

error_dict={
    1:"invalid Login",
    2:"Invalid Password",
    3:"session expired",
    4:"Page not found",
    5:"no internet connection"
}
def log_error(str1):
    with open("./textfiles/error_log.txt", 'a') as f:
        f.write(f"{str1}-{timestamp}\n")
for v in error_dict.values():
    log_error(v)
