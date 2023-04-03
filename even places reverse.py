s="My name is priya"
k=s.split()
print(k)
m=[]
for i in k:
    if i=='name'or i=='priya':
        m.append(i[::-1])
        print(m)
    else:
        m.append(i)
        print(m)
d=" ".join(m)
print(d)


output:-
['My', 'name', 'is', 'priya']
['My']
['My', 'eman']
['My', 'eman', 'is']
['My', 'eman', 'is', 'ayirp']
My eman is ayirp
