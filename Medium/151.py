class Solution:
    '''
        要求：
            单词内正序，单词间倒叙
            头尾没有空格，单词间仅一个空额

    '''
    def reverseWords(self, s: str) -> str:
        ret_str = ''
        temp_str =''
        for c in s:
            if c == ' ':
                if len(temp_str)>0:
                    if len(ret_str)>0:
                        ret_str=temp_str+' '+ret_str
                    else:
                        ret_str=temp_str+ret_str
                    temp_str=''
            else:
                temp_str+=c

        if len(temp_str)>0 and len(ret_str)>0:
            ret_str=temp_str+' '+ret_str
        else:
            ret_str=temp_str+ret_str
        return ret_str

    def reverseWords3(self,s:str)->str:
        return ' '.join(reversed(s.split()))

    def reverseWords2(self,s:str)->str:
        '''
        每当空格来了，就pop现在内容
        :param s:
        :return:
        '''
        temp_str = ''
        ret_str = ''
        for c in s:
            if c !=' ':
                temp_str+=c
            elif c == ' ':
                if len(temp_str)>0:
                    ret_str = temp_str+ret_str
                    temp_str=''

        return ret_str
        pass


if __name__ == '__main__':
    s  =Solution()
    str1 = "the sky is blue"
    str2 = "  hello world!  "
    str3='a'
    str4 = "  hello world!  "
    res = s.reverseWords3(str2)
    print(res,len(res))