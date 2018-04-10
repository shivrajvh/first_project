'''
class myclass():
	def m1(self):
		print("Welcome")

	def m2 (self, test):
		print("This is Life " + test)


def main():
	c=myclass()
	c.m1()
	c.m2("Have a good one")

if __name__ == '__main__':
    main()
'''

'''
class myclass():
	def m1(self):
		print("Master Class")

	def m2(self, test):
		print("Still in master class.." + test)

class childclass(myclass):
	def m3(self):
		print("Child Class")

	def m4(self, test1):
		print ("Still in child class.." + test1)

def main():
	c = childclass()
	c.m3()
	c.m4("Calling child class")
	c.m1()
	c.m2("Blah BLAH")

if __name__ == '__main__':
	main()

'''




