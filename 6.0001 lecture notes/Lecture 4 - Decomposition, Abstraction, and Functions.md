- **functions** are mechanisms to achieve **decomposition** and **abstraction**
	- **abstraction** - don't need to know how something works in order to use it
	- **decomposition** - different pieces of code can work together to achieve an end goal
- Create structure with decomposition 
	- in programming means you divide code into **modules**, which are:
		- **self-contained**
		- used to **break up** code
		- intended to be **reusable**
		- keep code **organized** and **coherent**
	- Decomposition can be achieved with **functions** and **classes**
- Suppress details with Abstraction
	- can achieve abstraction using **function specifications** or **docstrings**
- Functions
	- reusable pieces of code that are not run in a program until called or invoked
	- characteristics:
		- name
		- parameters (0 or more)
		- docstring (optional but recommended)
			- tells others how the code works (multiline comments)
		- body
		- returns something
- Variable Scope
	- **formal parameter** gets bound to the value of **actual parameter** when function is called
		- formal parameter 'x': `def f(x): ...`
		- actual parameter 'x': `x = 3; z = f(x)`
	- if there is no `return` statement in a function, python returns `None` which represents the absence of a value
- Functions as arguments
	- Because everything in python is an object, functions are considered objects, and therefore can be passed as arguments to other functions
	```
	def func_a(): 
		print 'inside func_a' 
	def func_c(z): 
		print 'inside func_c' 
		return z() # expects 'z' to be a function and attempts to call 'z'
	print func_c(func_a)
	```
- Scope
	- you can access a variable defined outside a function while inside the function
	- however, while inside a function you cannot modify a variable defined outside the function (except if defined as a global variable) - allowed but frowned upon