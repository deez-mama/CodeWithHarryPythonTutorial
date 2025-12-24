# Repeat program 4 for a list of such words to be censored.

with open ("Donkey.txt",) as f:
    content=f.read().lower()   

with open ("Donkey.txt","w")as f:
    if "donkey" in content:
        content=content.replace("donkey","#####")
    if "mad" in content:
        content=content.replace("mad","#####")
    if "stupid" in content:
        content=content.replace("stupid","#####")
    
    f.write(content)

"""
Or a better way would be making a list of bad words

words=["donkey","stupid","mad"]\
for word in words
    content=content.replace(word,"#####")

"""
