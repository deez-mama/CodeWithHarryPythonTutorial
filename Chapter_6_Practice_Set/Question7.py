# Write a program to find out whether a given post is talking about “Harry” or not.

post=input("Enter the post content: ")

if("Harry".lower() in post.lower()):
    print("The post talks about Harry")

else:
    print("The post does not talk about Harry")

