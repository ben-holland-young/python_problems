from random import randint
# Write a program to generate all potential
# anagrams of an input string.

# For example, the potential anagrams of "biro" are

# biro bior brio broi boir bori
# ibro ibor irbo irob iobr iorb
# rbio rboi ribo riob roib robi
# obir obri oibr oirb orbi orib


def anagramise(a):
    n = len(a)
    a = list(a)
    new = ""
    for x in range(1,n):
        generated = randint(0,x)
        new += a[generated]
    return new
print(anagramise("hello"))


