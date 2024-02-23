class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # circular sandwich = 0
        # square sandwich =  1

        count = len(students)
        while sandwiches and students and sandwiches[0] in students:

            # if the first student does not like the upper sandwich
            if sandwiches[0] != students[0]:
                students.append(students[0])
                students.pop(0)

            # if the first student like the upper sandwich
            else:
                students.pop(0)
                sandwiches.pop(0)
                count -= 1

        return count
