

disallowed_words = ["word",'word2','word3','word4','word5']
text = input("Word plz!:")
text_res = ''


"""
for Word in List2:
    for letter in text:
        flag = False
        for i in range(len(Word)):
            if Word[i] == letter:
                flag = True
                text_res += letter

        if not flag:
            text_res =""
            break
    if text_res in List2:
        print("ff")
"""#FOR NOT HIDDEN WORD#

temp_text = ""
for Word in disallowed_words:
    flag = False
    for i2 in range(len(Word)):
        for i in range(len(text)):
            if Word[i2] == text[i]:
                sum = len(Word)
                temp_text = text[i:]
                res1 = ""

                res1 += temp_text[0:sum]
                if res1 == Word:
                    print(word )
            else:
                text_res =""

