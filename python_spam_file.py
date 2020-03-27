import python_spam_regel_functie

def file_is_spam():
    answer = input("Welke file moet gecontroleerd worden?\n")
    path = answer.split(" ")
    with open(answer) as fh:
        is_spam = False
        for line in fh.readlines():
            is_spam = is_spam or python_spam_regel_functie.check_spam_line(line)
    if is_spam:
        print("Deze file bevat spam!")
    else:
        print("Deze file is in orde!")
