BASE_CODE, CHO_CODE, JUNG_CODE, MAX_CODE = 44032, 588, 28, 55203

CHO_LIST = list('ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ')
JUNG_LIST = list('ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ')
JONG_LIST = list(' ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ')

KORS = list('ㄱㄲㄳㄴㄵㄶㄷㄸㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅃㅄㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ')
ENGS = ['r', 'R', 'rt', 's', 'sw', 'sg', 'e', 'E', 'f', 'fr', 'fa', 'fq', 'ft', 'fx', 'fv', 'fg', 'a', 'q', 'Q', 'qt',
        't', 'T', 'd', 'w', 'W', 'c', 'z', 'x', 'v', 'g',
        'k', 'o', 'i', 'O', 'j', 'p', 'u', 'P', 'h', 'hk', 'ho', 'hl', 'y', 'n', 'nj', 'np', 'nl', 'b', 'm', 'ml', 'l']
KOR_ENG_TABLE = dict(zip(KORS, ENGS))


def kor2eng(text):
    res = []
    res2 = []
    for ch in text:
        spl = split(ch)
        if spl is None: #캐릭터가 영어라면
            res.append(ch)
            res2.append(False)
        else: #캐릭터가 한글이라면
            res.append(''.join([KOR_ENG_TABLE[v] for v in spl if v != ' ']))
            res2.append(True)
    return res, res2


"""
def kor2eng(text):
    res = ''
    for ch in text:
        spl = split(ch)
        if spl is None: #캐릭터가 영어라면
            res += ch
        else: #캐릭터가 한글이라면
            res += ''.join([KOR_ENG_TABLE[v] for v in spl if v != ' '])
    return res
"""

def combine(cho, jung, jong):
    res = BASE_CODE
    res += 0 if cho == ' ' else CHO_LIST.index(cho) * CHO_CODE
    res += 0 if jung == ' ' else JUNG_LIST.index(jung) * JUNG_CODE
    res += JONG_LIST.index(jong)
    return chr(res)


def split(kor):
    code = ord(kor) - BASE_CODE
    if code < 0 or code > MAX_CODE - BASE_CODE:
        if kor == ' ': return None
        if kor in CHO_LIST: return kor, ' ', ' '
        if kor in JUNG_LIST: return ' ', kor, ' '
        if kor in JONG_LIST: return ' ', ' ', kor
        return None
    return CHO_LIST[code // CHO_CODE], JUNG_LIST[(code % CHO_CODE) // JUNG_CODE], JONG_LIST[(code % CHO_CODE) % JUNG_CODE]


if __name__ == '__main__':
    print(split('뷁'), split('하'), split('a'), split('b'))
    print(combine(*split('뷁')))
    print(kor2eng('안녕하세요 파이썬은 정말 최고에요 abc'))