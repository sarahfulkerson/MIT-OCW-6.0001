## Constant Complexity
- complexity is independent of inputs - not many of these algorithms, but pieces often fit here

## Logarithmic Complexity
- complexity grows as log of size of one of its inputs
- Ex. bisection search a.k.a. binary search of a sorted list of length `n`
	- divide the list in half, check if the middle value (which can be represented by `n/2`) is larger or smaller than the value we are looking for
	- keep dividing the list in half looking for the value (`n/2*2*2...` and so on)
	- worst case scenario: we have to search the entire list (which can be represented by `n/2^i`) until we reach a list of length 1 or determine that the element is not present in the list 
	- so, stop when `n/2^i = 1`, which is the same as saying stop when `2^i >= n`, which is the same as saying `log2(n) = i`, which is the same as as saying "2 raised to the i-th power represents the number of times we would have to bisect a list in order to search the entire list"
	- therefore, the search complexity of a binary search is `log2(n)`

Bisection search implementation #1
```bisect_search1
def bisect_search1(L, e):
	if L == []:    # constant O(1)
		return False
	elif len(L) == 1:    # constant O(1)
		return L[0] == e
	else:
		half = len(L)//2    # constant O(1)
		if L[half] > e:
			return bisect_search1(L[:half], e)    # NOT constant, copies list
		else:
			return bisect_search1(L[half:], e)    # NOT constant, copies list
```
- complexity is O(log n) for the bisection search calls, but O(n) for EACH list copy operation because the list starts at length of 'n' before you cut it in half (slicing a list creates a copy)
- so, O(log n) for the recursive calls \* O(n) for each list copy operation inside the recursive call gives us O(n log n), "log linear"
- what if I didn't have to copy the list? what if I could just have a "pointer" and move the pointer to a different part of the existing list?

Bisection search implementation #2
```bisect_search2
def bisect_search2(L, e):
	def bisect_search_helper(L, e, low, high):
		if high == low:
			return L[low] == e
		mid = (low + high)//2
		if L[mid] == e:
			return True
		elif L[mid] > e:
			if low == mid: #nothing left to search
				return False
			else:
				return bisect_search_helper(L, e, low, mid - 1)
		else:
			return bisect_search_helper(L, e, mid + 1, high)
	if len(L) == 0:
		return False
	else:
		return bisect_search_helper(L, e, 0, len(L) - 1)
```
- still have the O(log n) complexity of the binary search, but we eliminated the list copying of O(n) complexity and replaced it with O(1) constant complexity operations
- **Note**: anything that is iterative and reduces the problem space by 1 each time is **linear**, anything that reduces the problemscape by half/third/quarter each time is going to be logarithmic in **complexity**

Convert ints to strings
```intToStr
def intToStr(i):
	digits = '0123456789'
	if i == 0:
		return '0'
	res = ''
	while i > 0:
		res = digits[i%10] + res
		i = i//10
	return result
```
- everything but the loop is constant complexity - O(1)
- each time through the loop, we reduce the scope of the problem by one tenth, `n/10*10*10...`
- problem is therefore represented as n/10<sup>i</sup> and we stop when n/10<sup>i</sup> >= n, which is the same as saying `log10(n) = i`
## Linear
- complexity commonly seen with loops and depends on the number of iterative calls
- cost of a loop may be constant each time but number of iterations of the loop is unknown
## Log-Linear
- next lecture
## Polynomial
- most common polynomial algorithms are quadratic, i.e. complexity grows with the square of the size of the input
- commonly occurs with nested loops or recursive function calls
## Exponential
- commonly occurs where we have more than one recursive call for each size of a problem (ex. Towers of Hanoi), **but not always**
- sometimes, exponential growth can also be "buried" in code without multiple recursive calls, such as when a loop gets larger every time a recursive call is made, ex. generating power sets
### Towers of Hanoi example
```towersOfHanoi	
def towersOfHanoi(n, source, target, spare):
	if n == 1:
		print('move from ' + str(source) + ' to ' + str(target))
	else:
		towersOfHanoi(n-1, source, spare, target)
		towersOfHanoi(1, source, target, spare)
		towersOfHanoi(n-1, spare, target, source)
```
#### Explanation:
- to solve Towers of Hanoi, you have to do 3 things:
	1. move a stack of n-1 disks from source to to spare
	2. then, move n-the (largest) disk from source to target
	3. finally, move the stack of n-1 disks from spare to target
