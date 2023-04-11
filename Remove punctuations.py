punctuations="'''''!@#$%^&*()_+,.>"
my_str=input('Enter a string:')
new_str=""
for c in my_str:
    if c not in punctuations:
        new_str+=c
print(new_str)


# output
# Enter a string:Hi My name is supriya Reddy, and i am studying BTech Oh! my god.
# Hi My name is supriya Reddy and i am studying BTech Oh my god
