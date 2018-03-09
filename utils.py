import random

def gen_korean_letter():
    letter_korean_flist = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', \
                           'ㅅ','ㅆ', 'ㅇ', 'ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
    letter_korean_mlist = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', \
                           'ㅗㅏ','ㅗㅐ', 'ㅗㅣ', 'ㅛ','ㅜ','ㅜㅓ','ㅜㅔ','ㅜㅣ','ㅠ',\
                           'ㅡ','ㅡㅣ','ㅣ']
    letter_korean_llist = ['', 'ㄱ', 'ㄲ', 'ㄱㅅ', 'ㄴ', 'ㄴㅈ', 'ㄴㅎ', 'ㄷ', 'ㄹ', \
                           'ㄹㄱ','ㄹㅁ', 'ㄹㅂ', 'ㄹㅅ','ㄹㅌ','ㄹㅍ','ㄹㅎ', 'ㅁ', \
                           'ㅂ', 'ㅂㅅ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    CODE_INITIAL_KOREAN_UTF8_LETTER = ord('가')

    fchoice = random.choice(['ㄱ', 'ㄴ'])
    mchoice = random.choice(letter_korean_mlist)
    lchoice = '' #random.choice(letter_korean_llist)

    findex = letter_korean_flist.index(fchoice)
    mindex = letter_korean_mlist.index(mchoice)
    lindex = letter_korean_llist.index(lchoice)

    letter_code = CODE_INITIAL_KOREAN_UTF8_LETTER + lindex + mindex * len(letter_korean_llist) + findex * len(letter_korean_mlist) * len(letter_korean_llist)
    letter_str  = chr(letter_code)
    return letter_str

def randomword(length):
    return ''.join(random.choice(list('abcdefghijklmnopqrstuvwxyz0123456789')) for i in range(length))
