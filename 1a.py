
name = input("Enter student name: ")
dob = input("Enter date of birth (DD/MM/YYYY): ")
reg_no = input("Enter registration number: ")
department = input("Enter department: ")
for i in range(1, 6):
    mark = int(input("Enter marks for subject {i}: "))
    marks=[]
    total_marks = sum(marks)
percentage = total_marks / 5
print("\n--- Student Details ---")
print(f"Name       : {name}")
print(f"DOB        : {dob}")
print(f"Reg No     : {reg_no}")
print(f"Department : {department}")
print(f"Marks      : {marks}")
print(f"Total Marks: {total_marks}")
print(f"Percentage : {percentage:.2f}%")
if percentage >= 75:
    print("Excellent performance! Keep it up.")
elif percentage >= 50:
    print("Good work, but there’s room for improvement.")
else:
    print("Needs improvement. Focus more on studies.")