def check_spam_line(line):
    words = line.split(" ")
    is_spam = False
    for word in words:
        if word == "lottery" or word == "inheritance" or word == "viagra":
            is_spam = True
    return is_spam