- therefore, each time you move the largest disk (size of 1), you have to solve the problem for a stack of disks of size n-1 two times
- so, the time needed to solve a tower of size 'n' is the time it takes to solve the smaller tower two times, plus 1 for the time it takes to solve for the largest disk (a single move)
- in a formula, this looks like {$t_n = 2t_{n-1} + 1$}
- that formula eventually reduces down to {$t_n = 2^n - 1$}, which will give us Big Oh complexity of O(2<sup>n</sup>)
#### Math Breakdown:
1. If {$t_n = 2t_{n-1} + 1$}, then it follows that we can write {$t_{n-1}$} as {$t_{n-1} = 2t_{n-2} + 1$}
2. well now to solve for {$t_{n-1}$} in our first equation we can just substitute in our second equation!
	- {$t_n = 2(2t_{n-2} + 1) + 1$}
	- Reduces to {$t_n = 4t_{n-2} + 2 + 1$}
	- Further reduces to {$t_n = 4t_{n-2} + 3$}
3. well, if {$t_{n-2} = 2t_{n-3} + 1$}, then we can perform the same substitution to solve for {$t_{n-2}$} ... that's a pattern!
4. Our pattern can be written like this:
$$
t_n = 2^kt_{n-k} + (2^k - 1)
$$
5. We need to get $k$ out of there!
	- When {$k = n - 1$}, we find that {$t_{n-k}$} becomes {$t_{n-(n-1)}$} which is the same as {$t_{n-1(n-1)}$} which reduces to {$t_{n-n+1)}$}, which reduces again to {$t_1$} and eliminates $k$ from the equation
	- When we sub {$k = n - 1$} into the whole equation, it looks like this:
$$
t_n = 2^{n-1}t_1 + (2^{n-1} - 1)
$$
6. Now we can sub in our base case to get $t_1$ out of there!
	1. Base case: when {$n = 1$}, that means {$t_1 = 1$} because it takes 1 move to move 1 disk, so our base case we can use 1 in place of $t_1$
	2. Sub in base case: {$t_n = 2^{n-1}*1 + (2^{n-1} - 1)$}
	3. Reduce to: {$t_n = 2^{n-1} + 2^{n-1} - 1$}
	4. Combine like terms: {$t_n = 2 * 2^{n-1} - 1$}
	5. Use the exponent rule of {$a^m \cdot a^n = a^{m+n}$} to fully reduce:
		1. Another way to write our equation is: {$t_n = 2^1 * 2^{n-1} - 1$}
		2. Exponent rule: {$t_n = 2^{1+(n-1)} - 1$}
	6. Distribute: {$t_n = 2^{n+1-1} - 1$}
	7. Simplify for final result: {$t_n = 2^{n} - 1$}
### Generating power sets example
- Power set - the collection of all possible subsets of a set of integers
- {1, 2, 3, 4} would generate:
	- {}, {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}, {4}, {1, 4}, {2, 4}, {1, 2, 4}, {3, 4}, {1, 3, 4}, {2, 3, 4}, {1, 2, 3, 4}
- If we want to generate the power set of integers from 1 to `n`, then let's assume that we can generate the power set of integers from 1 to `n-1`. Then, all of those subsets must belong to the bigger power set. Furthermore, all of those subsets with `n` added to each of them must also belong to the bigger power set. Applied to the list above, this looks like:
	- {}
	- {}, {1}
	- {}, {1}, {2}, {1, 2}
	- {}, {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}
	- {}, {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}, {4}, {1, 4}, {2, 4}, {1, 2, 4}, {3, 4}, {1, 3, 4}, {2, 3, 4}, {1, 2, 3, 4}
```genSubsets
def genSubsets(L):
	if len(L) == 0:
		return [[]]    # list of empty list
	smaller = genSubsets(L[:-1])    # all subsets without last element 
	extra = L[-1:]    # create a list of just last element
	new = []
	for small in smaller:
		new.append(small+extra)    # for all smaller solutions, add one with last element
	return smaller+new    # combine those with last element and those without
```