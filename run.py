from s3.user import read, delete, update, create

# Read Query
print("Read Data")
print(read("WHERE firstname = 'Devina'"))

# Output
# [['1274', 'Devina', 'Terencio', 'Devina.Terencio@yopmail.com', 'Devina.Terencio@gmail.com', 'doctor']]

# Update Query
print("Update Data")
update(
  "WHERE firstname = 'Devina'",
  {
    'lastname': 'Green'
  }
)

# Output
print(read("WHERE firstname = 'Devina'"))
# [['1274', 'Devina', 'Green', 'Devina.Terencio@yopmail.com', 'Devina.Terencio@gmail.com', 'doctor']]

# Delete Item
# print("Delete Item")
delete("WHERE firstname = 'Devina'")

# Output
print(read("WHERE firstname = 'Devina'"))
# []

# Create Item
print("Create Item")
create({
  'firstname': 'Devina',
  'lastname': 'Terencio',
  'email': 'Devina.Terencio@yopmail.com',
  'email2': 'Devina.Terencio@gmail.com',
  'profession': 'doctor'
})

# Output
print(read("WHERE firstname = 'Devina'"))
# [['2100', 'Devina', 'Terencio', 'Devina.Terencio@yopmail.com', 'Devina.Terencio@gmail.com', 'doctor']]
