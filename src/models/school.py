from models import Student
from models import Teacher
from file_operation import write_json
from converting_type import studentObject_to_Dict, teacherObject_to_Dict

class School:
    def __init__(self, students, teachers):
        self.students = students
        self.teachers = teachers

    def display_all_students(self):
        if self.students != []: 
            # sort alphabetically
            sorted_students = sorted(self.students, key=lambda student: (student.name, student.last_name))
            for i in sorted_students:
                print(Student.print_info(i))
        else:
            print("\nThere is no students records")

    def display_all_teachers(self):
        if self.teachers != []: 
            # sort alphabetically
            sorted_teachers = sorted(self.teachers, key=lambda teacher: (teacher.name, teacher.last_name))
            for i in sorted_teachers:
                print(Teacher.print_info(i))
        else:
            print("\nThere is no teachers records")

    def find_student_by_id(self, student_id):
        found =False

        for i in self.students:
            if Student.get_id(i) == student_id:
                record = i
                found = True
                break
        try:
            print(Student.print_info(record))
        except UnboundLocalError:
            print("\nStudent record NOT in the system")
        return found
    
    def find_student_by_name(self, student_name):
        record = False

        for i in self.students:
            if i.name.lower() == student_name.lower():
                print(Student.print_info(i))
                record = True
        if record == False:
            print("\nStudent recond NOT in the system")
        return record

    def find_teacher_by_id(self, teacher_id):
        found = False

        for i in self.teachers:
            if Teacher.get_id(i) == teacher_id:
                record = i
                found = True
                break
        try:
            print(Teacher.print_info(record))
        except UnboundLocalError:
            print("\nTeacher record NOT in the system")
        return found
    
    def find_teacher_by_name(self, teacher_name):
        record = False

        for i in self.teachers:
            if i.name.lower() == teacher_name.lower():
                print(Teacher.print_info(i))
                record = True
        if record == False:
            print("\nTeacher recond NOT in the system")
        return record

    def student_update(self, id):
        for i in self.students:
            if Student.get_id(i) == id:
                Student.update_student(i)
        json_data = studentObject_to_Dict(self.students) + teacherObject_to_Dict(self.teachers)
        write_json(json_data, "\nStudent info updated succesfully!")

    def teacher_update(self, id):
        for i in self.teachers:
            if Teacher.get_id(i) == id:
                Teacher.update_teacher(i)  
        json_data = studentObject_to_Dict(self.students) + teacherObject_to_Dict(self.teachers) 
        write_json(json_data,"\nTeacher info updated succesfully!")

    def delete_teacher(self, id):
        for i in self.teachers:
            if Teacher.get_id(i) == id:
                self.teachers.remove(i)
        json_data = studentObject_to_Dict(self.students) + teacherObject_to_Dict(self.teachers)
        write_json(json_data, "\nTeacher record deleted succesfully!")

    def delete_student(self, id):
        for i in self.students:
            if Student.get_id(i) == id:
                self.students.remove(i)
        json_data = studentObject_to_Dict(self.students) + teacherObject_to_Dict(self.teachers)
        write_json(json_data, "\nStudent record deleted succesfully!")

    def filter_students_by_course(self, course):
        record = False
        list = []
        for i in self.students:
            if i.course.lower() == course.lower():
                list.append(i)
                print(Student.print_info(i))
                record = True
        if not record:
            print(f"\nThe course {course} has NOT been found in the system")
        return list
    
    def filter_teachers_by_subject(self, subject):
        record = False
        list = []
        for i in self.teachers:
            if i.subject_area.lower() == subject.lower():
                list.append(i)
                print(Teacher.print_info(i))
                record = True
        if not record:
            print(f"\nThe subject {subject} has NOT been found in the system")
        return list
    
    def print_list_all_courses(self):
        # defining a set variable to store the list of courses with no duplicate
        list_courses = set()
        # defining a boolean variable that returns False if the list is empty
        course = True

        for i in self.students:
            if i.course == "":
                continue
            list_courses.add(i.course)
        if list_courses:
            print("\n***** List of all courses in the school *****\n")
            for i in list_courses:
                print(i)
        else:
            print("There is no courses to show in the system")
            course = False
        return course

    def print_list_all_subjects(self):
        # defining a set variable to store the list of all subjects with no duplicate
        list_subjects = set()
        # defining a boolean variable that returns False if the list is empty
        subject = True
        
        for i in self.teachers:
            if i.subject_area == "":
                continue
            list_subjects.add(i.subject_area)
        if list_subjects:
            print("\n***** List of all the subjects taught in the school *****\n")
            for i in list_subjects:
                print(i)
        else:
            print("There is no teaching subjects to show in the system")
            subject = False
        return subject