# def sum_list(items):
#     sum = 0
#     for x in items:
#         sum += x
#     return sum
# print(sum_list([1, 2, 3]))
# OUTPUT:6

# write a python program to multiply all the items in a list
# def mul_list(items):
#     total=1
#     for i in items:
#         total=total*i
#     return total
# print(mul_list([2,4,2]))

# OUTPUT:
# 16

# stack = []
#
#
# def push():
#     if len(stack) == n:
#         print("Stack is Full")
#     else:
#         elements = input("Enter a number")
#         stack.append(elements)
#         print(stack)
#
#
# def pop_element():
#     if not stack:
#         print("stack is empty")
#     else:
#         k = stack.pop()
#         print("removed element", k)
#         print(stack)
#
#
# n = int(input("Enter a limit:"))
# while True:
#     print("select the operation 1.push 2.pop 3.quit")
#     choice = int(input())
#     if choice == 1:
#         push()
#     elif choice == 2:
#         pop_element()
#     elif choice == 3:
#         break
#     else:
#         print("Enter the correct operations!")


# import queue
# stack=queue.LifoQueue(3)
# stack.put(10)
# stack.put(102)
# stack.put(150)
# stack.get()
# stack.get()
# stack.get()

# import collections
# queue=collections.deque()
# queue.append(78)
# queue.append(782)
# queue.append(738)
# queue.append(378)
# queue

def pyramid(rows):
    for i in range(rows):
        print(''*(rows-i-1)+'* '*(i+1))
    for j in range(rows-1,0,-1):
        print(''*(rows-j)+'* '*(j))