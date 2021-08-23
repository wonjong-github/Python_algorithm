import itertools


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return list(map(list, itertools.combinations(list(range(1, n+1)), k)))


print(range(5))
# for t in itertools.combinations(range(1, 6), 3):
#     print(t)
k = "kitjb"
print(sorted(k))
t = list(map(list, itertools.permutations(sorted(k), 2)))
print(''.join(t[t.index(list(k))+1]))