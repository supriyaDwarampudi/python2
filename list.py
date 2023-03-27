# list=[1,'priya',True]
# for i in list:
# print(list[-1])
#
# l=[13,14,15,16,11,19,23,33]
#  print(l[0:3:2])
#
# l=[13,14,15,16,11,19,23,33]
# print(l[-1:-4:-2])
# l=[13,12,'sai',67]
# l.append(14)
# print(l)

# l=[13,34.28,29,31]
# k=l.copy()
# print(k)
# l.append('priya')
# print(l)

# l=[1,22,3,3,4,5,6,7,5]
# print(l.count(3))

# l=[1,2,3,4]
# k=l.clear()
# print(k)

# l=[13,14,15,16,17]
# l.insert(5,'priya')
# print(l)

# l=[12,13,14,'priya']
# l.pop(3)
# l.remove('priya')
# print(l)

# l=[1,2,3]
# k=l[::-1]
# m=[13,14,15]
# m.reverse()
# print(m)
# print(k)

# a = input()
# b = a.split()
# m = []
# for i in b:
#     if len(m) % 2 != 0:
#         m.append(i[::-1])
#     else:
#         m.append(i)
# c = " ".join(m)
# print(c)

# l='My Name Is Supriya Reddy'
# n=l.split()
# print(n)
# m=[]
# for i in n:
#     if len(m)%2!=0:
#         m.append(i[::-1])
#     else:
#         m.append(i)
# d=" ".join(m)
# print(d)
#
# l=input('Enter your name')
# m=l.split()
# print(m)
# n=[]
# for i in m:
#     if len(n)%2==0:
#         n.append(i[::-1])
#     else:
#         n.append(i)
# o=" ".join(n)
# print(o)

s='Iam Learning Python'
k=s.split()
print(k)
m=[]
for i in k:
    if i == 'Python':
        m.append(i[::-1])
    else:
        m.append(i)
d=" ".join(m)
print(d)

