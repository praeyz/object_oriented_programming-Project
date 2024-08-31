from typing import Union,List

class Person:
    
    def __init__(self, name, id_number) -> None:
        self.name = name 
        self.id_number = id_number 

    def __str__ (self) -> str:
        return f" Name : {self.name}, id_number : {self.id_number}"
    
    def __repr__ (self) -> str:
        return f" Name : {self.name}, id_number : {self.id_number}"
    

class Student(Person):
    def __init__(self, name : str, id_number : int, major: str) -> None:
        super().__init__(name, id_number)
        self.major = major 
    
    def __str__ (self) -> str:
        return f"Student data : (Name: {self.name}, ID: {self.id_number}, Major: {self.major})"
    
    def __repr__ (self) -> str:
        return f"Student data : (Name: {self.name}, ID: {self.id_number}, Major: {self.major})"


class Instructor(Person):
    def __init__(self, name, id_number, department) -> None:
        super().__init__(name, id_number)
        self.department = department 
    
    def __str__ (self) -> str:
        return f" Instructor(Name : {self.name}, id_number : {self.id_number}\n department : {self.department})"
    def __repr__ (self) -> str:
        return f" Instructor (Name : {self.name} id_number : {self.id_number}\n department : {self.department})"


class Course:
    def __init__(self, course_name, course_id) -> None:
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = []   

    def __str__ (self) -> str:
        return f" course : {self.course_name},  course_id : {self.course_id}"
        
    def __repr__ (self) -> str:
        return f" course : {self.course_name},  course_id : {self.course_id}"
    
    def add_students_to_course(self, student :Student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            return f"Student {student.name} has enrolled to {self.course_name}"
        else:
            return f"Student {student.name} is already enrolled in {self.course_name}"
        
    def remove_student_from_course(self, student: Student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            return f"Student {student.name} has been removed from {self.course_name}"
        else:
            return f"Student {student.name} is not enrolled in {self.course_name}"

    def list_enrolled_students(self):
        return [str(student) for student in self.enrolled_students]


class Enrollment:
    def __init__(self, student :Student, course : Course, grade = None) -> None:       
        self.student = student
        self.course = course
        self.grade = grade 

    def __str__ (self) -> str:
        return f" the student with details: {self.student.name} enrolled in : {self.course.course_name}, and achived a grade of: {self.grade}"
    
    def __repr__ (self) -> str:
        return f" the student with details: {self.student.name} enrolled in : {self.course.course_name}, and achived a grade of: {self.grade}"
    
    def assign_grade(self, grade):
        self.grade = grade



class StudentManagementSystem:
    def __init__(self) -> None:
        self.students = []
        self.instructors = []
        self.courses = []
        self.enrollments = []   
        self.grades = {}       
        self.enrollment_fee = False

    def add_student(self, student) -> str:
        self.students.append(student)

    def remove_student(self, id_number) -> str:
        for student in self.students:
            if student.id_number == id_number:
                self.students.remove(student)
                return f"student with ID {id_number} has been removed."
            
        return f"found no studnet"

    def find_student(self, id_number):
        for i, found_student in enumerate(self.students):
            if found_student.id_number == id_number:
                return i, found_student
        return None

    def update_student(self, student : Student )-> str: 
        i, _ = self.find_student(student.id_number)
        self.students[i] = student
        return f"data has been updated with {student}"
    
    def show_student(self):
        return self.students    

    def add_instructor(self, instructor) -> str:
        return self.instructors.append(instructor)

    def remove_instructor(self, id_number) -> str:
        for instructor in self.instructors:
            if instructor.id_number == id_number:
                self.instructors.remove(instructor)  
                return f"instructor with ID {id_number} has been removed."
        return None       

    def find_instructor(self, id_number):
        for i, found_instructor in enumerate(self.instructors):
            if found_instructor.id_number == id_number:
                return i, found_instructor
        return None

    def update_instructor(self, instructor : Instructor )-> str:
        i, _ = self.find_instructor(instructor.id_number)
        self.instructor[i] = instructor
        return f"data has been updated with {instructor}"
    
    def show_instructors(self):
        return self.instructors

    def add_courses(self, courses):
        self.courses.append(courses)
    
    def remove_course(self, course_id):
        for course in self.courses:
            if course.id_number == course_id:
                self.courses.remove(course)
                return f"course with ID {course_id} has been removed."

    def find_course(self, course_id):
        for i, found_course in enumerate(self.courses):
            if found_course.course_id == course_id:
                return i, found_course
        return None
    
    def update_course(self, course : Course )-> str:
        i, _ = self.find_course(course.course_id)
        self.courses[i] = course
        return f"data has been updated with {course}"
    
    def enroll_student_in_courses(self,student :Student, *courses:Course) -> str:
        for course in courses:
            enroll = Enrollment(student, course)   
            self.enrollments.append(enroll)                
            if student.id_number not in self.grades:
                self.grades[student.id_number] = {}
            self.grades[student.id_number][course.course_name] = None
        return f"{student.name} has been enrolled in {len(courses)} courses "

    def show_enrollment(self):
        for enrollment in self.enrollments:
            print(enrollment)

    def assign_grade(self, student : Student, course :Course, grade:int):
        for enrollment in self.enrollments:
            if enrollment.student == student and enrollment.course == course:
                enrollment.assign_grade(grade)
                self.grades[student.id_number][course.course_name] = grade    

        return f"Grade {grade} assigned to student {student.name} for course {course.course_name}."
        
    def students_grades(self):
        return self.grades

    def get_student_grades(self, student_id): 
        return self.grades.get(student_id)
    
    def studentlist_in_course(self,course_id):  
        course_object = next((course for course in self.courses if course.course_id == course_id), None)
        print(course_object)
        if course_object:
            enrolled_students = course_object.list_enrolled_students()             
            print(enrolled_students)
            if enrolled_students:
                return enrolled_students
            else:
                return f"No students are enrolled in {course_object.course_name}."
        else:
            return "Course not found."

    def student_course_list(self,student_id):   
        student_object = next((student for student in self.students if student.id_number == student_id), None)

        if student_object:
            enrolled_courses = []
            for course in self.courses:
                if student_object in course.enrolled_students:
                    enrolled_courses.append(course.course_name)

            if enrolled_courses:
                return enrolled_courses
            else:
                return f"Student {student_object.name} is not enrolled in any courses."
        else:
            return "Student not found."        
    






        




