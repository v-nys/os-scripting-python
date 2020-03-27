import python_spam_file_functie
import os

def spam_filter():
    path = input("Welke directory wil je analyseren?")
    for fn in os.listdir(path):
        abspath = os.path.join(path,fn)
        if python_spam_file_functie.file_is_spam(path):
            print(f"{abspath}: spam")
        else:
            print(f"{abspath}: geen spam")
