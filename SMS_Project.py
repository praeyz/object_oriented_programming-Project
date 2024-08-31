from typing import List, Optional, Tuple, Dict, Union

class Person:
    """
    Represents a generic person with a name and an ID number.
    
    Attributes:
        name (str): The name of the person.
        id_number (int): The ID number of the person.

    Methods:
        __str__(): Returns a human-readable string representation of the person's details.
        __repr__(): Returns a string representation of the person's details for debugging.
    """

    def __init__(self, name: str, id_number: int) -> None:
        self.name: str = name
        self.id_number: int = id_number

    def __str__(self) -> str:
        return f"Name: {self.name}, ID Number: {self.id_number}"
    
    def __repr__(self) -> str:
        return f"Name: {self.name}, ID Number: {self.id_number}"
    

class Student(Person):
    """
    Represents a student, inheriting from Person, with an additional attribute for their major.
    
    Attributes:
        major (str): The major field of study for the student.

    Methods:
        __str__(): Returns a human-readable string representation of the student's details.
        __repr__(): Returns a string representation of the student's details for debugging.
    """

    def __init__(self, name: str, id_number: int, major: str) -> None:
        super().__init__(name, id_number)
        self.major: str = major 
    
    def __str__(self) -> str:
        return f"Student data: (Name: {self.name}, ID: {self.id_number}, Major: {self.major})"
    
    def __repr__(self) -> str:
        return f"Student data: (Name: {self.name}, ID: {self.id_number}, Major: {self.major})"


class Instructor(Person):
    """
    Represents an instructor, inheriting from Person, with an additional attribute for their department.
    
    Attributes:
        department (str): The department to which the instructor belongs.

    Methods:
        __str__(): Returns a human-readable string representation of the instructor's details.
        __repr__(): Returns a string representation of the instructor's details for debugging.
    """

    def __init__(self, name: str, id_number: int, department: str) -> None:
        super().__init__(name, id_number)
        self.department: str = department 
    
    def __str__(self) -> str:
        return f"Instructor(Name: {self.name}, ID Number: {self.id_number}, Department: {self.department})"
    
    def __repr__(self) -> str:
        return f"Instructor(Name: {self.name}, ID Number: {self.id_number}, Department: {self.department})"


class Course:
    """
    Represents a course with a name and an ID, and manages the enrollment of students.
    
    Attributes:
        course_name (str): The name of the course.
        course_id (int): The unique identifier for the course.
        enrolled_students (List[Student]): A list of students enrolled in the course.

    Methods:
        __str__(): Returns a human-readable string representation of the course's details.
        __repr__(): Returns a string representation of the course's details for debugging.

        add_students_to_course(student: Student): Takes a student object and enrolls them into the course.
        Args:
            student (Student): The student to be enrolled in the course.
        Returns:
            str: A message indicating whether the student was successfully enrolled or already enrolled.

        remove_student_from_course(student: Student): Removes a student from the course.
        Args:
            student (Student): The student to be removed from the course.
        Returns:
            str: A message indicating whether the student was successfully removed or is not an enrolled student.

        list_enrolled_students(): Returns a list of string representations of all enrolled students.
    """

    def __init__(self, course_name: str, course_id: int) -> None:
        self.course_name: str = course_name
        self.course_id: int = course_id
        self.enrolled_students: List[Student] = []  # List of students enrolled in the course

    def __str__(self) -> str:
        return f"Course: {self.course_name}, Course ID: {self.course_id}"
        
    def __repr__(self) -> str:
        return f"Course: {self.course_name}, Course ID: {self.course_id}"
    
    def add_students_to_course(self, student: Student) -> str:
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            return f"Student {student.name} has enrolled in {self.course_name}"
        else:
            return f"Student {student.name} is already enrolled in {self.course_name}"
        
    def remove_student_from_course(self, student: Student) -> str:
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            return f"Student {student.name} has been removed from {self.course_name}"
        else:
            return f"Student {student.name} is not enrolled in {self.course_name}"

    def list_enrolled_students(self) -> List[str]:
        return [str(student) for student in self.enrolled_students]


