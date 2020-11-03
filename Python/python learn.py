class E:
    i=3

print(E.i)

E.i=2

s=E()
s.i=5
print(s.i,E.i)