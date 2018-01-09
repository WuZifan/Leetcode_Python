
# 不知道为什么过不了= -
def solution(strs):
    result=""
    temp=strs[0]
    count=1
    for s in strs[1:]:
        if temp==s:
            count+=1
        else:
            if count==1:
                result+=str(temp)
            else:
                result+=str(temp)+str(count)
            temp=s
            count=1

    if count == 1:
        result += str(temp)
    else:
        result += str(temp) + str(count)

    compressed=list(result)

    return len(compressed)

if __name__ == '__main__':

    print(solution(["a","a","b","b","c","c","c"]))