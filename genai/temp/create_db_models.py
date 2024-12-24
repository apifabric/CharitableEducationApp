# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py

from sqlalchemy.dialects.sqlite import *


class Teacher(Base):
    """
    description: Table to store teacher details.
    """
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date_of_birth = Column(DateTime)
    qualification = Column(String)


class Student(Base):
    """
    description: Stores student details and information.
    """
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date_of_birth = Column(DateTime)
    grade_id = Column(Integer, ForeignKey('grades.id'))


class Grade(Base):
    """
    description: Represents grade levels for students.
    """
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    level_name = Column(String)
    description = Column(String)


class TeacherSkill(Base):
    """
    description: Records skills of teachers.
    """
    __tablename__ = 'teacher_skills'

    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    skill_name = Column(String)


class TeacherTopicAssignment(Base):
    """
    description: Assigns topics to teachers.
    """
    __tablename__ = 'teacher_topic_assignments'

    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    topic_name = Column(String)


class StudentGrade(Base):
    """
    description: Records student grades.
    """
    __tablename__ = 'student_grades'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject = Column(String)
    grade = Column(String)


class Fundraising(Base):
    """
    description: Records fundraising activities from local businesses.
    """
    __tablename__ = 'fundraising'

    id = Column(Integer, primary_key=True)
    business_name = Column(String)
    amount_raised = Column(Integer)
    date = Column(DateTime)


class GovernmentGrant(Base):
    """
    description: Stores information about government grants.
    """
    __tablename__ = 'government_grants'

    id = Column(Integer, primary_key=True)
    grant_name = Column(String)
    amount_awarded = Column(Integer)
    grant_date = Column(DateTime)


class Zoo(Base):
    """
    description: Contains information about the local zoo.
    """
    __tablename__ = 'zoo'

    id = Column(Integer, primary_key=True)
    animal_name = Column(String)
    species = Column(String)
    description = Column(String)


# end of model classes


try:
    
    
    
    
    # ALS/GenAI: Create an SQLite database
    
    engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    
    Base.metadata.create_all(engine)
    
    
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    
    
    # ALS/GenAI: Prepare for sample data
    
    
    
    session.commit()
    teacher1 = Teacher(id=1, name="John Doe", date_of_birth=date(1975, 5, 20), qualification="Masters in Education")
    teacher2 = Teacher(id=2, name="Jane Smith", date_of_birth=date(1985, 8, 15), qualification="Bachelors in Science")
    teacher3 = Teacher(id=3, name="Alice Johnson", date_of_birth=date(1990, 2, 13), qualification="PhD in Mathematics")
    teacher4 = Teacher(id=4, name="Bob Brown", date_of_birth=date(1980, 10, 30), qualification="Masters in Physics")
    student1 = Student(id=1, name="Michael X.", date_of_birth=date(2010, 11, 22), grade_id=1)
    student2 = Student(id=2, name="Sara Y.", date_of_birth=date(2009, 6, 17), grade_id=2)
    student3 = Student(id=3, name="Luke Z.", date_of_birth=date(2011, 3, 5), grade_id=1)
    student4 = Student(id=4, name="Emily W.", date_of_birth=date(2010, 12, 11), grade_id=3)
    
    
    
    session.add_all([teacher1, teacher2, teacher3, teacher4, student1, student2, student3, student4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
