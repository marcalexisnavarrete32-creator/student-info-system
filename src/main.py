"""Student Information System - CLI entry point. Run from repo root: python src/main.py"""
import logging

from services.student_service import StudentService
from utils.config import load_config
from utils.logger import setup_logging


class StudentInformationSystem:
    def __init__(self):
        config = load_config()
        setup_logging(config["log_file"], config["log_level"])
        self.student_service = StudentService(config["data_file"])
        self.logger = logging.getLogger(__name__)

    def display_menu(self):
        print("\n=== Student Information System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. View Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

    def add_student(self):
        print("\n--- Add New Student ---")
        name = input("Name: ").strip()
        email = input("Email: ").strip()
        course = input("Course: ").strip()
        year_level = input("Year Level: ").strip()
        if not (name and email and course and year_level):
            print("All fields are required.")
            return
        try:
            student = self.student_service.add_student({
                "name": name, "email": email,
                "course": course, "year_level": year_level,
            })
            self.logger.info(f"Added student: {student['student_id']}")
            print(f"Student added successfully! ID: {student['student_id']}")
        except Exception as e:
            self.logger.error(f"Error adding student: {e}")
            print("Error adding student.")

    def view_all_students(self):
        print("\n--- All Students ---")
        students = self.student_service.get_all_students()
        if not students:
            print("No students found.")
            return
        for s in students:
            print(f"ID: {s['student_id']}, Name: {s['name']}, "
                  f"Email: {s['email']}, Course: {s['course']}, Year: {s['year_level']}")

    def view_student(self):
        student = self.student_service.get_student(input("Enter Student ID: ").strip())
        if student:
            print("\nStudent Details:")
            for key, value in student.items():
                print(f"  {key}: {value}")
        else:
            print("Student not found.")

    def update_student(self):
        student_id = input("Enter Student ID to update: ").strip()
        if not self.student_service.get_student(student_id):
            print("Student not found.")
            return
        print("Leave a field blank to keep its current value.")
        fields = {"name": "Name", "email": "Email", "course": "Course", "year_level": "Year Level"}
        updates = {}
        for key, label in fields.items():
            value = input(f"New {label}: ").strip()
            if value:
                updates[key] = value
        if not updates:
            print("Nothing to update.")
            return
        try:
            self.student_service.update_student(student_id, updates)
            self.logger.info(f"Updated student: {student_id}")
            print("Student updated successfully!")
        except Exception as e:
            self.logger.error(f"Error updating student: {e}")
            print("Error updating student.")

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ").strip()
        if input(f"Delete {student_id}? (y/n): ").strip().lower() != "y":
            print("Cancelled.")
            return
        try:
            if self.student_service.delete_student(student_id):
                self.logger.info(f"Deleted student: {student_id}")
                print("Student deleted.")
            else:
                print("Student not found.")
        except Exception as e:
            self.logger.error(f"Error deleting student: {e}")
            print("Error deleting student.")

    def run(self):
        actions = {
            "1": self.add_student, "2": self.view_all_students,
            "3": self.view_student, "4": self.update_student,
            "5": self.delete_student,
        }
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ").strip()
            if choice == "6":
                print("Goodbye!")
                break
            action = actions.get(choice)
            if action:
                action()
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    StudentInformationSystem().run()
