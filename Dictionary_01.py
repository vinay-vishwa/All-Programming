student = {
    "name":"Vinay",
    "Roll_No.":"21",
    "Course": "MCA",
    "Marks": 90
}
print("Dictionary :",student)
print("\nDictionary elements:")
for key,value in student.items():
    print(key,":",value)
print("\nName:",student.get("Name"))
print("keys:",student.keys())
print("Values",student.values())
print("Items",student.items())
student.update({"marks":90,"city":"Lucknow"})
print("\nDictionary after update:")
for key, value in student.items():
    print(key,":",value)