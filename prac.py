def middle(s):
    answer=''
    answer_len = len(s)
    if answer_len % 2 == 0:
        answer = s[answer_len//2-1:answer_len//2+1]
    else:
        answer = s[answer_len//2]
    return answer
        
a='abcdefg'
print(middle(a))
b='qwer'
print(middle(b))


