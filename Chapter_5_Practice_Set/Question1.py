# Write a program to create a dictionary of Nepali words with values as their English
# translation. Provide user with an option to look it up!

Nepali_dict={
    "Namaste": "Hello",
    "Dhoka" : "Door",
    "Paani" : "Water"
}

word=input("Enter a Nepali word to translate: ")

print(Nepali_dict.get(word))
