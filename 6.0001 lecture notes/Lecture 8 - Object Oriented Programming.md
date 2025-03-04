- Objects
	- basically different kinds of data
	- every object has:
		1. a **type**
		2. an internal **data representation** (primitive or composite)
		3. a set of procedures for **interaction** with the object
	- an object is an instance of a type
- Object oriented programming
	- everything in python is an object and has a type
	- you can create new objects of a type
	- you can manipulate and destroy objects
	- What are objects? a data abstraction that captures:
		1. an **internal representation** through data attributes
		2. an **interface** for interacting with the object through methods/procedures/functions - behavior is defined but implementation is hidden
- Advantages of OOP
	- can bundle data into packages with procedures that operate on them in well defined interfaces
	- divide-and-conquer development
		- allows you to implement and test behavior of each class separately
		- reduce complexity through increased modularity
	- easy to reuse code
		- classes have their own environment, so no namespace collisions
		- inheritance allows subclassing to redefine or extend a subset of the superclass' behavior
- Classes vs. instances
	- creating a class involves defining the class name and attributes
	- using the class involves creating new instances of objects and doing operations on the instance
- What are attributes?
	- data attributes - other objects that make up the class
	- methods (procedural attributes) - functions that only work with this class; allows you to interact with the object
- How to create an instance of a class?
	- first have to define **how to create an instance** of the object
	- done using a **special method called `__init__`** to initialize some data attributes
	```Coordinate
	class Coordinate(object):
		def __init__(self, x, y):
			self.x = x
			self.y = y

	c = Coordinate(3,4)
	origin = Coordinate(0,0)
	print(c.x)
	print(origin.x)
	```
	- the 'self.' notation refers to an instance of the class - python will implicitly pass in this argument
	- data attributes of an instance are called **instance variables**
- Methods
	```
	def distance(self, other):
		x_diff_sq = (self.x-other.x)**2
		y_diff_sq = (self.y-other.y)**2
		return (x_diff_sq + y_diff_sq)**0.5
	```
	- `c.distance(zero)` is equivalent to `Coordinate.distance(c,zero)`
- Print representation of an object
	- print by default returns largely unhelpful memory location information
	- Python calls the `__str__` method for the class to determine how to represent the object when used with the `print` statement