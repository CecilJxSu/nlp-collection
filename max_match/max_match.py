#!/usr/bin/env python3

def max_match(sentence, dictionary):
    if not sentence:
        return []
    for i in range(len(sentence), 0, -1):
        firstword = sentence[:i]
        remainder = sentence[i:]
        if firstword in dictionary:
            list = max_match(remainder, dictionary)
            list.insert(0, firstword)
            return list

    firstword = sentence[:1]
    remainder = sentence[1:]
    list = max_match(remainder, dictionary)
    list.insert(0, firstword)
    return list

if __name__ == '__main__':
    # ---------------- Example 1 ----------------
    dictionary = ['你', '我', '他', '喜欢', '特别', '北京', '烤鸭', '北京烤鸭']
    sentence = '他特别喜欢北京烤鸭'
    list = max_match(sentence, dictionary)
    # ['他', '特别', '喜欢', '北京烤鸭']
    print(list)

    # ---------------- Example 2 ----------------
    dictionary = ['we', 'can', 'only', 'see', 'a', 'short', 'distance', 'ahead',
                  'canon', 'l', 'y', 'ash', 'ort']
    # We can only see a short distance ahead
    sentence = 'wecanonlyseeashortdistanceahead'
    list = max_match(sentence, dictionary)
    # ['we', 'canon', 'l', 'y', 'see', 'ash', 'ort', 'distance', 'ahead']
    print(list)
