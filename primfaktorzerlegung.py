import math

def primfaktorzerlegung(n):
    t=2
    list = []
    print("primfaktoren für zahl: " + str(n))
    while t<=math.sqrt(n):
        if n%t ==0:
            print(str(t) + "*")
            n/=t
        else:
            t=t+1
    print(int(n))
  

        


primfaktorzerlegung(12)
primfaktorzerlegung(123)
primfaktorzerlegung(360)
primfaktorzerlegung(754)

