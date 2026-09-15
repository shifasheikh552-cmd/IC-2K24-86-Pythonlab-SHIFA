name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
student = input("Are you a student? (True/False): ")

if student == "True":
    student = True
else:
    student = False

print("Name:", name, "Type:", type(name))
print("Age:", age, "Type:", type(age))
print("Height:", height, "Type:", type(height))
print("Student:", student, "Type:", type(student))
			
			
