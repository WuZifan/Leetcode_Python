
# 问题：找到一系列字符串的最长公共前缀

# 思路：找到最短的字符串之一，从它的第一个字符开始搜索，就可以找到最长的。

def solution(strs):
    if len(strs)==0:
        return ''
    str_list=sorted([(len(str),str) for str in strs])

    target=str_list[0][1]
    target_list=list(target)
    prefix=''
    for c in target_list:
        prefix+=c
        for ss in strs:
            if not ss.startswith(prefix):
                prefix=prefix[:-1]
                break
    return prefix

if __name__ == '__main__':
    str_list=[]
    print(solution(str_list))