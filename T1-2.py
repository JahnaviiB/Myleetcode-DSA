# Sunwoo Yeom
# syeom2@student.gsu.edu
# CSC 2720 024
# 09/12/2023
# LAB 4

# for just solving...

# get input for s and t

s = str(input("Enter input for s: "))

t = str(input("Enter input for h: "))

def anagram(a, b):
    if len(a) == len(b):
        # sorting inputs
        if sorted(a) == sorted(b):
            print("True")
        else:
            print("False")
    else:
        print("False")

anagram(s, t)



