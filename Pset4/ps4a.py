# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    # Base Case: There is only 1 permutation for a sequence of length 1 - return it.
    if len(sequence) == 1:
        return [sequence]
    # Recursive Case: The permutations for a sequence of length n > 1 can be found by
    # permuting all but the first letter of the sequence and then placing the first letter 
    # at every index of every returned permutation.
    else:
        permutations = []   # will hold all our found permutations
        first_char = sequence[0]    # the first char of the sequence to hold out
        received = get_permutations(sequence[1:])   # decrement the sequence by 1 character so that we eventually hit our base case; returns a list of strings of permutations of sequence[1:]
        for item in received:   # iterate over all permutations of sequence[1:]
            for n in range(len(item) + 1):  # first_char can be placed at the beginning, end, and inbetween every char of 'item', so we need to iterate len(item)+1 number of times
                permutations.append(item[:n] + first_char + item[n:])  # take everything before index 'n', concat first_char, then concat everything at and after index 'n'
        return permutations

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

# Sarah Test 1
    example = 'a'
    print('Input:', example)
    print('Expected Output:', ['a'])
    print('Actual Output:', get_permutations(example))
# Sarah Test 2
    example = 'ab'
    print('\nInput:', example)
    print('Expected Output:', ['ab', 'ba'])
    print('Actual Output:', get_permutations(example))
# Sarah Test 3
    example = 'abc'
    print('\nInput:', example)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example))