## Recursion
- Recursion
	- Wikipedia: the process of repeating items in a self-similar way
	- Algorithmically: a way to design solutions to problems by **divide and conquer**/**decrease and conquer**
	- Semantically: a programming technique where a **function calls itself**
		- goal is to NOT have infinite recursion
		- need **1 or more base cases** that are easy to solve
		- must solve the same problem on some other input the goal of simplifying the larger problem input
- Iterative algorithms so far
	- while and for loops
	- can capture computation in a set of state variables that update on each iteration through the loop
- Multiplication - recursive solution
	- `a*b` really just means "sum '`b`' number of '`a`'"
	- **recursive step** - think how to reduce problem to a simpler/smaller version of the same problem
		- b times: `a*b = a + a + ... + a`
		- b-1 times: `a*b = a + (a + ... + a)` 
		- recursive reduction: `a*b = a + a*(b-1)`
	- **base case** - keep reducing problem until you reach a simple case that can be solved directly; in this case, when `b = 1`,  then `a*b = a`
	```
	def mult(a, b):
		if b == 1:
			return a
		else:
			return a + mult(a, b-1)
	```
- Inductive reasoning
	- How do we know our recursive code above will work?
	- Answer: (Assuming b is always a positive integer) base case is 1 and we decrease b by 1 every time we go through the loop, therefore b will at some point become 1
- Mathematical induction
	- To prove a statement that is indexed on integers is true for all values of n, we must do the following:
		1. Base case: Prove the statement is true when 'n' is the smallest value (e.g. n = 0, or n = 1)
		2. Inductive step: Prove that if the statement is true for an arbitrary value of 'n', then the statement must also be true for n+1
	- We must apply the same logic to our recursive code above:
		- Base case: When b == 1, return 'a' because a\*1 = a
		- Recursive case: Assuming that `mult` will correctly return an answer for problems of size smaller than 'b' (i.e. `b-1`), then by the time we add to 'a' it must also return a correct answer for a problem of size 'b'
## Dictionaries
- Dictionaries can be implemented alternatively using multiple lists using related info indexed at the same place in every list
	- maintain separate lists for each item
	- each list must be same length
	- info must be stored across lists at same index
- Not ideal!
	- messy if there's lots of info to keep track of
	- must maintain many lists and pass as args
	- must always index using integers
	- must remember to change multiple lists
- Dictionaries! better and cleaner than multiple lists
	- can index an item of interest directly and it doesn't have to be an int
	- can utilize a single data structure, not separate lists
- Dictionary features
	- stores data as key/value pairs
	- look up values in the dict using the key, which returns the value associated with the key; throws error if no key found
- Dictionary operations
	- add an entry: `grades['Sylvan'] = 'A'`
	- test if key in dictionary: `'John' in grades` returns `True`
	- delete an entry: `del(grades['Ana'])`
	- call the dict for an iterable of all keys
	- call the dict for an iterable of all values
- Keys and Values
	- Values
		- can be any type (mutable/immutable)
		- can be duplicates
		- can be lists or other dictionaries!
	- Keys
		- must be unique
		- must be of an immutable type (int, float, string, tuple, bool)
			- technically, must be hashable
		- floats are funny - can use them but not recommended
	- there are no order to keys or values