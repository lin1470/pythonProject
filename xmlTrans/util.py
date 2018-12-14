def is_chinese(words):
    for ch in words:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


def chinese2html(words):
    transword = list()
    retstring = ''
    for word in words:
        # print(word)
        word = word.encode('unicode_escape').decode().upper().replace('\\U','&#x')
        word = word+';'
        # print(word)
        transword.append(word)
    for word in transword:
        retstring += word
    return retstring

print("金文坚".encode('unicode_escape').decode())
print(chinese2html("金文坚"))