class Enrollment:
    """
    Represents enrollment of a student in a course, including their grade.
    
    Attributes:
        student (Student): The student enrolled in the course.
        course (Course): The course in which the student is enrolled.
        grade (Optional[int]): The grade assigned to the student for the course.

    Methods:
        __str__(): Returns a human-readable string representation of the enrollment details.
        __repr__(): Returns a string representation of the enrollment details for debugging.
        assign_grade(grade: int): Assigns a grade to the student for the course.
    """

    def __init__(self, student: Student, course: Course, grade: Optional[int] = None) -> None:
        self.student: Student = student
        self.course: Course = course
        self.grade: Optional[int] = grade

    def __str__(self) -> str:
        return f"The student {self.student.name} is enrolled in {self.course.course_name} with a grade of {self.grade}"
    
    def __repr__(self) -> str:
        return f"The student {self.student.name} is enrolled in {self.course.course_name} with a grade of {self.grade}"
    
    def assign_grade(self, grade: int) -> None:
        """
        Assigns a grade to the student for the course.
        
        Args:
            grade (int): The grade to assign to the student.
        """
        self.grade = grade


class StudentManagementSystem:
    """
    Manages students, instructors, courses, and enrollments in the system.
    
    Attributes:
        Returns a list of all students in the system, instructors, courses, enrollments and grades in the system.
    
    Method:
    
        add_student(student: Student): Adds student object to the list.
        remove_student(id_number: int): Removes a student from the student list using the student ID number.
        find_student(id_number: int): Finds a student in the student list using the student ID number.
        update_student(student: Student): Replaces student details in the system
        show_student(self): Returns the list of all the students in the system.
        add_instructor(instructor: Instructor): Adds an instructor to the system.
        remove_instructor(id_number: int): Removes an instructor from the system by their ID number.
        find_instructor(id_number: int): Finds an instructor by their ID number.
        update_instructor(instructor: Instructor): Updates an instructor's details in the system.
        show_instructors(): Returns a list of all instructors in the system.
        add_courses(course: Course): Adds a course to the system.
        remove_course(course_id: int): Removes a course from the system by its course ID.
        find_course(course_id: int): Finds a course by its course ID.
        update_course(course: Course): Updates a course's details in the system.
        enroll_student_in_courses(student: Student, *courses: Course): Enrolls a student in one or more courses.
        show_enrollment(): Prints all enrollments in the system.
        assign_grade(student: Student, course: Course, grade: int): Assigns a grade to a student for a specific course.
        students_grades(): Returns a dictionary of all students and their grades.
        get_student_grades(student_id: int): Returns the grades for a particular student by their ID.
        studentlist_in_course(course_id: int): Retrieves a list of students enrolled in a specific course by its ID.
        student_course_list(student_id: int): Retrieves a list of courses a specific student is enrolled in by their ID.
        """

    def __init__(self) -> None:
        self.students: List[Student] = []
        self.instructors: List[Instructor] = []
        self.courses: List[Course] = []
        self.enrollments: List[Enrollment] = []
        self.grades: Dict[int, Dict[str, Optional[int]]] = {}  # {"student_id": {"course_name": grade}}

    def add_student(self, student: Student) -> None:
        """
        Adds a student to the system.
        
        Args:
            student (Student): The student to be added to the system.
        """
        self.students.append(student)

    def remove_student(self, id_number: int) -> str:
        """
        Removes a student from the system by their ID number.
        
        Args:
            id_number (int): The ID number of the student to be removed.
        
        Returns:
            str: A message indicating whether the student was successfully removed or not found.
        """
        for student in self.students:
            if student.id_number == id_number:
                self.students.remove(student)
                return f"Student with ID {id_number} has been removed."
        return f"No student found with ID {id_number}"

    def find_student(self, id_number: int) -> Optional[Tuple[int, Student]]:
        """
        Finds a student by their ID number.
        
        Args:
            id_number (int): The ID number of the student to find.
        
        Returns:
            Optional[Tuple[int, Student]]: The index and student object if found, otherwise None.
        """
        for i, found_student in enumerate(self.students):
            if found_student.id_number == id_number:
                return i, found_student
        return None

    def update_student(self, student: Student) -> str:
        """ 
        It first iterates over the student list and saves the index where the student is located.
        Then replaces the student's details in the system using the index.
        
        Args:
            student (Student): The student with updated details.
        
        Returns:
            str: A message indicating that the student data has been updated.
        """
        i, _ = self.find_student(student.id_number)
        self.students[i] = student
        return f"Student data has been updated to {student}"
    
    def show_student(self) -> List[Student]:
        """
        Returns a list of all students in the system.
        
        Returns:
            List[Student]: A list of all student objects.
        """
        return self.students

    def add_instructor(self, instructor: Instructor) -> None:
        """
        Adds an instructor to the system.
        
        Args:
            instructor (Instructor): The instructor to be added to the system.
        """
        self.instructors.append(instructor)

    def remove_instructor(self, id_number: int) -> str:
        """
        Removes an instructor from the system by their ID number.
        
        Args:
            id_number (int): The ID number of the instructor to be removed.
        
        Returns:
            str: A message indicating whether the instructor was successfully removed or not found.
        """
        for instructor in self.instructors:
            if instructor.id_number == id_number:
                self.instructors.remove(instructor)
                return f"Instructor with ID {id_number} has been removed."
        return "No instructor found with the given ID"

    def find_instructor(self, id_number: int) -> Optional[Tuple[int, Instructor]]:
        """
        Finds an instructor by their ID number.
        
        Args:
            id_number (int): The ID number of the instructor to find.
        
        Returns:
            Optional[Tuple[int, Instructor]]: The index and instructor object if found, otherwise None.
        """
        for i, found_instructor in enumerate(self.instructors):
            if found_instructor.id_number == id_number:
                return i, found_instructor
        return None

    def update_instructor(self, instructor: Instructor) -> str:
        """
        Updates an instructor's details in the system.
        
        Args:
            instructor (Instructor): The instructor with updated details.
        
        Returns:
            str: A message indicating that the instructor data has been updated.
        """
        i, _ = self.find_instructor(instructor.id_number)
        self.instructors[i] = instructor
        return f"Instructor data has been updated to {instructor}"
    
    def show_instructors(self) -> List[Instructor]:
        """
        Returns a list of all instructors in the system.
        
        Returns:
            List[Instructor]: A list of all instructor objects.
        """
        return self.instructors

    def add_courses(self, course: Course) -> None:
        """
        Adds a course to the system.
        
        Args:
            course (Course): The course to be added to the system.
        """
        self.courses.append(course)
    
    def remove_course(self, course_id: int) -> str:
        """
        Removes a course from the system by its course ID.
        
        Args:
            course_id (int): The ID of the course to be removed.
        
        Returns:
            str: A message indicating whether the course was successfully removed or not found.
        """
        for course in self.courses:
            if course.course_id == course_id:
                self.courses.remove(course)
                return f"Course with ID {course_id} has been removed."
        return "No course found with the given ID"

    def find_course(self, course_id: int) -> Optional[Tuple[int, Course]]:
        """
        Loops through self.courses and returns the index where the course is found by comparing the id of the course 
        and the given course id.
        
        Args:
            course_id (int): The id of the course to find.
        
        Returns:
            Optional[Tuple[int, Course]]: The index and course object if found, otherwise None.
        """
        for i, found_course in enumerate(self.courses):
            if found_course.course_id == course_id:
                return i, found_course
        return None
    
    def update_course(self, course: Course) -> str:
        """
        Find the course using the previous find_course method, 
        and replace the course in the index location with another course.
        
        Args:
            course (Course): The course with updated details.
        
        Returns:
            str: A message indicating that the course data has been updated.
        """
        i, _ = self.find_course(course.course_id)
        self.courses[i] = course
        return f"Course data has been updated to {course}"
    
    def enroll_student_in_courses(self, student: Student, *courses: Course) -> str:
        """
        Enrolls a student in one or more courses.
        
        Args:
            student (Student): The student to enroll.
            *courses (Course): One or more courses to enroll the student in.
        
        Returns:
            str: A message indicating how many courses the student has been enrolled in.
        """
        for course in courses:
            enrollment = Enrollment(student, course)
            self.enrollments.append(enrollment)
            if student.id_number not in self.grades:
                self.grades[student.id_number] = {}
            self.grades[student.id_number][course.course_name] = None
        return f"{student.name} has been enrolled in {len(courses)} course(s)"

    def show_enrollment(self) -> None:
        """
        Prints all enrollments in the system.
        """
        for enrollment in self.enrollments:
            print(enrollment)

    def assign_grade(self, student: Student, course: Course, grade: int) -> str:
        """
        Assigns a grade to a student for a specific course.
        
        Args:
            student (Student): The student to whom the grade is assigned.
            course (Course): The course for which the grade is assigned.
            grade (int): The grade to assign.
        
        Returns:
            str: A message indicating that the grade has been assigned.
        """
        for enrollment in self.enrollments:
            if enrollment.student == student and enrollment.course == course:
                enrollment.assign_grade(grade)
                self.grades[student.id_number][course.course_name] = grade
        return f"Grade {grade} assigned to student {student.name} for course {course.course_name}"
        
    def students_grades(self) -> Dict[int, Dict[str, Optional[int]]]:
       

        """
        Returns a dictionary of all students and their grades.
        
        Returns:
            Dict[int, Dict[str, Optional[int]]]: A dictionary where the keys are student IDs and values are dictionaries of course names and grades.
        """
        return self.grades

    def get_student_grades(self, student_id: int) -> Optional[Dict[str, Optional[int]]]:
        """
        Returns the grades for a particular student by their ID.
        
        Args:
            student_id (int): The ID of the student whose grades are to be retrieved.
        
        Returns:
            Optional[Dict[str, Optional[int]]]: A dictionary of course names and grades for the specified student, or None if the student is not found.
        """
        return self.grades.get(student_id)
    
    def studentlist_in_course(self, course_id: int) -> Union[List[str], str]:
        """
        Retrieves a list of students enrolled in a specific course by its ID.
        
        Args:
            course_id (int): The ID of the course for which to retrieve the student list.
        
        Returns:
            Union[List[str], str]: A list of student names enrolled in the course, or a message indicating no students or course not found.
        """
        course_object = next((course for course in self.courses if course.course_id == course_id), None)
        if course_object:
            enrolled_students = course_object.list_enrolled_students()
            if enrolled_students:
                return enrolled_students
            else:
                return f"No students are enrolled in {course_object.course_name}."
        else:
            return "Course not found."

    def student_course_list(self, student_id: int) -> Union[List[str], str]:
        """
        Retrieves a list of courses a specific student is enrolled in by their ID.
        
        Args:
            student_id (int): The ID of the student for whom to retrieve the course list.
        
        Returns:
            Union[List[str], str]: A list of course names the student is enrolled in, or a message indicating no courses or student not found.
        """
        student_object = next((student for student in self.students if student.id_number == student_id), None)
        if student_object:
            enrolled_courses = [
                course.course_name for course in self.courses if student_object in course.enrolled_students
            ]
            if enrolled_courses:
                return enrolled_courses
            else:
                return f"Student {student_object.name} is not enrolled in any courses."
        else:
            return "Student not found."