# Write a python function to remove a given word from a list and strip it at the same time.

def rem(my_list,word):
    n=[]
    for item in my_list:
        if not(item==word):
            n.append(item.strip())
    return n



my_list=["apple","banana","cherry","kiwi","mango","banana"]
word=input("Enter a word to remove from the list: ")