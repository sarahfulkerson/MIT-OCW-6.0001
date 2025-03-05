- Getter and Setter methods
	- used outside of the class to access data attributes
	- can also use **dot notation** to access attributes (both data and methods), but not recommended
	- if accessing data attribute directly, you are not protected from name changes to the class attributes - better to access via getters/setters ("**information hiding**")
- Python is not great at information hiding!
	- allows you to access data from outside class definition
	- allows you to write to data from outside class definition
	- allows you to create data attributes for an instance from outside class definition
- Default arguments
	- **default arguments** are used for formal parameters if no arguments were given when creating the string
	- if no default argument set and the method is called without providing an argument, you get an error
- Hierarchies
	- **parent classes/superclasses** and **child classes/subclasses**
	- child class behavior
		- inherits all data and behaviors of parent class
		- add more info
		- add more behavior or override inherited behavior
	- any data or methods missing from child class will be inherited from above in the hierarchy (if it exists)
- Class variables
	- **class variables** - present in each instance of a class but the value is shared by all instances of the class
	- defined outside of the `__init__` method
	- can use a class variable to set the value for an instance variable:
	```Rabbit
	class Rabbit(Animal):
		tag = 1
		def __init__(self, age, parent1=None, parent2=None):
			Animal.__init__(self, age)
			self.parent1 = parent1
			self.parent2 = parent2
			self.rid = Rabbit.tag
			Rabbit.tag += 1
	```
	