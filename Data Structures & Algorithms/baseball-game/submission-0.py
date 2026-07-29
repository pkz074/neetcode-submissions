class Solution:
    def calPoints(self, operations: List[str]) -> int:
    
        new_arr = []

        for op in operations:
            if op == "+":
                new_arr.append(new_arr[-1] + new_arr[-2])
            elif op == "D":
                new_arr.append(2 * new_arr[-1])
            elif op == "C":
                new_arr.pop()
            else:
                new_arr.append(int(op))

        return sum(new_arr)