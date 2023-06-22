# def is_overlaping(a, b):
#   if b[0] > a[0] and b[0] < a[1]:
#     return True
#   else:
#     return False
#
#
# # merge the intervals
# def merge(arr):
#   #sort the intervals by its first value
#   arr.sort(key = lambda x: x[0])
#
#   merged_list= []
#   merged_list.append(arr[0])
#   for i in range(1, len(arr)):
#     pop_element = merged_list.pop()
#     if is_overlaping(pop_element, arr[i]):
#       new_element = pop_element[0], max(pop_element[1], arr[i][1])
#       merged_list.append(new_element)
#     else:
#       merged_list.append(pop_element)
#       merged_list.append(arr[i])
#   return merged_list
# arr=[[1,3],[2,6],[8,10]]
# # print(merge(arr))
#
# n = int(input('Enter a number'))
# count = 0
# while n > 0:
#     n = n // 10
#     count = count
# print(count)
# num = int(input("enter a number"))
# n=num
# while n> 10:
#
#     n=n// 10
#
# print("{} is the first digit of {}".format(n,num))
# num = int(input("enter a number"))
#
# n = num
#
# total = 0

# while n != 0:
#
#     rem = n % 10
#
#     total = total + rem
#
#     n = n // 10
#
# print(total)


# j='priya'
# s="supriya reddy"
# f='''Dwarampudi supriya reddy
# hbfeuegfb
#   cdhgfyecb
#   cdyfugfbc
#   fdmvnueify'''
# print(type(j))
# print(type(s))
# print(type(f))

#
# m=('APPLE','BALL','CAR')
# v=m.lower()
# print(v)

# p='my fav god is sai'
# # print(p.index('durga'))
# print(p.find('durga'))
