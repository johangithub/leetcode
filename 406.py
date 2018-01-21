"""
Suppose you have a random list of people standing in a queue.
Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people
in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.
Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""
people = [[5,0], [6,1], [7,0], [4,4], [7,1], [5,2]]
def reconstructQueue(people):
    res = []
    for p in sorted((-x[0], x[1]) for x in people):
        res.insert(p[1], [-p[0], p[1]])
    return res

"""
Explanation and solution from @SergeyTachenov:
Imagine you only had the tallest people. Then the you would sort them based on the second index,
since they only see themselves and themselves only. e.g. [[7, 0], [7, 1], ... ]
Then the next tallest group, and the second index would indicate exactly where they should be.
and so on and on.
The second part was confusing at first, but playing with it and writing it down on paper made it easier to understand.

"""