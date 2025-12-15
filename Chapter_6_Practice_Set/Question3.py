"""
A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams.
"""

comment=input("Enter your comment: ")

lower=comment.lower()

if("make a lot of money" in lower or "buy now" in lower or "subscribe this" in lower or "click this" in lower):
    print("This is a spam comment")

