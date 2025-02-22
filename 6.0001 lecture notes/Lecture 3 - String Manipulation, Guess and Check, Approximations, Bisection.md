- Strings 
	- are a **sequence** of case sensitive characters
	- `len()` will retrieve the length of the string in the parentheses
	- square brackets '[]' are used to perform **indexing** into a string to get the value at a certain index/position
		- ex. if you have `s = "abc"` then `s[0]` evaluates to "a", `s[-1]` evaluates to "c", and `s[3]` will give an IndexError
	- you can **slice** a string using the format `[start:stop:step]`
		- if given 2 numbers, defaults to `[start:stop]` and `step=1`
		- `s = "abcdefgh"`
		  `s[3:6]` = "def", same as `s[3:6:1]`
		  `s[3:6:2]` = "df"
		  `s[::]` = "abcdefgh", same as `s[0:len(s):1]`
		  `s[::-1]` = "hgfedbca", same as `s[-1:-(len(s)+1):-1]`
		  `s[4:1:-2]` = "ec"
		- the `stop` value is the index to stop returning values; whatever is at that index and beyond will not be returned
	- strings are **immutable** and cannot be modified
		- ex: `s[0] = 'y'` is not allowed
- `for` loops recap
	- has a **loop variable** that iterates over a set of values
	- the range of values can be a set of numbers (ex. `range(5)`), but the loop variable can **iterate over any set of values**
- Guess-and-Check
	- also called **exhaustive enumeration**, when given a problem...
		- you are able to **guess a value** for a solution
		- you are able to **check if the solution is correct**
		- you keep guessing until you have found the solution or guessed all values
	- Cube root example:
		```
		cube = 8
	
		for guess in range(abs(cube)+1):
			if guess**3 >= abs(cube):
				break
		if guess**3 != abs(cube):
			print(cube, 'is not a perfect cube')
		else:
			if cube < 0:
				guess = -guess
			print('Cube root of '+str(cube)+' is '+str(guess))
		```
- Approximate Solutions
	- When you want a **good enough** solution
	- you start with a guess and increment by some **small value**
	- In our cube root example, you then keep guessing if `|guess^3 - cube| >= epsilon` for some **small epsilon value**
	- **epsilon** in this case = a small, positive value that defines the allowed error tolerance when finding an approximate solution to an optimization algorithm
- Bisection search
	- halve the interval each iteration
	- pick a new guess halfway in between
- Bisection search convergence
	- search space:
		- 1st guess: N/2
		- 2nd guess: N/4
		- 3rd guess: N/2^k
	- guess converges on the order of log2N steps
		- N/2^k = 1
		- 2^k  = N
		- k = logN