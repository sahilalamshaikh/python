text = input("Enter the text")
if "make a lot of money fast " in text:
    spam = True
elif "buy now" in text:
    spam = True
elif "watch this" in text:
    spam = True
elif "click this" in text:
    spam = True
else:
    spam = False

if spam:
    print(" This text is spam")
else:
    print("this is not spam")
