"""
DSC 20 HW 07 OOP
NAME: Maxwell Levitt
PID : A15788481
"""

## Question 2 ##

NO_PENDING_MSG = "No pending assignments to grade!"
INVALID_ASSGN_MSG = "Submission has invalid assignment name!"

def doctests_go_here():
    """
    Since this question involves class interaction, we decided to put all
    doctests together for your benefit.

    The idea of these doctest is to simulate the operation of the whole
    system of classes. If your are successful in this regard you will get
    full points from style. You should add (at least) three doctests for
    each function you defined.

    >>> s1 = Student("fan", "yUXUAN", 2)
    >>> s2 = Student("Bati", "aRdA", 5)
    >>> s3 = Student("Nakahara", "Etsu", 4)
    >>> s4 = Student("Ozberkman", "Nabi", 4)

    >>> print(s2)
    ID: 2; Bati, Arda; Graduate student
    >>> s2.get_name()
    'Bati, Arda'
    >>> s1.get_id()
    1
    >>> s3.get_level()
    'Senior'

    >>> b1 = Submission(s3, "hw1", "Line1\\nLine2")
    >>> b2 = Submission(s3, "hw2", "Line1\\nLine2\\nLine3")
    >>> b3 = Submission(s4, "hw2", "AAAAAAAAAAAAAAAAAAA")
    >>> print(b2)
    Submission #2
    Name: Nakahara, Etsu
    Assignment: HW2
    Score: Pending
    Content:
    Line1
    Line2
    Line3

    >>> c1 = Course("dsc 20")
    >>> c2 = Course("DsC 30")
    >>> _, __ = c1.enroll_student(s1), c2.enroll_student(s4)
    >>> _, __ = c1.enroll_student(s2), c2.enroll_student(s2)
    >>> _, __ = c1.enroll_student(s3), c2.enroll_student(s3)
    >>> print(c2)
    Course name: DSC 30
    Students Enrolled: (3 students in total)
    ID: 4; Ozberkman, Nabi; Senior student
    ID: 2; Bati, Arda; Graduate student
    ID: 3; Nakahara, Etsu; Senior student

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> s1 = Student("han", "ChaN", 5)
    >>> s2 = Student("Boi", "gIRl", 1)
    >>> s3 = Student("MaN", "woMan", 3)
    >>> s4 = Student("leVitT", "MaX", 2)
    
    >>> print(s1)
    ID: 5; Han, Chan; Graduate student
    
    >>> b1 = Submission(s3, "hw1", "Line1\\nLine2")
    >>> b2 = Submission(s3, "hw2", "Line1\\nLine2\\nLine3")
    >>> b3 = Submission(s4, "hw2", "AAAAAAAAAAAAAAAAAAA")
    >>> b4 = Submission(s2, "hw1", "Line1\\nLine2")
    >>> b5 = Submission(s1, "hw2", "Line1\\nLine2\\nLine3")
    >>> b6 = Submission(s2, "hw2", "AAAAAAAAAAAAAAAAAAA")
    
    >>> print(b1)
    Submission #4
    Name: Man, Woman
    Assignment: HW1
    Score: Pending
    Content:
    Line1
    Line2
    
    >>> c1 = Course("dsc 20")
    >>> c2 = Course("DsC 30")
    
    >>> print(c1)
    Course name: DSC 20
    Students Enrolled: (0 students in total)
    
    >>> c1.enroll_student(s1)
    >>> c1.enroll_student(s2)
    >>> c1.enroll_student(s3)
    >>> c2.enroll_student(s2)
    >>> c2.enroll_student(s1)
    >>> c2.enroll_student(s4)
    
    >>> print(c1)
    Course name: DSC 20
    Students Enrolled: (3 students in total)
    ID: 5; Han, Chan; Graduate student
    ID: 6; Boi, Girl; Freshmen student
    ID: 7; Man, Woman; Junior student
    
    >>> c1.add_assignment('hw1', 18)
    >>> c1.add_assignment('hw2', 100)
    >>> c2.add_assignment('hw1', 1000)
    
    >>> c1.assignments
    {'HW1': 18, 'HW2': 100}
    
    >>> s1.submit_assignment(c1, 'hw2', 'work')
    >>> s2.submit_assignment(c1, 'hw1', 'work')
    >>> s3.submit_assignment(c2, 'hw2', 'work')
    >>> s4.submit_assignment(c1, 'hw1', 'work')
    >>> s2.submit_assignment(c2, 'hw2', 'work')
    >>> s1.submit_assignment(c2, 'hw1', 'work')
    >>> s4.submit_assignment(c1, 'hw2', 'work')
    >>> s3.submit_assignment(c1, 'hw2', 'work')
    
    
    >>> c1.peak_pending()
    Submission #19
    Name: Man, Woman
    Assignment: HW2
    Score: Pending
    Content:
    work
    >>> c2.peak_pending()
    Submission #17
    Name: Han, Chan
    Assignment: HW1
    Score: Pending
    Content:
    work
    
    >>> c1.grade_pending(9)
    True
    >>> c1.grade_pending(11)
    True
    >>> c2.grade_pending(7)
    True
    >>> c1.grade_pending(9)
    True
    
    
    >>> s1.grades
    {'DSC 30': [0.7], 'DSC 20': [9.0]}
    
    >>> s1.overall_grade(c1)
    9.0
    
    >>> c1.get_assignment_avg('HW1')
    61.11
    """
    return


