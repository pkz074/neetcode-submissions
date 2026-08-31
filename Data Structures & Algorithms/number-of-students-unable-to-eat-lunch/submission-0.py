class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        
        qntity = Counter(students)
        res = len(students)

        for s in sandwiches:
            if qntity[s] > 0:
                res -= 1
                qntity[s] -= 1
            else:
                break
        return res
