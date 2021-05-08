"""
https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first
if you want to take course ai. For example, the pair [0, 1], indicates that to take course 0 you have to first take
course 1.

Return true if you can finish all courses. Otherwise, return false.
"""

from typing import List
from collections import defaultdict, deque


class Solution:

    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        """Use Kahn's algorithm as defined here https://en.wikipedia.org/wiki/Topological_sorting#Algorithms"""
        adj_list = defaultdict(list)
        num_of_prereqs = [0] * num_courses  # number of prerequisites for a course

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            num_of_prereqs[course] += 1

        courses_with_no_prereqs = deque()
        for course in range(num_courses):
            if num_of_prereqs[course] == 0:
                courses_with_no_prereqs.append(course)

        top_sorted = []
        while courses_with_no_prereqs:
            prereq = courses_with_no_prereqs.popleft()
            top_sorted.append(prereq)

            for course in adj_list[prereq]:
                num_of_prereqs[course] -= 1
                if num_of_prereqs[course] == 0:
                    courses_with_no_prereqs.append(course)

        return len(top_sorted) == num_courses


if __name__ == "__main__":
    t_prer = [[1, 0], [3, 1], [2, 1]]
    t_num = 4
    s = Solution()
    print(s.canFinish(num_courses=t_num, prerequisites=t_prer))
