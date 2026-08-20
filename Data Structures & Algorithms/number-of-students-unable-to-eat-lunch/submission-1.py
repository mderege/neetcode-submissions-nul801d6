import collections 
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        j = 0
        st = deque(students)
        ro = len(students)
        while ro > count:
            if st[0] == sandwiches[j]:
                st.popleft()
                j+=1
                ro -=1 
                count = 0
            else:
                curr = st.popleft()
                st.append(curr)
                count+=1
        return ro
            

        