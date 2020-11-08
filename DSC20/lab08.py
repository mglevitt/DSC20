# Question 1.


class Student:
    """
    Manages student information for any student.
    >>> st1 = Student("Black", "John", 12345, "blackj@ucsd.edu")
    >>> print(st1)
    Black, John -- ID: 12345
    Email Address: blackj@ucsd.edu
    >>> st2 = Student("White", "Ann", 35435, "whitea@rt.edu")
    >>> print(st2)
    White, Ann -- ID: 35435
    Email Address: whitea@rt.edu
    """
    def __init__(self,lname,fname,id,email):
        self.lname=lname
        self.fname=fname
        self.id=id
        self.email=email
    def __str__(self):
        lname=self.lname
        fname=self.fname
        id=self.id
        email=self.email
        return lname+', '+fname+' -- ID: '+str(id)+'\n'+'Email Address: '+email
        


class DSC_Student(Student):
    """
    DSC_Student inherits from Student. Manages student information
    DSC students specifically. Has the taken_classes method.
    >>> dsc_s1 = DSC_Student("Nabi", "Cool", 98767, "cooln@ucsd.edu")
    >>> print(dsc_s1)
    Nabi, Cool -- ID: 98767
    Email Address: cooln@ucsd.edu
    >>> print(DSC_Student.major)
    DSC
    >>> dsc_s1.taken_classes(["dsc10", "dsc40a", "dsc20"])
    ['dsc10', 'dsc40a', 'dsc20']
    >>> dsc_s1.taken_classes(["dsc10", "dsc40a", "dsc20", "dsc30"])
    ['dsc10', 'dsc40a', 'dsc20', 'dsc30']
    """
    def __init__(self,lname,fname,id,email):
        self.lname=lname
        self.fname=fname
        self.id=id
        self.email=email
    def __str__(self):
        lname=self.lname
        fname=self.fname
        ID=str(self.id)
        email=self.email
        return lname+', '+fname+' -- ID: '+ID+'\n'+'Email Address: '+email
    major='DSC'
    def taken_classes(self,classes):
        self.class_list=classes
        return self.class_list


# Question 2.

class DSC_Student_Proud(DSC_Student):
    """
    DSC_Student_Proud inherits from DSC_Student. Manages student information
    for proud DSC students.
    >>> dsc_s2 = DSC_Student_Proud("Nabi", "Cool", 98767, "cooln@ucsd.edu")
    >>> print(dsc_s2)
    Nabi, Cool -- ID: Secret
    Major: DSC
    Email Address: cooln@ucsd.edu
    >>> dsc_s2
    DSC_Student_Proud(Nabi, Cool, DSC, cooln@ucsd.edu), type:class
    """
    def __init__(self,lname,fname,id,email):
        self.lname=lname
        self.fname=fname
        self.id=id
        self.email=email
    def __str__(self):
        ln=self.lname
        fn=self.fname
        ID='Secret'
        eml=self.email
        mjr=DSC_Student.major
        return ln+', '+fn+' -- ID: '+ID+'\nMajor: '+mjr+'\nEmail Address: '+eml
    def __repr__(self):
        ln=self.lname
        fn=self.fname
        mjr=DSC_Student.major
        eml=self.email
        return 'DSC_Student_Proud('+ln+', '+fn+', '+mjr+', '+eml+'), type:class'
    


# Question 3.

class DSC_Student_Drop(DSC_Student):
    """
    Inherits from DSC_Student. This class is intended for DSC Students
    that are dropping a course.
    >>> dsc_s1 = DSC_Student_Drop("Nabi", "Cool", 98767, "cooln@ucsd.edu")
    >>> print(dsc_s1)
    Nabi, Cool -- ID: 98767
    Email Address: cooln@ucsd.edu
    >>> print(DSC_Student.major)
    DSC
    >>> dsc_s1.drop("dsc40b")
    'You do not have list of classes'
    >>> dsc_s1.taken_classes(["dsc10", "dsc40a", "dsc20"])
    ['dsc10', 'dsc40a', 'dsc20']
    >>> dsc_s1.taken_classes(["dsc10", "dsc40a", "dsc20", "dsc30"])
    ['dsc10', 'dsc40a', 'dsc20', 'dsc30']
    >>> dsc_s1.drop("dsc30")
    >>> print(dsc_s1.class_list)
    ['dsc10', 'dsc40a', 'dsc20']
    >>> dsc_s1.drop("dsc40b")
    'Class is not in your list'
    """
    class_list=[]
    def __init__(self,lname,fname,id,email):
        self.lname=lname
        self.fname=fname
        self.id=id
        self.email=email
    def __str__(self):
        lname=self.lname
        fname=self.fname
        ID=str(self.id)
        email=self.email
        return lname+', '+fname+' -- ID: '+ID+'\n'+'Email Address: '+email
    def taken_classes(self,classes):
        self.class_list=classes
        return self.class_list
    def drop(self,clas):
        length=len(self.class_list)
        if length > 0:
            for i in range(length):
                if self.class_list[i] == clas:
                    self.class_list=self.class_list[:i]+self.class_list[i+1:]
            if length == len(self.class_list):
                return 'Class is not in your list'
        else:
            return 'You do not have list of classes'
        

# Question 4.

class Address:
    """
    Keeps street name and number in each instance.
    >>> Arda_addr = Address("1 Miramar Street", 3303)
    >>> Arda_addr.street_name
    '1 Miramar Street'
    >>> Arda_addr.number
    3303
    >>> Arda_addr.number = 2222
    >>> print(Arda_addr.get_full_addr())
    Street Name: 1 Miramar Street
    Number: 2222
    """

    def __init__(self,street,num):
        self.street_name=street
        self.number=num
    def get_full_addr(self):
        return 'Street Name: '+self.street_name+'\nNumber: '+str(self.number)


class WorkAddress(Address):
    """
    Inherits from Address. Used specifically for Work Adresses.
    >>> Marina_addr = WorkAddress("205E")
    >>> Marina_addr.office_number
    '205E'
    >>> Marina_addr.street_name
    'Hopkins Dr'
    >>> Marina_addr.number
    10100
    >>> print(Marina_addr.get_full_addr())
    Street Name: Hopkins Dr
    Number: 10100
    Office No: 205E
    """

    def __init__(self,num):
        self.office_number=num
        self.street_name='Hopkins Dr'
        self.number=10100
    def get_full_addr(self):
        strt=self.street_name
        number=str(self.number)
        onumber=self.office_number
        return 'Street Name: '+strt+'\nNumber: '+number+'\nOffice No: '+onumber


class HomeAddress(Address):
    """
    Inherits from Address. Used specifically for Home Adresses.
    >>> Arda_addr = HomeAddress("1 Miramar St.", 3303, "La Jolla")
    >>> print(super(HomeAddress, Arda_addr).get_full_addr())
    Street Name: 1 Miramar St.
    Number: 3303
    >>> print(Arda_addr.get_full_addr())
    Street Name: 1 Miramar St.
    Number: 3303
    City: La Jolla
    """
    def __init__(self,street,num,city):
        self.street_name=street
        self.number=num
        self.city=city
    def get_full_addr(self):
        strt=self.street_name
        num=str(self.number)
        cty=self.city
        return 'Street Name: '+strt+'\nNumber: '+num+'\nCity: '+cty
    
