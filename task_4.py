def validate_recharge():
    available_plans = [199, 299, 399, 599]

    while True:
        try:
            recharge_amt = int(input("Enter recharge amount: ₹"))

            if recharge_amt < 50:
                print("Recharge amount must be at least ₹50.")
            elif recharge_amt not in available_plans:
                print("Invalid plan selected. Available plans:", available_plans)
            else:
                print("Recharge successful for ₹", recharge_amt)
                break

        except ValueError:
            print("Please enter a valid numeric amount.")


validate_recharge()




def check_inventory(stock_data):
    for product, quantity in stock_data.items():
        if quantity < 15:
            print(product, "→ Reorder Alert")
        else:
            print(product, "→ Stock OK")


# Sample Data
inventory = {
    "Laptop": 11,
    "Mouse": 25,
    "Keyboard": 18,
    "Monitor": 13
}

# Function Call
check_inventory(inventory)




def evaluate_result(marks_list):
    total_marks = 0

    for mark in marks_list:
        total_marks += mark

    average = total_marks / len(marks_list)

    print("Average Marks:", average)

    if average >= 50:
        return "Pass"
    else:
        return "Fail"


# Sample Data
marks = [65, 55, 72, 45]

result = evaluate_result(marks)
print("Result:", result)




def calculate_fare(distance, peak):
    base_fare = 50
    per_km_rate = 12

    total_fare = base_fare + (distance * per_km_rate)

    if peak.lower() == "yes":
        total_fare += total_fare * 0.25   # 25% extra

    return total_fare


while True:
    km = float(input("Enter distance (in km): "))
    peak_time = input("Is it peak hour? (yes/no): ")

    fare = calculate_fare(km, peak_time)
    print("Total Fare: ₹", fare)

    retry = input("Do you want to calculate again? (yes/no): ")
    if retry.lower() != "yes":
        break




def check_eligibility(attendance_list):
    present_days = 0

    for status in attendance_list:
        if status == "P":
            present_days += 1

    percentage = (present_days / len(attendance_list)) * 100

    print("Attendance Percentage:", percentage, "%")

    if percentage >= 75:
        return "Eligible"
    else:
        return "Not Eligible"


# Sample Data
attendance = ["P", "A", "P", "P", "P", "A", "P", "P"]

status = check_eligibility(attendance)
print("Eligibility Status:", status)





def check_password_strength(password):
    has_digit = False
    has_special = False
    special_chars = "@#$"

    if len(password) < 8:
        return "Weak Password (Minimum 8 characters required)"

    for char in password:
        if char.isdigit():
            has_digit = True
        if char in special_chars:
            has_special = True

    if has_digit and has_special:
        return "Strong Password"
    else:
        return "Weak Password (Include at least one digit and one special character)"

# Test
user_password = input("Enter your password: ")
print(check_password_strength(user_password))