class Student:
    """
    Implementation of student.
    """
    STR_LEVEL = ["", "Freshmen", "Sophomore", "Junior", "Senior", "Graduate"]
    id=0
    ## Question 2.1.2 (A) ##
    def __init__(self, lastname, firstname, level):
        """
        Constructor of Student.

        Requirement:
        Input validation

        Parameters:
        lastname (str): Last name of student. After initialization, the first
                        letter should be in uppercase while other letters are
                        all in lowercase. This string must have at least 2
                        characters.
        firstname (str): First name of student. After initialization, the first
                        letter should be in uppercase while other letters are
                        all in lowercase. This string must have at least 2
                        characters.
        level (int): Class level of student.
                     1 - Freshmen, 2 - Sophomore,
                     3 - Junior, 4 - Senior, 5 - Graduate

        Other attributes you need to initialze:
        (1) A student ID (int), ordered by the order of initialization
        (2) A list to record all courses (as Course instance) this
            student enrolled
        (3) A dictionary to record all graded submissions (as Submission
            instance) of this student, with course name (as string) as key
        """
        graduate=5
        assert isinstance(lastname,str) and isinstance(firstname,str)
        assert isinstance(level,int) and level>=1 and level<=graduate
        Student.id+=1
        self.ID =Student.id
        self.lastname=lastname[0].upper()+lastname[1:].lower()
        self.firstname=firstname[0].upper()+firstname[1:].lower()
        self.level=level
        self.courses=[]
        self.grades={}

    ## Question 2.1.2 (E) ##
    def __str__(self):
        """String representation (__str__). Do not modify."""
        return "ID: {}; {}; {} student".format( \
        self.get_id(), self.get_name(), self.get_level())

    ## Question 2.1.2 (B) ##
    def get_name(self):
        """Get student's name in Lastname, Firstname format."""
        return self.lastname+', '+self.firstname

    ## Question 2.1.2 (C) ##
    def get_id(self):
        """Get student's ID."""
        return self.ID

    ## Question 2.1.2 (D) ##
    def get_level(self):
        """Get student's level in string format."""
        return Student.STR_LEVEL[self.level]

    ## Question 2.5.1 (A) ##
    def submit_assignment(self, course, assignment, content):
        """
        Create a submission and submit it to the course only if the
        student enrolled in this course.

        Requirement:
        Input validation

        Parameters:
        course (Course): The course to submit.
        assignment (str): Assignment name of this submission.
        content (str): Content of this submission.

        Returns:
        None
        """
        assert isinstance(course,Course)
        assert isinstance(assignment,str) and isinstance(content,str)
        name=assignment.upper()
        if course.name in self.courses:
            Submission(self,name,content)
            course.submissions.append(Submission(self,name,content))

    ## Question 2.6.1 (A) ##
    def overall_grade(self, course):
        """
        Get this student's overall grade in given course as percentage,
        round to 2 decimal places.

        Parameters:
        course (Course): The course to check overall grade.

        Returns:
        (int or float) This student's overall grade in given course as
        percentage, rounded to 2 decimal places. For example: return 94.65
        if overall grade is 94.65%. Return -1 if course not found, or no
        graded submissions under this course.
        """
        assert isinstance(course,Course)
        rnd=2
        if course.name in self.grades:
            grade=sum(self.grades[course.name])/len(self.grades[course.name])
            return round(grade,rnd)
        else:
            return -1


