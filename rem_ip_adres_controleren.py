def bestaat_uit_bytes(s):
    elements = s.split(".")
    result = True
    for elem in elements:
        num = int(elem)
        if not (num >= 0 and num <= 255):
            result = False
    return result

