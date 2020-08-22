"""
Given a linked list which contains some loop.
You need to find the node, which creates a loop, and break it by making the node point to NULL.
"""
class Solution:
    def solve(self, A):
        visited = set()
        temp = A
        visited.add(temp)
        while temp.next:
            if temp.next in visited:
                temp.next = None
                return A
            else:
                temp = temp.next
                visited.add(temp)
        return A