## Search Algorithms
- search algorithm - method for finding an item or group of items with specific properties within a collection of items
- collections can be implicit or explicit
	- implicit ex. - find the square root of a number
	- explicit ex. - is a student record in a stored collection of data?

## Searching algorithms
- linear/brute force search
	- list does not have to be sorted
	- typically linear complexity, O(n)
- bisection search
	- list must be sorted
	- typically logarithmic in complexity, O(log n)

## So... when does it make sense to sort then search?
- Makes sense to sort first when the cost of sorting plus the cost of an algorithm of logarithmic complexity is less than the cost of an algorithm of linear complexity
- This can be expressed as: `SORT + O(log n) < O(n)`, which is the same as saying `SORT < O(n) - O(log n)`
- HOWEVER, this relationship is never true - in order to sort a collection of elements, we must look at each one at least once!
- why bother sorting then? because for a very large number of searches, we can amortize the cost of the search over each search - gains the benefit of many searches using O(log n) with only 1 initial, expensive O(n) sort

## Sorting algorithms
### Monkey/bogo sort
- randomly reshuffle the list until it is sorted
- in the best case complexity is O(n), but in the worst case the complexity is unbounded
```bogo_sort
def bogo_sort(L):
	while not is_sorted(L):
		random.shuffle(L)
```
### Bubble sort
- compare consecutive pairs of elements, swap elements in the pair so that the smallest is first, when you reach the end of the list you start over, and stop when no more swaps have been made
- result is that the largest element is at the end after the first pass, then the second largest is second from the end after the second pass, etc... so at most you need to go through a list of length 'n' only 'n' number of times
```bubble_sort
def bubble_sort(L):
	swap = False
	while not swap:    # O(len(L))
		swap = True
		for j in range(1, len(L)):    # O(len(L))
		if L[j-1] > L[j]:
			swap = False
			temp = L[j]
			L[j] = L[j-1]
			L[j-1] = temp
```
- Complexity of `bubble_sort()` above is O(n<sup>2</sup>) - in the worst case, you have to make 'n' number of swaps 'n' number of times, and n\*n is n<sup>2</sup>
### Selection sort
- kind of like a backwards bubble sort: find the smallest element and swap it to index 0, find the next smallest element and swap it to index 1, etc.
- result is that at step 'i' of the loop you know that the first 'i' elements of the list are sorted and the remaining items in the list are bigger than the first 'i' elements
```selection_sort
def selection_sort(L):
	suffixSt = 0
	while suffixSt != len(L):    # len(L) times = O(len(L))
		for i in range(suffixSt, len(L)):    # len(L)-suffixSt times = O(len(L))
			if L[i] < L[suffixSt]:
				L[suffixSt], L[i] = L[i], L[suffixSt]
		suffixSt += 1
```
- Complexity of `selection_sort()` above is still O(n<sup>2</sup>) - in the worst case, you have to make 'n' number of swaps 'n' number of times, and n\*n is n<sup>2</sup>
### Merge sort
- divide-and-conquer approach:
	1. if list length is 0 or 1, list is already sorted
	2. if list has more than one element, split the list into two lists and sort each of those
	3. finally, merge the sorted sublists:
		1. look at the first element of each sublist and move the smaller of the two to the end of your result
		2. when one list is empty, just copy the rest of the other list
- splitting lists in half occurs until you have sublists of only 1 element, then you start to merge - after a merge, you know that the result of the merge is sorted
```merge
def merge(left, right):
	result = []
	i,j = 0,0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	while (i < len(left)):
		result.append(left[i])
		i += 1
	while (j < len(right)):
		result.append(right[j])
		j += 1
	return result
```
- `merge` complexity is linear O(n) and based on the length of the longer list
```merge_sort
def merge_sort(L):
	if len(L) < 2:    # base case
		return L[:]
	else:
		middle = len(L)//2    # divide up the problem
		left = merge_sort(L[:middle])
		right = merge_sort(L[middle:])
		return merge(left, right)    # conquer with the merge step
```
- `merge_sort` complexity is O(n log n) because you divide the problem scope in half with each recursive call giving O(log n) and then do O(n) amount of work
- O(n log n) is the fastest a sort can be in the worst case scenario!