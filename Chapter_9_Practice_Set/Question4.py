# A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.

with open ("Donkey.txt",) as f:
    content=f.read().lower()   

with open ("Donkey.txt","w")as f:
    if "donkey" in content:
        f.write(content.replace("donkey","#####"))


