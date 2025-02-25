- Tuples
	- ordered sequence of elements, which can mix elements types
	- can't change the values as a tuple is **immutable**
	- represented with parentheses: `t = (2, 'mit', 3)`
	- can index and slice a tuple: ex. t[0], t[0:2]
	- to represent a tuple of one element, need an extra comma: `t = ('mit',)`
- Uses of tuples
	- can be used to concisely **swap** variable values:
		- before: `temp = x; x = y; y = temp`
		- after: `(x, y) = (y, x)`
	- can be used to **return more than one value** from a function
	```
	def quotient_and_remainder(x, y):
		q = x // y # integer division
		r = x % y
		return (q, r)
	(quot, rem) = quotient_and_remainder(4,5) # returns (0, 4)
	```
- Lists
	- **ordered sequence** of information, accessible by index
	- lists are denoted by **square brackets**
	- a list contains **elements**, usually homogeneous but can contain mixed types
	- can be indexed and sliced like tuples and strings
	- lists are **mutable**, meaning that its elements can be changed, i.e. can perform assignment using indexing: `L = [2,1,3]; L[1] = 5`
- Operations on Lists
	- **add** elements to the end of the list
		- append an object using `List.append(element)` notation ("**mutation**")
		- combine lists together using **concatenation** operator ("+")
	- **remove** elements at certain places in the list
		- delete at **specific index** with `del()`
		- remove at **end of list** with `.pop()`
		- remove the very first occurrence of a **specific element** with `.remove()`
	- convert lists to strings and back
		- convert strings to lists with `list(s)`
		- use `s.split()` to split a string on a character parameter (default is spaces)
		- use `''..join(L)` to turn a list of characters into a string and can give a character in quotes to add char between every element
		- `s = "I<3 cs"` -> `s` is a string
		- `list(s)` -> returns `['I','<','3',' ','c','s']`
		- `s.split('<')` -> returns `['I', '3 cs']`
		- `L = ['a','b','c']` -> `L` is a list
		- `''.join(L)` -> returns `"abc"`
		- `'_'.join(L)` -> returns `"a_b_c"`
	- Other
		- `sort()` sorts by mutating original list
		- `sorted()` returns sorted list but does not mutate original list
		- `reverse()` reverses by mutating original list
- Aliases
	- different names for the same object in memory - ex. `warm = ['red', 'yellow', 'orange']; hot = warm`
- Cloning a list
	- creates a new list and copies every element - ex. `chill = cool[:]`
- Nesting
	- lists can be **nested**, i.e. you can have lists of lists indefinitely
- Mutation and iteration
	- avoid mutating a list as you are iterating over it or you can end up skipping an index you want to perform an operation on
	- ex:
	```
	def remove_dups(L1, L2):
		for e in L1:
			if e in L2:
				L1.remove(e)

	L1 = [1, 2, 3, 4]
	L2 = [1, 2, 5, 6]
	remove_dups(L1, L2)
	```
	- The code block above modifies `L1` to `[2,3,4]`
