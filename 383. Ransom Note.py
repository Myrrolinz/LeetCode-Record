
def canConstruct(ransomNote: str, magazine: str) -> bool:
    from collections import Counter
    cnt_ransom = Counter(ransomNote)
    cnt_magazine = Counter(magazine)
    for letter in cnt_ransom:
        print(f"letter: {letter}")
        if letter not in cnt_magazine or cnt_ransom[letter] > cnt_magazine[letter]:
            print(f"letter: {letter} not in cnt_magazine or {cnt_ransom[letter]} > {cnt_magazine[letter]}")
            return False
        
    return True

    # 最简单的写法只要这一句：return not Counter(ransomNote) - Counter(magazine)

ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
print(canConstruct(ransomNote, magazine)) # True