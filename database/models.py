# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  December 24, 2024 17:02:55
# Database: sqlite:////tmp/tmp.Ap7Lk8lY26-01JFWSX7XYMVKDY2JEXPY517YP/CharitableEducationApp/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Fundraising(SAFRSBaseX, Base):
    """
    description: Records fundraising activities from local businesses.
    """
    __tablename__ = 'fundraising'
    _s_collection_name = 'Fundraising'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    business_name = Column(String)
    amount_raised = Column(Integer)
    date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)



class GovernmentGrant(SAFRSBaseX, Base):
    """
    description: Stores information about government grants.
    """
    __tablename__ = 'government_grants'
    _s_collection_name = 'GovernmentGrant'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    grant_name = Column(String)
    amount_awarded = Column(Integer)
    grant_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)



class Grade(SAFRSBaseX, Base):
    """
    description: Represents grade levels for students.
    """
    __tablename__ = 'grades'
    _s_collection_name = 'Grade'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    level_name = Column(String)
    description = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    StudentList : Mapped[List["Student"]] = relationship(back_populates="grade")



class Teacher(SAFRSBaseX, Base):
    """
    description: Table to store teacher details.
    """
    __tablename__ = 'teachers'
    _s_collection_name = 'Teacher'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date_of_birth = Column(DateTime)
    qualification = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    TeacherSkillList : Mapped[List["TeacherSkill"]] = relationship(back_populates="teacher")
    TeacherTopicAssignmentList : Mapped[List["TeacherTopicAssignment"]] = relationship(back_populates="teacher")



class Zoo(SAFRSBaseX, Base):
    """
    description: Contains information about the local zoo.
    """
    __tablename__ = 'zoo'
    _s_collection_name = 'Zoo'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    animal_name = Column(String)
    species = Column(String)
    description = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)



class Student(SAFRSBaseX, Base):
    """
    description: Stores student details and information.
    """
    __tablename__ = 'students'
    _s_collection_name = 'Student'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date_of_birth = Column(DateTime)
    grade_id = Column(ForeignKey('grades.id'))

    # parent relationships (access parent)
    grade : Mapped["Grade"] = relationship(back_populates=("StudentList"))

    # child relationships (access children)
    StudentGradeList : Mapped[List["StudentGrade"]] = relationship(back_populates="student")



class TeacherSkill(SAFRSBaseX, Base):
    """
    description: Records skills of teachers.
    """
    __tablename__ = 'teacher_skills'
    _s_collection_name = 'TeacherSkill'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    teacher_id = Column(ForeignKey('teachers.id'))
    skill_name = Column(String)

    # parent relationships (access parent)
    teacher : Mapped["Teacher"] = relationship(back_populates=("TeacherSkillList"))

    # child relationships (access children)



class TeacherTopicAssignment(SAFRSBaseX, Base):
    """
    description: Assigns topics to teachers.
    """
    __tablename__ = 'teacher_topic_assignments'
    _s_collection_name = 'TeacherTopicAssignment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    teacher_id = Column(ForeignKey('teachers.id'))
    topic_name = Column(String)

    # parent relationships (access parent)
    teacher : Mapped["Teacher"] = relationship(back_populates=("TeacherTopicAssignmentList"))

    # child relationships (access children)



class StudentGrade(SAFRSBaseX, Base):
    """
    description: Records student grades.
    """
    __tablename__ = 'student_grades'
    _s_collection_name = 'StudentGrade'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    student_id = Column(ForeignKey('students.id'))
    subject = Column(String)
    grade = Column(String)

    # parent relationships (access parent)
    student : Mapped["Student"] = relationship(back_populates=("StudentGradeList"))

    # child relationships (access children)
