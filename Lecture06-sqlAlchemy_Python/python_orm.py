"""
This script demonstrates how ORM works.
ORM = Object relational mapping.
SQLAlchemy is a popular Python library that people use to extract rows from
a database and turn the data into an object.
Then the object is useable in your program.

To run this you need to:
1. Install Python3 on your computer
2. Open a command prompt and type "pip install sqlalchemy" to install the sqlalchemy library
3. Run the script by typing "python python_orm.py"
4. Then have a look in the folder you ran the script in and you should see a database!
   You can use the sqlite3 command line to investigate the db and verify that your python code worked.
"""

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey# For all supported datatypes, see https://docs.sqlalchemy.org/en/14/core/types.html
from sqlalchemy.orm import sessionmaker, declarative_base

BaseClass = declarative_base()

class Student(BaseClass):
	__tablename__ = "students"
	id_number = Column("id_number", String, primary_key=True)
	gpa = Column("gpa", Float)
	first = Column("first", String)
	last = Column("last", String)

	def __init__(self, id_number, gpa, first, last):
		self.id_number = id_number
		self.gpa =  gpa
		self.first = first
		self.last = last

	def __repr__(self):
		return "{} {} has id_number {} and gpa {}".format(self.first, self.last, self.id_number, self.gpa)



class GothicCard(BaseClass):
	__tablename__ = "GothicCard"
	# Note: if you uncomment this rownumber line and comment out the other
	# then you run the script, NO tables are created. Why?
	# Remember that sqlite is ACID compliant / transactional DB
	# So if there is any error before you Commit(), then nothing happens 
	# at all.
	# Look in the main part of the code and you will see that there is a commit() method.
	#rownumber = Column("rownumber", Integer)
	rownumber = Column("rownumber", Integer, primary_key=True)
	funds = Column("funds", Float)
	number = Column(String, ForeignKey("students.id_number"))

	def __init__(self, rownumber,funds, number):
		self.rownumber = rownumber
		self.funds = funds
		self.number = number

	def __repr__(self):
		return "{} has ${}".format(self.number, self.funds)


if __name__ == '__main__':
	dbEngine = create_engine("sqlite:///pythonExample.db")

	BaseClass.metadata.create_all(bind=dbEngine)

	Session = sessionmaker(bind=dbEngine)
	session = Session()

	student = Student("01110123", 3.97, "Julian", "Cienfuegos")
	session.add(student)

	student2 = Student("09990123", 2.0, "Napoleon", "Dynamite")
	session.add(student2)

	student3 = Student("65464512", 3.4, "Bella", "Hermosin")
	session.add(student3)

	card = GothicCard(1, 40.00, "01110123")
	session.add(card)

	card2 = GothicCard(2, 140.00, "65464512")
	session.add(card2)
	
	card3 = GothicCard(3, 4.00, "09990123")
	session.add(card3)

	session.commit()


	print("Students with gpa > 3.0: ")
	overachievers = session.query(Student).filter(Student.gpa > 3.0)
	for pupil in overachievers:
		print(pupil)

	print("Students joined with their funds:")
	moneymoney = session.query(Student, GothicCard).filter(Student.id_number == GothicCard.number).all()
	for money in moneymoney:
		print(money)