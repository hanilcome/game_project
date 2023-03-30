def solution(array):
    answer = 0
    b = {}
    for i in array:
        b[i] = array.count(i)  # key값과 value값을 가져옴
    for i in b:
        if max < b[i]: #  b = key값, b[i] = value값 
            max = b[i]
            answer = max
        elif max == b[i]:
            answer = -1
    return answer

print(solution)











