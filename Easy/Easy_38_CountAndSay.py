def read(n):
    num_list = list(str(n))

    temp = num_list[0]
    count = 1

    result = ''
    for ind, num in enumerate(num_list[1:]):
        if temp == num:
            count += 1;
        else:
            result += str(count)
            result += str(temp)
            temp = num
            count = 1

    result += str(count)
    result += str(temp)

    return result


def solution(n):
    if n == 1:
        return str(1)

    else:
        result= 1
        for i in range(0, n-1):
            result = int(read(result))

    return str(result)

if __name__ == '__main__':
    print(solution(4))
