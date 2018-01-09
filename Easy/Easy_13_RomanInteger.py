'''
这道题的关键就是理解这个罗马数字的构成啊。。。。
(1)基本数字Ⅰ、X 、C 中的任何一个，自身连用构成数目，或者放在大数的右边连用构成数目，都不能超过三个；放在大数的左边只能用一个。
(2)不能把基本数字 V 、L 、D 中的任何一个作为小数放在大数的左边采用相减的方法构成数目；放在大数的右边采用相加的方式构成数目，只能使用一个。
(3)V 和 X 左边的小数字只能用Ⅰ。
(4)L 和 C 左边的小数字只能用×。
(5)D 和 M 左 边的小数字只能用 C 。
'''


# 仅限二十以内
def romanToInt( s):
    conver_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_list = list(s)
    result=0
    length=len(roman_list)
    for ind,r in enumerate(roman_list):
        if r=='I':
            if ind<length-1 and (roman_list[ind+1]=='V' or roman_list[ind+1]=='X'):
                result-=conver_dict.get(r)
            else:
                result+=conver_dict.get(r)
        if r=='X':
            if ind<length-1 and (roman_list[ind+1]=='L' or roman_list[ind+1]=='C'):
                result-=conver_dict.get(r)
            else:
                result+=conver_dict.get(r)
        if r=='C':
            if ind<length-1 and (roman_list[ind+1]=='D' or roman_list[ind+1]=='M'):
                result-=conver_dict.get(r)
            else:
                result+=conver_dict.get(r)

        if r=='V':
            result+=conver_dict.get(r)

        if r=='L':
            result+=conver_dict.get(r)

        if r=='D':
            result+=conver_dict.get(r)

        if r=='M':
            result+=conver_dict.get(r)

    return result


if __name__ == '__main__':
    print(romanToInt('XV'))
