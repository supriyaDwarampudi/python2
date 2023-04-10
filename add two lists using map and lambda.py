l1=[1,2,3]
l2=[3,4,5]
print(l1)
print(l2)
result=map(lambda x,y:x+y,l1,l2)
print(list(result))

#output:
# [1, 2, 3]
# [3, 4, 5]
# [4, 6, 8]

# r=zip(l1,l2)
# print(list(r))              #output:    [(1, 3), (2, 4), (3, 5)]