phonebook = {
    "Alice": "9876543210",
    "Bob": "9123456780"
}
phonebook["Charlie"] = "9999999999"

print("Bob's number is:", phonebook.get("Bob", "Not found"))

phonebook["Alice"] = "1111111111"

for name, number in phonebook.items():
    print(f"{name}: {number}")

del phonebook["Charlie"]
print("After Deleting Charlie's :")

for name, number in phonebook.items():
    print(f"{name}: {number}")

