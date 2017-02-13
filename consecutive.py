def longest_consec(strarr, k):
        # your code
        n = len(strarr)
        if n == 0 or k > n or k <= 0:
            return ""
        strarr.sort(key = len)
        newString = ""
        for x in range(1,k+1):
            newString += strarr[n-x]

        return newString


