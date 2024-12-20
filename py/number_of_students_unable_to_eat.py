'''
https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
'''

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = collections.deque()

        for student in students:
            q.append(student)
        
        while len(q) > 0:
            if sandwiches[0] == q[0]:
                q.popleft()
                sandwiches.pop(0)
            else:
                rotateCount = 0
                while sandwiches[0] != q[0]:
                    firstStudent = q.popleft()
                    q.append(firstStudent)
                    rotateCount += 1
                    if rotateCount > len(q):
                        return len(q)
        
        return 0