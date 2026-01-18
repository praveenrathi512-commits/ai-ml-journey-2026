# Tuples Example (unchangable data)

user_location = (21.7453, 72.8211)
print("latitude:", user_location[0])
print("longitude:", user_location[1])


# Set Example (unorderd data & non duplicates)

emails = ["a@gmail.com", "b@gmail.com", "c@gmail.com", "b@gmail.com"]
unique_emails = set(emails)
print(unique_emails)

# Membership check

allowed_users = {"Admin", "Editor", "Viewer"}  # Set Syntax
role = "Admin"
if role in allowed_users:
  print("Access granted")


# Real world thinking

dataset_features = ("age", "salary", "experience")
print(dataset_features)
