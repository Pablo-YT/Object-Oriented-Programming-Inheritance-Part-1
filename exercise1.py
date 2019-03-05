class Person():
	"""docstring for Person"""
	
	def greeting(self):
		return "Hi, my name is {}".format(self.Student_name)
		
	def greeting2(self):
		return "Hi, my name is {}".format(self.Instructor_name)	


class Instructor(Person):
		"""docstring for Instructor"""	
		def teach(self):
			return "The object is an instance of a class"

		def Nadia(self):
			return self.greeting2()

		def __init__(self,Instructor_name):
			self.Instructor_name = Instructor_name

class Student(Person):
	"""docstring for Student"""
	def learn(self):
		return "I Get It"

	def Chris(self):
		return self.greeting()

	def __init__(self, Student_name):
		self.Student_name = Student_name


Student1 = Student('Chris')
Instructor1 = Instructor('Nadia')

print(Student1.Chris())
print(Instructor1.Nadia())

print(Instructor1.teach())
print(Student1.learn())


