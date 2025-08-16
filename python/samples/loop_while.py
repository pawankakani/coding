total_students = int(input("How many students are in class : "))
total_marks = int(input("Enter total marks : "))

# Variable to check loop condition
student_counter = 1
while student_counter <= total_students: ## <1>
    marks_received = int(input("Enter the marks received by student " + str(student_counter) + " : "))
    percentage = (marks_received/total_marks)*100
    print("Percentage :", percentage)
    student_counter = student_counter + 1 ## <2>

print("Loop has finished") ## <3>
