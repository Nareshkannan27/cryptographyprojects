l=[]
for i in range(65,91):
    l.append(chr(i))
    
h=[]
for i in range(0,26):
    h.append(i)
    
u=dict(zip(l,h))
print(u)

t=list(u.items())
n=input("enter a string")
key=int(input("entert a key value"))
r=[]
for c in n:
    t=u.get(c)
    b=(t+key)%26
    r.append(b)
print(r)
reverse=dict(zip(h,l))
s=[]
for i in r:
    s.append(reverse.get(i))
ciphertext=''.join(s)
print(ciphertext)
e=[]
for c in ciphertext:
    t=u.get(c)
    b=(t-key)%26
    e.append(b)
print(e)
v=[]
for i in e:
     v.append(reverse.get(i))
plaintext=''.join(v)
print(plaintext)
    
    
    
    
    
    
