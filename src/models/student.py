from models import Person

class Student(Person):
    """
    The Student class is a sub class of Person class and includes additional attributes
    and methods specific to students
    """
    # class const
    profile = "Student"

    def __init__(self, name, last_name, address, course):
        """ The constructor initializes a new instance of Student 
        It calls the constructor of the Person class using super()
        to initialize the inherited attributes an then initializa the student parameters
        by the given parameters
    
        parameters: name(str), last_name(str), address(str), course(str)
        """
        try:
            super().__init__(name, last_name, address)
            self.course = course
            self.profile = Student.profile
            self.__id = Person.get_id()
        except AttributeError as error:
            print(f"Attribute assignment fails {error}")
        except Exception as error:
            print(f"An expected error occured: {error}")
        
    def get_id(self):
        """ This getter method returns the ID of the student instance"""
        return self.__id

    def print_info(self):
        """
        return: This method returns a string with the both inherited and student information like the course name. 
        """
        info = f"""
        Profile: {self.profile}
        Course name: {self.course}
        """
        return super().print_info() + info
    
    def update_student(self):
        """ This method updatates both inherited attributes and the course attribute by the prompt of the user """
        try:
            # call the update_info() method inherited from the superclass
            super().update_info()
            # call the Person.not_empty_value
            self.course = Person.not_empty_value("New course --> ").capitalize()
        except AttributeError:
            print("Attribute assignment fails")
        except Exception as error:
            print(f"Unexpected error occurred: {error}")
                