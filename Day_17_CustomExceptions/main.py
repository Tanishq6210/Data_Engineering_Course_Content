import logging
from datetime import date

log_format = '%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s'

today = str(date.today())
# Syntax for using logging
logging.basicConfig(
    filename=f"{today}_main_app.log",
    level=logging.INFO,
    format=log_format,
    datefmt='%Y-%m-%d %H:%M:%S',
    force=True #For Collab
)

logging.warn("Application Started!")


# Bank application
withdraw_amount = -5000
student_mark = -1000000

# Valid integer, amount invalid

# Error -> ValueError, TypeError, FileNotFoundError

# Custom Exception Classes
class InvalidAmountError(Exception):
    pass

class InvalidMarkError(Exception):
    pass


# # if withdraw_amount <=0 :
# #     raise InvalidAmountError("Amount cannot be less than or equals to 0.")

# if student_mark <= -300 or student_mark >= 1000:
#     raise Exception("Marks should be more than -300.")

# Bad Pracices in Exception Handling
print("Doing divide by 0 operation")
logging.info("Doing divide by 0 operation")
dividend = 0
try:
    dividend = int(input("Enter dividend: "))
    result =  10 / dividend
except ZeroDivisionError:
    print(f"Division by 0 error, when divided with {dividend}")
    logging.error(
        f"Division by 0 occuered! {dividend}"
    )
logging.info("Completed divide by 0 operation")

# Logging Vs Printing
# print("Something is wrong")

logging.info("Application ended!")


# When to use print?
# 1. During learning
# 2. Quick debugging

# When to use logging?
# 1. Production system
# 2. Enterprise applications
# 3. Data pipelines