class Submission:
    """
    Implementation of submission.
    """
    id=0
    ## Question 2.2.2 (A) ##
    def __init__(self, student, assignment, content):
        """
        Constructor of Submission.

        Requirement:
        Input validation

        Parameters:
        student (Student): Student that created this submission.
        assignment (str): Assignment name this submission belongs to. After
                          initialization, this string should be all capitalized.
        content (str): Content of this submission.

        Other attributes you need to initialze:
        (1) The score of this assignment (int or float), initialize it to
            -1, which stands for not graded (pending).
        (2) A submission ID (int), ordered by the order of initialization
        """
        assert isinstance(content,str) and isinstance(assignment,str)
        assert isinstance(student,Student)
        Submission.id+=1
        self.student=student
        self.assignment=assignment.upper()
        self.content=content
        self.score = -1
        self.ID = Submission.id

    ## Question 2.2.2 (B) ##
    def __str__(self):
        """String representation (__str__). Do not modify."""
        return "\n".join([
        "Submission #{}".format(self.ID),
        "Name: {}".format(self.student.get_name()),
        "Assignment: {}".format(self.assignment),
        "Score: {}".format((lambda g: "Pending" if g < 0 else g)(self.score)),
        "Content:",
        self.content])


class Course:
    """
    Implementation of course.
    """

    ## Question 2.3.2 (A) ##
    def __init__(self, name):
        """
        Constructor of Course.

        Requirement:
        Input validation

        Parameters:
        name (str): Name of the course. After initialization, this string
                    should be all capitalized. This string must have at least 2
                    characters.

        Other attributes you need to initialze:
        (1) A list to record all students (as Student instances) that enrolled
            in this class
        (2) A list to accept all submissions (as Submission instances) from
            students that are pending a grade
        (3) A dictionary to record all assignments created and their maximum
            score
        (4) A dictionary to record all graded submissions of all assignments
        """
        assert isinstance(name,str)
        self.name=name.upper()
        self.submissions=[]
        self.assignments={}
        self.grades={}
        self.students = []

    ## Question 2.3.2 (B) ##
    def __str__(self):
        """String representation (__str__). Do not modify."""
        join_list = [
        "Course name: {}".format(self.name),
        "Students Enrolled: ({} students in total)".format(len(self.students))
        ]
        join_list += list(map(str, self.students))
        return "\n".join(join_list)

    ## Question 2.3.2 (C) ##
    def add_assignment(self, assignment_name, full_score):
        """
        Add assignment to the course.

        Requirement:
        Input validation

        Parameters:
        assignment_name (str): Name of assignment
        full_score (int): Full score of assignment

        Returns:
        None
        """
        assert isinstance(assignment_name,str) and isinstance(full_score,int)
        self.assignments[assignment_name.upper()]=full_score

    ## Question 2.5.2 (A) ##
    def enroll_student(self, student):
        """
        Enroll student to this course.

        Requirement:
        Input validation

        Parameters:
        student (Student): Student to enroll

        Returns:
        None
        """
        assert isinstance(student,Student)
        self.students.append(student)
        student.courses.append(self.name)

    ## Question 2.5.2 (B) ##
    def peak_pending(self):
        """
        Print the content of the first pending submission. See write-up
        for details.

        Returns:
        None
        """
        if len(self.submissions)>0:
            sub=self.submissions.pop()
            print(sub)
            self.submissions.append(sub)
        else:
            print(NO_PENDING_MSG)

    ## Question 2.5.2 (C) ##
    def grade_pending(self, score):
        """
        Grade the first pending submission. See write-up for details.

        Requirement:
        Input validation

        Parameters:
        score (int or float): Score assigned to this assignment. Cannot
                              exceed the full score of this assignment.

        Returns:
        (boolean) True if graded submission is successfully send back to
        student, False otherwise.
        """
        cnvt=100
        rnd=2
        assert isinstance(score,int) or isinstance(score,float)
        if len(self.submissions)>0:
            sub=self.submissions.pop()
            name=sub.assignment
            if name in self.assignments:
                assert score <= self.assignments[name]
                grade=round((score/self.assignments[name])*cnvt,rnd)
                if sub in self.grades:
                    self.grades[name]+=[grade]
                else:
                    self.grades[name]=[grade]
                if self.name in sub.student.grades:
                    sub.student.grades[self.name]+=[grade]
                else:
                    sub.student.grades[self.name]=[grade]
                return True
            else:
                print(INVALID_ASSGN_MSG)
                return False
        else:
            print(NO_PENDING_MSG)
            return False
    ## Question 2.6.2 (A) ##
    def get_assignment_avg(self, assignment_name):
        """
        Get the average score of graded submissions of given assignment.
        Round to 2 decimal places.

        Requirement:
        Input validation

        Parameters:
        assignment_name (str): Name of assignment

        Returns:
        (int or float)The average score of graded submissions of given
        assignment, rounded to 2 decimal places. Return -1 if assignment not
        found, or no graded submissions under this assignment.
        """
        assert isinstance(assignment_name,str)
        rnd=2
        if assignment_name in self.grades:
            if len(self.grades[assignment_name])>0:
                grades=self.grades[assignment_name]
                return round(sum(grades)/len(grades),rnd)
            else:
                return -1
        else:
            return -1
