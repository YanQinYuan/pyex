__author__ = 'yangqinyuan'

# 思路：先判断是否每个字母都在second Word ，再判断每个字母的出现次数是否等于second word上的出现次数

def verify_anagrams(first_word, second_word):
    return "".join(sorted(first_word.lower())).strip() == ''.join(sorted(second_word.lower())).strip()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams(
        "Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams(
        "Kyoto", "Tokyo") == True, "The global warming crisis of 3002"
