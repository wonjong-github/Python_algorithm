class Solution(object):
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letters, digits = list(), list()
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters+digits
