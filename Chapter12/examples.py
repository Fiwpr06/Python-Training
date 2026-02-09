# If/elif/else
status = "gold"
if status == "bronze":
    discount = 5
elif status == "silver":
    discount = 10
elif status == "gold":
    discount = 15
else:
    discount = 0
print(f"Discount: {discount}%", end="\n\n")

# One-liner if
age = 20
category = "adult" if age >= 18 else "minor"
print(f"Category: {category}", end="\n\n")

# Nested if
score = 85
if score >= 60:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "D"
else:
    grade = "F"
print(f"Grade: {grade}", end="\n\n")

# Match-case

status_code = 404
match status_code:
    case 200:
        message = "OK"
    case 404:
        message = "Not Found"
    case 500:
        message = "Internal Server Error"
    case _:
        message = "Unknown Status"
        
print(f"Status Message: {message}", end="\n\n")

# Pattern matching with guards
value = 15
match value:
    case x if x < 10:
        category = "Low"
    case x if 10 <= x < 20:
        category = "Medium"
    case _:
        category = "High"
print(f"Value Category: {category}", end="\n\n")

# Dictionary-based switch
branch = {"Main": "You selected the Main branch.", "Dev": "You selected the Dev branch.,", "Test": "You selected the Test branch."}
message = branch.get("Dev", "Unknown branch selected.")
print(f"Branch Message: {message}", end="\n\n")

# Short-circuit evaluation
user_input = ""
result = user_input or "Default Value"
print(f"Result: {result}")
      
actice = "running" and 234
print(f"Active: {actice}", end="\n\n")