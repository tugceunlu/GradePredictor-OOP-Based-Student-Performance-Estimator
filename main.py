from models.student import Student
from models.course import Course
from models.predictor import Predictor

def get_student_input():
    name = input("Enter student name: ")
    study_hours = float(input(f"How many hours did {name} study? "))
    midterm_score = float(input(f"What was {name}'s midterm score (out of 100)? "))
    attendance = float(input(f"What was {name}'s attendance rate (in %)? "))
    return Student(name, study_hours, midterm_score, attendance)

def main():
    print("📘 Course Performance Predictor")
    course_name = input("Enter course name: ")
    course = Course(course_name)

    students = []
    num_students = int(input("How many students do you want to evaluate? "))

    for _ in range(num_students):
        print("\n--- New Student ---")
        student = get_student_input()
        students.append(student)

    predictor = Predictor()
    predictor.train(students)

    print(f"\n📊 Predicted final grades for {course.name}:")
    for student in students:
        predicted_grade = predictor.predict(student)
        print(f"{student.name}: {predicted_grade:.2f}")

if __name__ == "__main__":
    main()
