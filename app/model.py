from sqlalchemy import (Column,String,DateTime,Integer,create_engine,ForeignKey)

                                         
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = create_engine("postgresql://postgres:example@localhost:5455/homeserver")
Base = declarative_base()

class User(Base):
    __tablename__= "users"
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False)
    password = Column(String,nullable=False)
    apiKey = Column(String,nullable=True)
    apiExpiry = Column(DateTime,default=datetime.utcnow)
    dateCreated = Column(DateTime,default=datetime.utcnow)
    
    projects = relationship("Projects")
    task = relationship("Tasks")

    def __repr__(self):
        return f'<{self.name} - {self.email} >'

class Statuses(Base):
    __tablename__="status"
    id = Column(Integer,primary_key=True)
    name = Column(String(50),nullable=False)
    description = Column(String(250),nullable=False)
    projects = relationship('Projects')
    tasks = relationship('Tasks')

    def __repr__(self):
        return f'<{self.id} - {self.name} >'

class Projects(Base):
    __tablename__="projects"
    id = Column(Integer,primary_key=True)
    project_name = Column(String(50),nullable=False)
    project_description = Column(String(300),nullable=True)
    status = Column(Integer,ForeignKey('status.id'))
    created_by = Column(Integer, ForeignKey('users.id'))
    created_on = Column(DateTime, default=datetime.utcnow)
    due_date = Column(DateTime)
    estimated_hours_required = Column(Integer,nullable=True)
    tasks = relationship('Tasks')

    def __repr__(self):
        return f'{self.id} - {self.project_name} due on: {self.due_date}'

class Tasks(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer,ForeignKey('projects.id'))
    assigned_to = Column(Integer,ForeignKey('users.id'))
    created_on = Column(DateTime,default=datetime.utcnow)
    title = Column(String(50),nullable=False)
    description = Column(String,nullable=False)
    estimated_hours_required = Column(Integer,nullable=False)
    status = Column(Integer,ForeignKey('status.id'))

    def __repr__(self):
        return f'{self.id} - {self.title} {self.description}'
    

