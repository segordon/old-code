"""
File Name: class_design_school_schedule.py

Developer: Samuel Gordon

Date last modified: November 29th,, 2012

Description:
Design a schedule class for classes that a student (your!)
take during a semester.

Kind of ambiguous instructions. I went with the idea of making a class
 that would make it easy to create a database of students enrolled
 in the school.

email address: sam.gordon.vvc@gmail.com
"""

# what do we need to store, what's important?
class StudentSchedule(object):
    def __init__(self,first='', last='', id=0, classes='', semester=''):
        self.first_name_str = first
        self.last_name_str = last
        self.id_int = id
        self.classes_str = classes
        self.semester_str = semester

# sets up a formatted output
    def __str__(self):
        return "{} {}, ID:{} , Classes:{} , Semester:{}\n".format\
               (self.first_name_str, self.last_name_str, self.id_int, self.classes_str ,self.semester_str)

#shows an example of the class in action

stu0 = StudentSchedule('Sam', 'Gordon', 10, 'ENG101,CIS83,MATH90', 'Fall')
stu1 = StudentSchedule('Mary', 'Jane', 2, 'ENG90,CIS9,MATH50', 'Summer')
stu2 = StudentSchedule('Bob', 'Dylan', 5, 'ENG50,BIO50,CHEM50', 'Spring')
stu3 = StudentSchedule('John', 'Doe', 7, 'ENG101,HIST90,HLTH50,CHEM90', 'Fall)')
print(stu0,stu1,stu2,stu3)