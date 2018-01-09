


class Solution:
    def reverse(self,x):

        if x==0:
            return 0

        if x>=0:
            return self.judge_int(self.reverse_positive(x))
        else:
            return self.judge_int(self.reverse_negative(x))

    def judge_int(self,x):
        if x<-2**31 or x>2**31-1:
            return 0
        else:
            return x

    def reverse_positive(self,x):
        str_int=str(x)
        list_int=list(str_int)
        list_int.reverse()
        flag=True
        result=''
        for s in list_int:
            if flag:
                if s=='0':
                    continue
                else:
                    flag=False
                    result+=s
            else:
                result += s

        return int(result)


    def reverse_negative(self,x):
        str_int = str(x)
        list_int = list(str_int)[1:]
        list_int.reverse()
        flag = True
        result = ''
        for s in list_int:
            if flag:
                if s == '0':
                    continue
                else:
                    flag = False
                    result += s
            else:
                result += s

        return 0-int(result)

if __name__ == '__main__':
    s=Solution()
    print(s.reverse(1534236469))

    x=1234567890
    ss=(x>0)-(x<0)
    print(str(ss*x)[::-1])
    r=int(str(ss*x)[::-2])
    print(r*ss*(r<2**31))