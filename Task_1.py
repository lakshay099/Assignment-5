students_details={"Lakshay":95,"Alice":78,"John":88,"Victor":72,"Vijay":66}
student_name=input("Enter the student's name:").capitalize()

if student_name in students_details:
    print(f"{student_name}'s marks:{students_details[student_name]} ")
else:
    print("Student not found")
