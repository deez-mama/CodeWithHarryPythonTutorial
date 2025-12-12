#Write a program to fill in a letter template given below with name and date.
"""letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
"""

name=input("Enter your name: ")
date=input("Enter date: ")

print("letter = '''\nDear ", name, "\nYou are selected!\n",date,"\n'''")

"""
Another way to do this is:

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>

print(letter.replace("<|Name|>", name).replace("<|Date|>", date))

"""