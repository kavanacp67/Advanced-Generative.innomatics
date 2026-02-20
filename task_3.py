employees = {
    "Ravi": 92,
    "Anita": 88,
    "Kiran": 92,
    "Suresh": 85
}

# Find highest score
highest_score = max(employees.values())

# Find all employees with highest score
top_performers = []

for name, score in employees.items():
    if score == highest_score:
        top_performers.append(name)

print("Top Performers Eligible for Bonus:", ", ".join(top_performers), f"(Score: {highest_score})")





import string

query = "Buy mobile phone buy phone online"

# Convert to lowercase
query = query.lower()

# Remove punctuation
query = query.translate(str.maketrans("", "", string.punctuation))

words = query.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Display words searched more than once
result = {}

for word, count in frequency.items():
    if count > 1:
        result[word] = count

print(result)




sensor_readings = [3, 4, 7, 8, 10, 12, 5]

valid_readings = []

for index, value in enumerate(sensor_readings):
    if value % 2 == 0:
        valid_readings.append((index, value))

print("Valid Sensor Readings (Hour, Value):")
print(valid_readings)





emails = [
    "ravi@gmail.com",
    "anita@yahoo.com",
    "kiran@gmail.com",
    "suresh@gmail.com",
    "meena@yahoo.com"
]

domain_count = {}

for email in emails:
    domain = email.split("@")[1]
    if domain in domain_count:
        domain_count[domain] += 1
    else:
        domain_count[domain] = 1

total_users = len(emails)

for domain, count in domain_count.items():
    percentage = (count / total_users) * 100
    print(f"{domain}: {percentage:.0f}%")






    sales = [1200, 1500, 900, 2200, 1400, 3000]

average_sales = sum(sales) / len(sales)

threshold = average_sales * 1.30

for day, value in enumerate(sales, start=1):
    if value > threshold:
        print(f"Day {day}: {value}")






user_ids = ["user1", "user2", "user1", "user3", "user1", "user3"]

id_count = {}

for user in user_ids:
    if user in id_count:
        id_count[user] += 1
    else:
        id_count[user] = 1

for user, count in id_count.items():
    if count > 1:
        print(f"{user} → {count} times")
