print("Monoalphabetic cipher")
l=[]
for i in range(65,91):
    l.append(chr(i))
h=[]
for i in range(66,91):
    h.append(chr(i))
h.append(chr(65))
g=dict(zip(l,h))
n=input("enter a plain text")
k=[]
for c in n:
    k.append(g.get(c))
print(k)
f=''.join(k)
d=dict(zip(h,l))
b=[]
for i in f:
    b.append(d.get(i))
print(b)
