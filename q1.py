class SchoolManagementTool:
    """A tool that handles course and student administrative tasks."""

    def __init__(self):
        self.tables = {
            "Courses": "courses",
            "Class": "class",
            "Students": "students"
        }
        # self.engine.connect()

    def add_student_to_class_by_student_id(self, student_id, class_id):
        """
        Add a student to a class by id.

        :param student_id: an int, the student id
        :param class_id:  an int, the class id
        """
        assert len(class_id) == 6

        # Check that student exists
        self.tables.Students.findById(student_id)
        target_class = self.tables.Class.findById(class_id)

        # This may be more appropriate to do in the database
        assert self.tables.Courses.findByKey(target_class.getCourseCode, target_class.getSection).seatsRemaining > 0
        target_class.Enrolled_student_ids.append(student_id)

        # increase_tuition(student)

    # def add_course(self, course_code, section, faculty, instructor, total_seats, class_name):
    #     assert len(course_code) == 3
    #     assert len(section) == 3
    #     course = Course(course_code, section, faculty, instructor, total_seats)
    #     class = Class(int(str(course_code) + str(section)), class_name, instructor)
    #     self.tables.Class.add(class)
    #     self.tables.Courses.add(course)

    # def update_course_instructor(self, instructor, course_code, section):
    #     assert len(course_code) == 3
    #     assert len(section) == 3
    #     target_class = self.tables.Class.findById(int(str(course_code) + str(section)))
    #     course = self.tables.Courses.findByKey(course_code, section)
    #     target_class.update({"instructor": instructor})
    #     course.update({"instructor": instructor})
