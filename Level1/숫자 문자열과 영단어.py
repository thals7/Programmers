def solution1(s):
    num = ["0","1","2","3","4","5","6","7","8","9"]
    num_s = ["zero","one","two","three","four","five","six","seven","eight","nine"]

    answer = ''
    string = ''
    for char in s:
        if char in num:
            answer += char
            continue
        string += char
        if string in num_s:
            answer += num[num_s.index(string)]
            string = ''
    return int(answer)

# dict 활용
def solution2(s):
    num = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    answer = s
    for key, value in num.items():
        answer = answer.replace(key,value)
    # for item in num:
    #     answer = answer.replace(item, num.get(item))
    return int(answer)